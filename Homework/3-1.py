x, y=map(str,input('input two hexadecimal numbers (예: 0xA3 0x3A) : ').split())
x=int(x,16);y=int(y,16)
print('a = {0:#x} = {0:#010b}'.format(x))
print('b = {0:#x} = {0:#010b}'.format(y))
print("a & b = {0:#x} = {0:#010b}".format(x&y))
print("a | b = {0:#x} = {0:#010b}".format(x|y))
print("a ^ b = {0:#x} = {0:#010b}".format(x^y))