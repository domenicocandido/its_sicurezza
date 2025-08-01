import sys
import random

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <filr name>")

# 1) devo leggere tutti  i file

data = None
with open(sys.argv[1], 'rb') as f:
    data = f.read()

# 2) prendo un byte casuale del file

pos = random.randint(0, len(data) - 1)

# 3) prendo un bit casuale nel byte

bit = random.randint(0, 7)

# 4) ora devo cambiare il valore del bit  <bit> di data[pos] (uso lo xor)
# in sostanza devo costruire un byte di tutti 0 e un solo 1 nel posto gisuto

byte = data[pos]
byte = byte ^ (1 << bit) # ho rovesciato il bit bit-esimo el byte

data = data[:pos - 1] + bytes([byte]) + data[pos + 1:]

with open(sys.argv[1], 'wb') as f:
    f.write(data)

print(f"Modificato il bit {bit} ap posto {pos} nel file {sys.argv[1]}")