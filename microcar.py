from bluetooth import *

ADDR = '00:06:66:61:A3:EA'


STEER = [b'\x81' + x.to_bytes(1, byteorder='big') for x in range(128)]
SPEED = [b'\x82' + x.to_bytes(1, byteorder='big') for x in range(128)]

SIDELIGHT_LEFT = [b'\x83\x00', b'\x83\x01',  b'\x83\x02',  b'\x83\x03', b'\x83\x04' ]
SIDELIGHT_RIGHT = [b'\x84\x00', b'\x84\x01',  b'\x84\x02',  b'\x84\x03', b'\x84\x04' ]

LIGHTS = [b'\x85\x00', b'\x85\x01', b'\x85\x02']
HORN = [b'\x86\x00', b'\x86\x01']


class Car(object):
    def __init__(self, address):
        self.address = address
        self.sock = BluetoothSocket(RFCOMM)
        self.light = 0
        self.left_sidelight = 0
        self.right_sidelight = 0
    
    def init(self):
        self.sock.connect((self.address, 1))

    def steer(self, value):
        self.sock.send(STEER[int(value*63)])
    
    def drive(self, value):
        self.sock.send(SPEED[int(value*63)])
    
    def toggle_light(self):
        self.light += 1
        self.sock.send(LIGHTS[self.light % len(LIGHTS)])

    
    def toggle_horn(self, horn=True):
        if horn:
            self.sock.send(HORN[1])
        else:
            self.sock.send(HORN[0])

    
    def toggle_left_sidelight(self):
        self.left_sidelight += 1
        self.sock.send(SIDELIGHT_LEFT[self.left_sidelight % len(SIDELIGHT_LEFT)])

    def toggle_right_sidelight(self):
        self.right_sidelight += 1
        self.sock.send(SIDELIGHT_RIGHT[self.right_sidelight % len(SIDELIGHT_RIGHT)])

    
    def __del__(self):
        self.sock.close()