'''
This is the main file of the Enigma machine application.
'''
import tkinter as tk
from enigma import Enigma
from rotor import Rotor
from reflector import Reflector
class EnigmaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Enigma Machine")
        self.enigma = Enigma()
        self.input_label = tk.Label(self, text="Input:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self)
        self.input_entry.pack()
        self.output_label = tk.Label(self, text="Output:")
        self.output_label.pack()
        self.output_entry = tk.Entry(self, state="readonly")
        self.output_entry.pack()
        self.encrypt_button = tk.Button(self, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack()
    def encrypt(self):
        plaintext = self.input_entry.get()
        ciphertext = self.enigma.encrypt(plaintext)
        self.output_entry.configure(state="normal")
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, ciphertext)
        self.output_entry.configure(state="readonly")
if __name__ == "__main__":
    app = EnigmaApp()
    app.mainloop()