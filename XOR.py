from functools import reduce

s:str = input("Inserire la stringa da decifrare: ")
key:int = int(input("Inserire la chiave: "))

cifrato = []

for c in s:
    cifrato.append(ord(c) ^ key)

print(cifrato)

codice_decifrato = "".join([chr(l^57) for l in cifrato])

print(codice_decifrato)

#cifrare e decifrare senza list comprhension

print(reduce(lambda x,y: x+y, map(lambda x : chr(x ^ key), map(lambda c: ord(c) ^ key, list(s))), ""))