# Cryptography - Caeser Cipher

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview

## Getting Started

First, make sure that you have python3 installed:
```
$ python3 --version
Python 3.7.5
```
If you do not:
```
$ brew install python
```
You need to have the files locally. Click on the green clone or download button and Download ZIP:

![Click_to_download](assets/Click_to_download.png)


In your command line, navigate to this directory:
```
$ cd ~  ##this is your root directory
$ cd Downloads  ##by default: Downloads is a directory inside of your root; and where your file will be downloaded
$ cd caesar-cipher ##and now you are in this directory
```
This module can be tested by using pytest. 

## Functionality/Architecture
This module is using the principals of a caesar cipher to encrypt and decrypt messages.

The encryption function is reading in a string and "shifting" every letter to a different character. A list of every letter in the english alphabet is defined and can be used to determine which letter a given letter will shift to. The "key" is the number of indices that the letters must shift to create the caesar cipher. 

The decryption method is given an encrypted caesar cipher, based on a 26 letter alphabet, and it returns the decrypted version. A corpus of english words is being used to test against. When the decryption function is invoked it tries to shift by every key between 1 and 26, then tests what gets returned against the corpus. The version that most resembles english is returned as the decrypted string.

## Change Log
Sun Jan 05 2020 17:55:59 <br>Created caesar cipher based on 26 letter alphabet. Created decryption method as well.

