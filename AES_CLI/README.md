# 🔐 AES Encryption Tool (CLI & GUI)

This folder includes two versions of an AES encryption tool:
- A *Command-Line Interface (CLI)* version
- A *Graphical User Interface (GUI)* version

Both tools demonstrate file encryption and decryption using a 16-character AES key.

---

## 📦 Requirements

- Python 3.x
- Install required module:
```bash
pip install cryptography


# Run the tool from the terminal
python aes_cli_tool.py [encrypt|decrypt] <input_file> <output_file> [--key <16_char_key>]


# Encrypt a cli file
python aes_cli_tool.py encrypt example.txt encrypted_cli_tool.bin --key your16charKeyHere


# decrypt a cli file
python aes_cli_tool.py decrypt encrypted_cli_tool.bin decrypted_cli_tool.txt --key your16charKeyHere


# Launch the GUI
python aes_gui.py 


## 📄 Output Files and Explanation

All tools use the same input file: example.txt

| Tool | Encrypted Output | Decrypted Output |
|------|------------------|------------------|
| CLI  | encrypted_cli_tool.bin | decrypted_cli_tool.txt |
| GUI  | encrypted_gui.txt      | decrypted_gui.txt      |

### 🔍 Notes

- encrypted_cli_tool.bin and decrypted_cli_tool.txt are the outputs from the *CLI tool*
- encrypted_gui.txt and decrypted_gui.txt are from the *GUI tool*
- All were created using the same input: example.txt
- This structure proves that both tools work and output is accurate



## ✅ Tool Tested Successfully
- Platform: Windows 11
- Python Version: 3.11
- Last Tested: June 6, 2025
- Command Used: [your_command_here]
- Status: ✅ Ran successfully, no errors