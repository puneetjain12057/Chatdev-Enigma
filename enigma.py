'''
This file contains the Enigma class which represents the Enigma machine.
'''
class Enigma:
    def __init__(self):
        self.rotors = []
        self.reflector = None
    def add_rotor(self, rotor):
        self.rotors.append(rotor)
    def set_reflector(self, reflector):
        self.reflector = reflector
    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            encrypted_char = char
            for rotor in self.rotors:
                encrypted_char = rotor.encrypt(encrypted_char)
            encrypted_char = self.reflector.reflect(encrypted_char)
            for rotor in reversed(self.rotors):
                encrypted_char = rotor.encrypt(encrypted_char, reverse=True)
            ciphertext += encrypted_char
        return ciphertext