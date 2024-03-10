# DISCLAIMER
**This KEYLOGGER  is for education/research purposes only. The author takes NO responsibility and/or liability for how you choose to use any of the tools/source code/any files provided.
 The author and anyone affiliated with will not be liable for any losses and/or damages in connection with the use of ANY files provided with This KEYLOGGER.
 By using KEYLOGGER or any files included, you understand that you are AGREEING TO USE AT YOUR OWN RISK. Once again this KEYLOGGER and ALL files included are for EDUCATION and/or RESEARCH purposes ONLY.
 KEYLOGGER is ONLY intended to be used on your pen testing labs, or with explicit consent from the owner of the property being tested.** 

# Overview
**Welcome to the Advanced Keylogger and System Information Gathering Tool repository! This project is designed to showcase advanced keylogging capacity alongside system information-gathering capabilities. 
The tool is equipped to gather essential data from the target system and discreetly send it via email for further analysis.**

# Usage
*Prerequisites*

**Before using the tool, ensure you have the following prerequisites:**
- Python 3.x installed (https://www.python.org/downloads/)
- Required Python libraries (specified in requirements.txt)

# Installation
  - clone the repo to your local machine.
  - Navigate to the project directory.
## **Install the required dependencies**.
    pip install -r requirements.txt 

## Email Configuration

Before using the email functionality in the code, ensure you have configured the email parameters. Open the script and locate the following lines:

```python
fromaddr = email_address
password = email_password
toaddr = recipient_email
```
## Additional Parameters:
Check the script for additional parameters, such as file_path, extend, and keys_information. Adjust these parameters based on your requirements.

# TO DO
- Add Clipboard Logging
- Screenshot capability
- Audio collection
- File Encryption

