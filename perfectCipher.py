#! /usr/bin/python3

import random
import sys
import struct

def encrypt(filename):
    random.seed(seed)
    plain_file = open(filename, "rb")
    encrypted_file = open(filename + ".enc", "wb")
    while True:
        plain_text = plain_file.readline()
        if plain_text == b"":
            break
        plain_text = ''.join([bin(x)[2:].zfill(8) for x in plain_text])
        encrypted_list = [random.randint(0, 1) ^ int(x) for x in plain_text]
        for i in range(0, len(encrypted_list), 8):
            encrypted_file.write(struct.pack("B", int(''.join([str(x) for x in encrypted_list[i:i+8]]), 2)))
    plain_file.close()
    encrypted_file.close()

def decrypt(filename):
    random.seed(seed)
    encrypted_file = open(filename, "rb")
    decrypted_file = open(filename[:-4] + ".dec", "wb")
    while True:
        encrypted_text = encrypted_file.readline()
        if encrypted_text == b"":
            break
        encrypted_text = ''.join([bin(x)[2:].zfill(8) for x in encrypted_text])
        decrypted_list = [random.randint(0, 1) ^ int(x) for x in encrypted_text]
        for i in range(0, len(decrypted_list), 8):
            decrypted_file.write(struct.pack("B", int(''.join([str(x) for x in decrypted_list[i:i+8]]), 2)))
    encrypted_file.close()
    decrypted_file.close()

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
