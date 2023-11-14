# Enigma Machine User Manual

## Introduction

The Enigma machine was a cipher machine used during World War II to encrypt and decrypt secret messages. This software application is a faithful replication of the Enigma machine's functionality, allowing you to encrypt and decrypt messages just like in the war era.

## Installation

To use the Enigma machine application, you need to have Python installed on your computer. You can download Python from the official website: [python.org](https://www.python.org/).

Once you have Python installed, you can follow these steps to set up the Enigma machine application:

1. Download the source code for the Enigma machine application from the provided repository.

2. Open a terminal or command prompt and navigate to the directory where you downloaded the source code.

3. Create a virtual environment for the Enigma machine application by running the following command:

   ```
   python -m venv enigma-env
   ```

4. Activate the virtual environment by running the appropriate command for your operating system:

   - On Windows:

     ```
     enigma-env\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source enigma-env/bin/activate
     ```

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Enigma machine application, follow these steps:

1. Open a terminal or command prompt and navigate to the directory where you downloaded the source code.

2. Activate the virtual environment by running the appropriate command (as mentioned in the installation steps).

3. Run the application by executing the `main.py` file:

   ```
   python main.py
   ```

4. The Enigma machine application window will open.

5. Enter the message you want to encrypt in the "Input" field.

6. Click the "Encrypt" button.

7. The encrypted message will be displayed in the "Output" field.

8. To decrypt a message, simply enter the encrypted message in the "Input" field and click the "Encrypt" button again.

## Customization

If you want to customize the Enigma machine's settings, such as the rotor configurations or the reflector wiring, you can modify the code in the following files:

- `enigma.py`: This file contains the `Enigma` class, which represents the Enigma machine. You can add or remove rotors and set the reflector wiring.

- `rotor.py`: This file contains the `Rotor` class, which represents a rotor in the Enigma machine. You can modify the rotor wiring.

- `reflector.py`: This file contains the `Reflector` class, which represents the reflector in the Enigma machine. You can modify the reflector wiring.

Please note that modifying the Enigma machine's settings may affect its functionality and compatibility with historical Enigma machines.

## Conclusion

Congratulations! You have successfully installed and used the Enigma machine application. Enjoy encrypting and decrypting messages just like in the World War II era. If you have any questions or need further assistance, please don't hesitate to contact our support team.