import time
from bluetooth import *
import carcmd

ADDR = '00:06:66:61:A3:EA'

sock = BluetoothSocket(RFCOMM)
sock.connect((ADDR, 1))
time.sleep(2)
sock.send((0x8140).to_bytes(2, byteorder='big'))
time.sleep(2)
sock.send((0x815C).to_bytes(2, byteorder='big'))
time.sleep(2)
sock.send((0x817F).to_bytes(2, byteorder='big'))
time.sleep(2)
sock.send((0x8122).to_bytes(2, byteorder='big'))
time.sleep(2)
sock.send((0x8100).to_bytes(2, byteorder='big'))
time.sleep(2)
sock.close()