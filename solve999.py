import r2pipe
import binascii
import sys

for i in range(1, 1000):
   b = r2pipe.open('{0:03}'.format(i) + '.c.out')
   # print(f'B: {b}')
   disass = b.cmd('aaa; s main; pdd')
   # print(f'DISASS: {disass}')
   field = disass.split("eax = *(obj.")[1][0]
   byte = disass.split(f'*(obj.{field}) = ')[-1][2:4]
   print(binascii.unhexlify(byte).decode('ascii'))