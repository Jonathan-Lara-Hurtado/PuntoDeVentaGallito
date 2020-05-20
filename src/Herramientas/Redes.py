import platform
import socket
import netifaces as ni


class Redes:
    def __init__(self):
        self.interfaces = ni.interfaces()

    def get_SistemaOperativo(self):
        return platform.system()

    def get_DireccionIp(self):
        try:
           # print(self.interfaces)
            ip = ni.ifaddresses(self.interfaces[1])[ni.AF_INET][0]['addr']
            return ip
        except:
            ip = ni.ifaddresses(self.interfaces[2])[ni.AF_INET][0]['addr']
            return ip