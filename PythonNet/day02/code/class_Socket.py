from socket import *


class socket(_socket.socket):

    """A subclass of _socket.socket adding the makefile() method."""

    __slots__ = ["__weakref__", "_io_refs", "_closed"]

    def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
        # For user code address family and type values are IntEnum members, but
        # for the underlying _socket.socket they're just integers. The
        # constructor of _socket.socket converts the given argument to an
        # integer automatically.
        if fileno is None:
            if family == -1:
                family = AF_INET
            if type == -1:
                type = SOCK_STREAM
            if proto == -1:
                proto = 0
        _socket.socket.__init__(self, family, type, proto, fileno)
        self._io_refs = 0
        self._closed = False

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if not self._closed:
            self.close()

    def __repr__(self):
        """Wrap __repr__() to reveal the real class name and socket
        address(es).
        """
        closed = getattr(self, '_closed', False)
        s = "<%s.%s%s fd=%i, family=%s, type=%s, proto=%i" \
            % (self.__class__.__module__,
               self.__class__.__qualname__,
               " [closed]" if closed else "",
               self.fileno(),
               self.family,
               self.type,
               self.proto)
        if not closed:
            try:
                laddr = self.getsockname()
                if laddr:
                    s += ", laddr=%s" % str(laddr)
            except error:
                pass
            try:
                raddr = self.getpeername()
                if raddr:
                    s += ", raddr=%s" % str(raddr)
            except error:
                pass
        s += '>'
        return s

    def __getstate__(self):
        raise TypeError("Cannot serialize socket object")

    def dup(self):
        """dup() -> socket object

        Duplicate the socket. Return a new socket object connected to the same
        system resource. The new socket is non-inheritable.
        """
        fd = dup(self.fileno())
        sock = self.__class__(self.family, self.type, self.proto, fileno=fd)
        sock.settimeout(self.gettimeout())
        return sock

    def accept(self):
        """accept() -> (socket object, address info)

        Wait for an incoming connection.  Return a new socket
        representing the connection, and the address of the client.
        For IP sockets, the address info is a pair (hostaddr, port).
        """
        fd, addr = self._accept()
        sock = socket(self.family, self.type, self.proto, fileno=fd)
        # Issue #7995: if no default timeout is set and the listening
        # socket had a (non-zero) timeout, force the new socket in blocking
        # mode to override platform-specific socket flags inheritance.
        if getdefaulttimeout() is None and self.gettimeout():
            sock.setblocking(True)
        return sock, addr

    def makefile(self, mode="r", buffering=None, *,
                 encoding=None, errors=None, newline=None):
        """makefile(...) -> an I/O stream connected to the socket

        The arguments are as for io.open() after the filename, except the only
        supported mode values are 'r' (default), 'w' and 'b'.
        """
        # XXX refactor to share code?
        if not set(mode) <= {"r", "w", "b"}:
            raise ValueError("invalid mode %r (only r, w, b allowed)" % (mode,))
        writing = "w" in mode
        reading = "r" in mode or not writing
        assert reading or writing
        binary = "b" in mode
        rawmode = ""
        if reading:
            rawmode += "r"
        if writing:
            rawmode += "w"
        raw = SocketIO(self, rawmode)
        self._io_refs += 1
        if buffering is None:
            buffering = -1
        if buffering < 0:
            buffering = io.DEFAULT_BUFFER_SIZE
        if buffering == 0:
            if not binary:
                raise ValueError("unbuffered streams must be binary")
            return raw
        if reading and writing:
            buffer = io.BufferedRWPair(raw, raw, buffering)
        elif reading:
            buffer = io.BufferedReader(raw, buffering)
        else:
            assert writing
            buffer = io.BufferedWriter(raw, buffering)
        if binary:
            return buffer
        text = io.TextIOWrapper(buffer, encoding, errors, newline)
        text.mode = mode
        return text

    if hasattr(os, 'sendfile'):

        def _sendfile_use_sendfile(self, file, offset=0, count=None):
            self._check_sendfile_params(file, offset, count)
            sockno = self.fileno()
            try:
                fileno = file.fileno()
            except (AttributeError, io.UnsupportedOperation) as err:
                raise _GiveupOnSendfile(err)  # not a regular file
            try:
                fsize = os.fstat(fileno).st_size
            except OSError as err:
                raise _GiveupOnSendfile(err)  # not a regular file
            if not fsize:
                return 0  # empty file
            blocksize = fsize if not count else count

            timeout = self.gettimeout()
            if timeout == 0:
                raise ValueError("non-blocking sockets are not supported")
            # poll/select have the advantage of not requiring any
            # extra file descriptor, contrarily to epoll/kqueue
            # (also, they require a single syscall).
            if hasattr(selectors, 'PollSelector'):
                selector = selectors.PollSelector()
            else:
                selector = selectors.SelectSelector()
            selector.register(sockno, selectors.EVENT_WRITE)

            total_sent = 0
            # localize variable access to minimize overhead
            selector_select = selector.select
            os_sendfile = os.sendfile
            try:
                while True:
                    if timeout and not selector_select(timeout):
                        raise _socket.timeout('timed out')
                    if count:
                        blocksize = count - total_sent
                        if blocksize <= 0:
                            break
                    try:
                        sent = os_sendfile(sockno, fileno, offset, blocksize)
                    except BlockingIOError:
                        if not timeout:
                            # Block until the socket is ready to send some
                            # data; avoids hogging CPU resources.
                            selector_select()
                        continue
                    except OSError as err:
                        if total_sent == 0:
                            # We can get here for different reasons, the main
                            # one being 'file' is not a regular mmap(2)-like
                            # file, in which case we'll fall back on using
                            # plain send().
                            raise _GiveupOnSendfile(err)
                        raise err from None
                    else:
                        if sent == 0:
                            break  # EOF
                        offset += sent
                        total_sent += sent
                return total_sent
            finally:
                if total_sent > 0 and hasattr(file, 'seek'):
                    file.seek(offset)
    else:
        def _sendfile_use_sendfile(self, file, offset=0, count=None):
            raise _GiveupOnSendfile(
                "os.sendfile() not available on this platform")

    def _sendfile_use_send(self, file, offset=0, count=None):
        self._check_sendfile_params(file, offset, count)
        if self.gettimeout() == 0:
            raise ValueError("non-blocking sockets are not supported")
        if offset:
            file.seek(offset)
        blocksize = min(count, 8192) if count else 8192
        total_sent = 0
        # localize variable access to minimize overhead
        file_read = file.read
        sock_send = self.send
        try:
            while True:
                if count:
                    blocksize = min(count - total_sent, blocksize)
                    if blocksize <= 0:
                        break
                data = memoryview(file_read(blocksize))
                if not data:
                    break  # EOF
                while True:
                    try:
                        sent = sock_send(data)
                    except BlockingIOError:
                        continue
                    else:
                        total_sent += sent
                        if sent < len(data):
                            data = data[sent:]
                        else:
                            break
            return total_sent
        finally:
            if total_sent > 0 and hasattr(file, 'seek'):
                file.seek(offset + total_sent)

    def _check_sendfile_params(self, file, offset, count):
        if 'b' not in getattr(file, 'mode', 'b'):
            raise ValueError("file should be opened in binary mode")
        if not self.type & SOCK_STREAM:
            raise ValueError("only SOCK_STREAM type sockets are supported")
        if count is not None:
            if not isinstance(count, int):
                raise TypeError(
                    "count must be a positive integer (got {!r})".format(count))
            if count <= 0:
                raise ValueError(
                    "count must be a positive integer (got {!r})".format(count))

    def sendfile(self, file, offset=0, count=None):
        """sendfile(file[, offset[, count]]) -> sent

        Send a file until EOF is reached by using high-performance
        os.sendfile() and return the total number of bytes which
        were sent.
        *file* must be a regular file object opened in binary mode.
        If os.sendfile() is not available (e.g. Windows) or file is
        not a regular file socket.send() will be used instead.
        *offset* tells from where to start reading the file.
        If specified, *count* is the total number of bytes to transmit
        as opposed to sending the file until EOF is reached.
        File position is updated on return or also in case of error in
        which case file.tell() can be used to figure out the number of
        bytes which were sent.
        The socket must be of SOCK_STREAM type.
        Non-blocking sockets are not supported.
        """
        try:
            return self._sendfile_use_sendfile(file, offset, count)
        except _GiveupOnSendfile:
            return self._sendfile_use_send(file, offset, count)

    def _decref_socketios(self):
        if self._io_refs > 0:
            self._io_refs -= 1
        if self._closed:
            self.close()

    def _real_close(self, _ss=_socket.socket):
        # This function should not reference any globals. See issue #808164.
        _ss.close(self)

    def close(self):
        # This function should not reference any globals. See issue #808164.
        self._closed = True
        if self._io_refs <= 0:
            self._real_close()

    def detach(self):
        """detach() -> file descriptor

        Close the socket object without closing the underlying file descriptor.
        The object cannot be used after this call, but the file descriptor
        can be reused for other purposes.  The file descriptor is returned.
        """
        self._closed = True
        return super().detach()

    @property
    def family(self):
        """Read-only access to the address family for this socket.
        """
        return _intenum_converter(super().family, AddressFamily)

    @property
    def type(self):
        """Read-only access to the socket type.
        """
        return _intenum_converter(super().type, SocketKind)

    if os.name == 'nt':
        def get_inheritable(self):
            return os.get_handle_inheritable(self.fileno())
        def set_inheritable(self, inheritable):
            os.set_handle_inheritable(self.fileno(), inheritable)
    else:
        def get_inheritable(self):
            return os.get_inheritable(self.fileno())
        def set_inheritable(self, inheritable):
            os.set_inheritable(self.fileno(), inheritable)
    get_inheritable.__doc__ = "Get the inheritable flag of the socket"
    set_inheritable.__doc__ = "Set the inheritable flag of the socket"

