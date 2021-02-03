#!/bin/python3

import sys # allows command-line args, plus extra
import socket

from datetime import datetime

flags = ["-i", "-p"]

class Scanner:
    def __init__(self, ip, portMax):
        self.ip = ip
        self.portMax = portMax

    def __init__(self, ip):
        self.ip = ip
        self.portMax = "80"

    def __init__(self):
        self.ip = "192.168.1.1"
        self.portMax = "80"

    def __str__(self):
        return "SCANNER: IP = " + self.ip + ", PORT = " + self.portMax

    def banner(self):
        # Banner
        print("=" * 50)
        print("SCANNING TARGET: " + self.ip)
        print("TIME INITIATED: " + str(datetime.now()))
        print("=" * 50)

    def scan(self):
        self.banner()

        try:
            for port in range(50, int(self.portMax)):
                # AF_INET = IPv4, SOCK_STREAM = port
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((self.ip, port)) # returns error indicator
                print("CHECKING PORT {}".format(port))

                if (result == 0):
                    print("PORT {} IS OPEN".format(port))
                s.close()
        except KeyboardInterrupt:
            print()
            print("EXITING PROGRAM")
            sys.exit()
        except socket.gaierror:
            print()
            print("HOSTNAME COULD NOT BE RESOLVED")
            sys.exit()
        except socket.error:
            print()
            print("SERVER CONNECTION COULD NOT BE ESTABLISHED")
            sys.exit()

def getArg(position):
    return sys.argv[position]

def parseSysArgs():
    if (len(sys.argv) < 2):
        exitWithMessage("SYNTAX ERROR, NOT ENOUGH ARGUMENTS", "SYNTAX: python3 port_scanner.py <ip>")

    # Single arg, IP
    if (len(sys.argv) == 2):
        target = getArg(1)
        return Scanner(target)

    # flag : position_in_args
    flagsFound = {}
    # multiple args
    for i in range(1, len(sys.argv)):
        for flag in flags:
            if (flag == sys.argv[i]):
                flagsFound[flag] = i

    print("FOUND FLAGS: " + str(flagsFound))
    print("VERIFYING FLAGS")
    scanner = Scanner()
    # get each flags content
    for key in flagsFound:
        print(key)
        if (key == "-i" or key == "-I"):
            print("IP FLAG RECEIVED")
            ip = sys.argv[flagsFound[key] + 1]
            scanner.ip = ip
        elif (key == "-p" or key == "-P"):
            print("MAX PORT FLAG RECEIVED")
            portMax = sys.argv[flagsFound[key] + 1]
            scanner.portMax = portMax
    
    print("SCANNER: " + str(scanner))
    return scanner
    
def exitWithMessage(error_message, description):
    print(error_message)
    print(description)
    sys.exit()

scanner = parseSysArgs()
scanner.scan()
