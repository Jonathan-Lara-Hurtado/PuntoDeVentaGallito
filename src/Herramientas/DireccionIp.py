import platform
import socket
import netifaces as ni
import platform
if platform.system() == 'Windows':
    import winreg as wr
else:
    pass

from  pprint import pprint
from netifaces import interfaces, ifaddresses, AF_INET

"""
Referencias paginas
https://stackoverflow.com/questions/19805654/python-try-finally-block-returns
"""

class DireccionIp:

    def __init__(self):
        self.interfaces = ni.interfaces()

    def get_SistemaOperativo(self):
        return platform.system()

	
    def ip4_addresses(self):
       ip_list = []
       for interface in interfaces():
           for link in ifaddresses(interface)[AF_INET]:
               ip_list.append(link['addr'])
       return ip_list
    """
    https://stackoverflow.com/questions/49195864/how-to-get-all-ip-addresses-using-python-windows
    """
    def get_DirrecionIp(self):
        if self.get_SistemaOperativo() == 'Linux':
            try:
                ip = ni.ifaddresses(self.interfaces[1])[ni.AF_INET][0]['addr']
                return ip
            except:
                ip = ni.ifaddresses(self.interfaces[2])[ni.AF_INET][0]['addr']
                return ip
        elif self.get_SistemaOperativo() == 'Windows':
            x = self.ip4_addresses()
            return x[0]
