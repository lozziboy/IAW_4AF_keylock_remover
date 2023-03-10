#!/usr/bin/python3

# You need to install pyserial
# Usage in terminal: dump_eeprom.py [comport] [filename]
# ex. dump_eeprom.py COM8 eDump.hex

import serial, sys


if len(sys.argv) != 3:
  print("Usage : dump_eeprom.py [comport] [filename]")
  exit(0)

device = sys.argv[1]
filename = sys.argv[2]


port = serial.Serial(device, baudrate=115200, parity=serial.PARITY_NONE, rtscts=0,
bytesize = 8)

# Reset Arduino
port.setDTR(False) # Drop DTR
port.setDTR(True)  # UP the DTR back

f = open(filename, "wb")

print(port.readline().decode("utf-8"))
port.write(b"read 0 7FF\n")

# Echo
line = port.readline()
# Data
line = port.readline()
bytelist=line.decode("utf-8").strip().split(' ')

i = 0
addr = 0
line = ""
for h in bytelist:
  if i == 0:
    sys.stdout.write(hex(addr).zfill(5) + " : ")
  code = int(h, 16)
  if code > 32 and code < 126:
    line += code.to_bytes(1, "big").decode("ascii")
  else:
    line += "."
  sys.stdout.write(h.zfill(2) + " ")
  b = bytes.fromhex(h.zfill(2))
  f.write(b)
  i+=1
  addr+=1
  if i == 16:
    sys.stdout.write(" " + line)
    sys.stdout.write("\n")
    line = ""
    i = 0
  
f.close()
