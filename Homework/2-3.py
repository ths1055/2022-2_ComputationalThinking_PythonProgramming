print('=================================')
print('Decimal   Bit  Octal  Hexadecimal')
print('---------------------------------')
for i in range(256):
    print("{0:6d} {0:08b} {0:#05o} {0:#04x}".format(i))
print('---------------------------------')