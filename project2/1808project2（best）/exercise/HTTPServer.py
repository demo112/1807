from socket import socket
import re


class Httpserver(object):

    def __init__(self, address):
        self.address = address
        self.ip = address[0]
        self.port = address[1]