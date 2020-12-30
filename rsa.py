from math import gcd
from decimal import Decimal 

p = int(input('Enter a prime number = ')) 
q = int(input('Enter another prime number = ')) 
M = int(input('Enter the message = ')) 

n = p*q 
print('the value of n = ',str(n))

phi = (p-1)*(q-1)
print('the value of phi = ',str(phi)) 

for e in range(2,phi): 
	if gcd(e,phi)== 1: 
		break
print('the value of public key = ',str(e))

for i in range(1,10): 
	x = 1 + i*phi 
	if x % e == 0: 
		d = int(x/e) 
		break
print('the value of private key = ',str(d))


ct = pow(M,e) % n
print('the value of cipher text = ',str(ct))

dt = pow(ct,d) % n
print('the value of plain text = ',str(dt)) 





