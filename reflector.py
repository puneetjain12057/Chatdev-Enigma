'''
This file contains the Reflector class which represents the reflector in the Enigma machine.
'''
class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring
    def reflect(self, char):
        return self.wiring[char]