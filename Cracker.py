import argparse
import hashlib
import random
import sys

from colorama import Fore
from termcolor import colored

rainbow = ['red', 'green', 'green', 'blue', 'magenta', 'cyan']
r0 = random.randint(0, 5)
r1 = random.randint(0, 5)
r2 = random.randint(0, 5)
r3 = random.randint(0, 5)
r4 = random.randint(0, 5)

print(colored("\t┌───────────────────────┐", rainbow[r0]))
print(colored("\t│ ╔═╗┬─┐╔═╗┌─┐╦╔═┌─┐╦═╗ │", rainbow[r1]))
print(colored("\t│ ║  ├┬┘╠═╣│  ╠╩╗├┤ ╠╦╝ │", rainbow[r2]))
print(colored("\t│ ╚═╝┴└─╩ ╩└─┘╩ ╩└─┘╩╚═ │", rainbow[r3]))
print(colored("\t└────────0xb14cky───────┘\n", rainbow[r4]))

parser = argparse.ArgumentParser(
    description="A Simple Hash Cracker Tool !!",
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=47)
)
parser.add_argument("-l", "--list", help="List Available Algorithms", action='store_true')
parser.add_argument("-hs", "--hash", help="Any Specific Port", type=str)
parser.add_argument("-t", "--hashtype", help="Username File", type=str)
parser.add_argument("-w", "--wordlist", help="Password File", type=str)
parser.add_argument("-o", "--output", help="Saving Output In Another File", type=str)
args = parser.parse_args()

avail_algo = list(hashlib.algorithms_available)

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

if args.list:
    print("Algorithms Available :-\n")
    for algo in avail_algo:
        print(f"{algo}")


def print_hash(hash, passwd, hashtype):
    print(Fore.GREEN, f"Hash : {hash}", Fore.RESET)
    print(Fore.GREEN, f"Password Found : {passwd}", Fore.RESET)
    print(Fore.GREEN, f"Hash Type : {hashtype}", Fore.RESET)
    pass


if args.hash and args.hashtype and args.wordlist:
    with open(args.wordlist, "r") as wordlist:
        words = wordlist.readlines()
        for passwds in words:
            passwds = passwds.strip("\n").strip("\r")
            if args.hashtype == "MD5" or "md5":
                hash_object = hashlib.md5(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "SHA-1" or "sha-1":
                hash_object = hashlib.sha1(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "SHA-256" or "sha-256":
                hash_object = hashlib.sha256(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "SHA-512" or "sha-512":
                hash_object = hashlib.sha512(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "SHA-384" or "sha-384":
                hash_object = hashlib.sha384(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "SHA3-224" or "sha3-224":
                hash_object = hashlib.sha3_224(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "SHA3-256" or "sha3-256":
                hash_object = hashlib.sha3_256(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "SHA3-384" or "sha3-384":
                hash_object = hashlib.sha3_384(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "SHA3-512" or "sha3-512":
                hash_object = hashlib.sha3_512(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "BLACK2B" or "black2b":
                hash_object = hashlib.blake2b(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "BLACK2S" or "blake2s":
                hash_object = hashlib.blake2s(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "SHAKE-128" or "shake-128":
                hash_object = hashlib.shake_128(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest(128)
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "SHAKE-256" or "shake-256":
                hash_object = hashlib.shake_256(f"{passwds}".encode('utf-8'))
                hashed = hash_object.hexdigest(256)
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "SM3" or "sm3":
                passwd = passwds.encode('utf-8')
                hash_object = hashlib.new('sm3', passwd)
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "RIPEMD160" or "ripemd160":
                passwd = passwds.encode('utf-8')
                hash_object = hashlib.new('ripemd160', passwd)
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "WHIRLPOOL" or "whirlpool":
                passwd = passwds.encode('utf-8')
                hash_object = hashlib.new('whirlpool', passwd)
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            if args.hashtype == "MD4" or "md4":
                passwd = passwds.encode('utf-8')
                hash_object = hashlib.new('md4', passwd)
                hashed = hash_object.hexdigest()
                if args.hash == hashed:
                    print_hash(args.hash, passwds, args.hashtype)
            else:
                print("Use -l or --list to see available algorithms !! ")


# mdc2
# md5-sha1
# sha512_224
# sha512_256
