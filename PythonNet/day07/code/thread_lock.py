import threading

a = b = 0

def value():
    while True:
        lock.acquire()
        if a != b:
            print("a = %s b = %s" % (a, b))
        lock.release()

t = threading.Thread(target=value)
e = threading.Event()
lock = threading.Lock()
t.start()

while True:
    with lock:
        a += 1
        b += 1

t.join()