def fromfd(fd, family, type, proto=0):
    """ fromfd(fd, family, type[, proto]) -> socket object

    Create a socket object from a duplicate of the given file
    descriptor.  The remaining arguments are the same as for socket().
    """
    nfd = dup(fd)
    return socket(family, type, proto, nfd)

if hasattr(_socket.socket, "share"):
    def fromshare(info):
        """ fromshare(info) -> socket object

        Create a socket object from the bytes object returned by
        socket.share(pid).
        """
        return socket(0, 0, 0, info)
    __all__.append("fromshare")

if hasattr(_socket, "socketpair"):

    def socketpair(family=None, type=SOCK_STREAM, proto=0):
        """socketpair([family[, type[, proto]]]) -> (socket object, socket object)

        Create a pair of socket objects from the sockets returned by the platform
        socketpair() function.
        The arguments are the same as for socket() except the default family is
        AF_UNIX if defined on the platform; otherwise, the default is AF_INET.
        """
        if family is None:
            try:
                family = AF_UNIX
            except NameError:
                family = AF_INET
        a, b = _socket.socketpair(family, type, proto)
        a = socket(family, type, proto, a.detach())
        b = socket(family, type, proto, b.detach())
        return a, b

else:

    # Origin: https://gist.github.com/4325783, by Geert Jansen.  Public domain.
    def socketpair(family=AF_INET, type=SOCK_STREAM, proto=0):
        if family == AF_INET:
            host = _LOCALHOST
        elif family == AF_INET6:
            host = _LOCALHOST_V6
        else:
            raise ValueError("Only AF_INET and AF_INET6 socket address families "
                             "are supported")
        if type != SOCK_STREAM:
            raise ValueError("Only SOCK_STREAM socket type is supported")
        if proto != 0:
            raise ValueError("Only protocol zero is supported")

        # We create a connected TCP socket. Note the trick with
        # setblocking(False) that prevents us from having to create a thread.
        lsock = socket(family, type, proto)
        try:
            lsock.bind((host, 0))
            lsock.listen()
            # On IPv6, ignore flow_info and scope_id
            addr, port = lsock.getsockname()[:2]
            csock = socket(family, type, proto)
            try:
                csock.setblocking(False)
                try:
                    csock.connect((addr, port))
                except (BlockingIOError, InterruptedError):
                    pass
                csock.setblocking(True)
                ssock, _ = lsock.accept()
            except:
                csock.close()
                raise
        finally:
            lsock.close()
        return (ssock, csock)
    __all__.append("socketpair")

socketpair.__doc__ = """socketpair([family[, type[, proto]]]) -> (socket object, socket object)
Create a pair of socket objects from the sockets returned by the platform
socketpair() function.
The arguments are the same as for socket() except the default family is AF_UNIX
if defined on the platform; otherwise, the default is AF_INET.
"""

_blocking_errnos = { EAGAIN, EWOULDBLOCK }
