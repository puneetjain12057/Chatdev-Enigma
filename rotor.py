'''
This file contains the Rotor class which represents a rotor in the Enigma machine.
'''
class Rotor:
    def __init__(self, wiring):
        self.wiring = wiring
    def encrypt(self, char, reverse=False):
        if not reverse:
            return self.wiring[char]
        else:
            return self.wiring.index(char)