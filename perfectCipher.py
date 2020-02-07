#! /usr/bin/python3

import random
import sys

def encrypt(filename):
    random.seed(seed)
    f = open(filename, "rb")
    s = f.read()
    f.close()
    plaintxt = ''.join([bin(x)[2:].zfill(8) for x in s])
    encryptedlist = [random.randint(0, 1) ^ int(x) for x in plaintxt]
    f = open(filename + ".enc", "wb")
    for i in range(0, len(encryptedlist), 8):
        f.write(struct.pack("B", int(''.join([str(x) for x in encryptedlist[i:i+8]]), 2)))
    f.close()

def decrypt(filename):
    random.seed(seed)
    f = open(filename, "rb")
    s = f.read()
    f.close()
    encryptedtxt = ''.join([bin(x)[2:].zfill(8) for x in s])
    plainlist = [random.randint(0, 1) ^ int(x) for x in encryptedtxt]
    f = open(filename[:-4] + ".dec", "wb")
    for i in range(0, len(plainlist), 8):
        f.write(struct.pack("B", int(''.join([str(x) for x in plainlist[i:i+8]]), 2)))
    f.close()

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("help: '-h' or '--h'")
        sys.exit()
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("=" * 64)
        print("perfectCipher.py <mode> <filename> <seed>")
        print()
        print("<mode>: '--encrypt' or '--decrypt'")
        print("<filename>: input filename")
        print("<seed>: input int")
        print("=" * 64)
        sys.exit()
    mode = sys.argv[1]
    filename = sys.argv[2]
    seed = sys.argv[3]
    if mode == "--encrypt" or mode == "-e":
        encrypt(filename)
    elif mode == "--decrypt" or mode == "-d":
        decrypt(filename)