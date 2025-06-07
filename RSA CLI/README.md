---

# 2. RSA_CLI/README.md

markdown
# RSA_CLI - RSA Public/Private Key Encryption Tool

This tool provides RSA key generation, encryption, and decryption from the command line.

## Features
- Generate RSA key pairs.
- Encrypt messages with public key.
- Decrypt messages with private key.

## Usage

Generate keys:

bash
python rsa_tool.py --generate-keys --keysize 2048 


# Encrypt message
python rsa_tool.py --encrypt --pubkey public_key.pem --input message.txt --output encrypted.bin


# Decrypt message
python rsa_tool.py --decrypt --privkey private_key.pem --input encrypted.bin --output decrypted.txt


## ✅ Tool Tested Successfully
- Platform: Windows 11
- Python Version: 3.11
- Last Tested: June 6, 2025
- Command Used: [your_command_here]
- Status: ✅ Ran successfully, no errors