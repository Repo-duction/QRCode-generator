# QRCode-generator

## Usage:
- Usage via Git:
    1. ### Setting up git:
    - [Download and install the latest version of Git.](https://git-scm.com/downloads)
    - (Optional) [Set your username in Git.](https://help.github.com/articles/setting-your-username-in-git)
    - (Optional) [Set your commit email address in Git.](https://help.github.com/articles/setting-your-commit-email-address-in-git)
    2. ### Cloning the Repo in your local machine
    - Run ``git clone git@github.com:Repo-duction/QRCode-generator.git``
    - ``cd QRCode-generator``

- Installing dependencies and running code
    - ``pip install -r requirements.txt``
    - ``cd QR``
    - ``python qrGen.py``
    
QR Code is a machine-readable matrix barcode that uniquely represents information. With the increase in optical capabilities of smartphones, the use of QR codes started increasing.

In this project, we will build a QR Code generator using Python Modules.
Generate QR Code in Python

We will be using Tkinter and Qrcode modules in Python to build this project. We use the Tkinter module to build the GUI to take the following inputs:

    1.text/URL to convert to QR Code
    2.location to save the QR code with name
    3.size of the QR code.

Then we generate the QR code from the above inputs and save in the given location using the qrcode module.
