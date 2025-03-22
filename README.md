PyKey - Simple Keylogger for Learning Purposes

Overview:

PyKey is a simple keylogger program built in Python using the pynput library. It is designed for educational purposes only to help you understand how keylogging works and how to prevent such attacks. The keylogger captures keystrokes and logs them into a text file, which can be used to analyze input events and better understand system security vulnerabilities.

Important: This program is NOT meant for illegal activities. It should only be used in controlled environments (e.g., your own lab or with explicit permission) to learn about cybersecurity and keylogging concepts.
Features

Logs keystrokes and stores them in a plain text file.

Detects special keys (space, shift, control, backspace, etc.).

Simple interface, easy to modify for educational use.

Setup Instructions:

Install Dependencies: To run PyKey, you need to install the pynput library. Install it using the following command:

    pip install pynput

Run the Program: After installing the dependencies, you can run the keylogger by executing the Python script:

    python pykey.py

The program will start listening for keyboard input and log it into the specified text file (log.txt).

Viewing the Log: The keystrokes are saved in the file located at:

    log.txt

You can open this file with any text editor to view the logged keys.


Ethical Use Disclaimer:

This program is for educational purposes only. It should not be used for any illegal activities, such as unauthorized surveillance or data collection. The purpose of PyKey is to help you learn how keylogging works in a controlled, ethical environment (e.g., your own lab or with explicit permission).

Important Notes:

- Only use this program on systems you own or have explicit permission to test.

- Never use this program for malicious purposes or without consent.

- Always respect privacy and ethical guidelines when exploring cybersecurity concepts.

Future Improvements

You can modify this program to add the following features:

- Store logs in an encrypted file.

- Send logs via email (for educational purposes, not for unauthorized use).

- Detect and prevent unauthorized access to logged data.

License

This project is licensed under the MIT License.
