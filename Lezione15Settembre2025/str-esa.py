n = "009a0a59eec8fea61d00fbc95ba90c" +\
    "5c1569c5148f449109d63d1fac0b05" +\
    "cb7150a83eaa721687f4967856c383" +\
    "6506a83458345fe84f5fa66b55320c" +\
    "ab53ee820ab11a062ecd8c51a74c6a" +\
    "9b2a05e3596a5e782411894647d580" +\
    "3e68ed7bb7e1adee9229e5144ed5e8" +\
    "e81ae8b67dc4ded1b507328ddaedd4" +\
    "5bfcb5786eccdbc725fe418923ec06" +\
    "3578b9c99856b69767dcf18d20aa0e" +\
    "f0e62f9db0b5681467712575eea133" +\
    "635ec7c76b2caedfac969d3901ba2e" +\
    "1415a5b7a06e6c95475d0a773638bd" +\
    "1d1fbcf5ff9bc085b29b34be7e19ab" +\
    "004ca98c908b9477ca9eb878cd7bd4" +\
    "3fde26bb6b972236e0183a84f870d5" +\
    "68b6a03857f563fb6916b3f81577db" +\
    "1ca5"

decimale = int(n, 16)

M = "Viva il calcio"
Mi=int(M.encode("utf-8").hex(), 16)

e = 3

C = pow(Mi,e,decimale)
print(C)

d = "19ac645276d51baf8029f6e49c2cba" +\
    "0391a0d8c28b6d81a3b4da9cac80f7" +\
    "3d8d715fc71303c1536e6963cb4090" +\
    "d6715e0eb36551628ff111e3885771" +\
    "e3526b01c82f0107ccecb8468cbc6f" +\
    "31aba5e43c65140602ec36614e400a" +\
    "66d23f495047a7c306fb836278fc26" +\
    "af26c914f62522f3813317a47cf8b9" +\
    "ff7394127779f68612a77db452664d" +\
    "fcc7a0462c8090289cbcac7bffd3ec" +\
    "a2bd6dcc9b8a394b5b9e9f8df8dbd0" +\
    "853c4f92d85aaf87023f63f4fadcb1" +\
    "5e065c25306c16d900b0a23e1bf7fd" +\
    "b8c4eb907e7fff2c458179f4ad59c4" +\
    "cb9e0d1710b2da30be3de29cbde43c" +\
    "b88a8b054a93cb9fe11a68012dc5af" +\
    "e3a144c8e19b283804dee14a84c4dc" +\
    "cb"

decimale2 = int(d, 16)
D = pow(C, decimale2, decimale)

decimale = format(D, "x")

testo_decifrato = bytes.fromhex(decimale).decode()
print(f"Testo decifrato: {testo_decifrato}") 