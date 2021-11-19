#PRACTICA 1

#EJERCICIO 1

bin(12345)
oct(12345)
hex(12345)

bin(177130)

oct(177130)
hex(177130)

#EJERCICIO 2

a=int("43210",5)
a=2930
b=hex(3EBC)
b=16160
b/a
5.48122866894198

#EJERCICIO 4

from math import gcd

a=1529

b=14038

gcd(a, b)
Out[20]: 1

c=int("11111",2)

d=int("111111",2)

gcd(c,d)
Out[25]: 1


#PRACTICA 2


#EJERCICIO 3

from sympy import factorint

81
Out[2]: 81

factorint(39)
Out[3]: {3: 1, 13: 1}

factorint(81)
Out[4]: {3: 4}

factorint(88)
Out[5]: {2: 3, 11: 1}

factorint(101)
Out[6]: {101: 1}

factorint(126)
Out[7]: {2: 1, 3: 2, 7: 1}

factorint(143)
Out[8]: {11: 1, 13: 1}

factorint(289)
Out[9]: {17: 2}

factorint(512)
Out[10]: {2: 9}

factorint(729)
Out[11]: {3: 6}
factorint(899)
Out[12]: {29: 1, 31: 1}

factorint(1001)
Out[13]: {7: 1, 11: 1, 13: 1}

factorint(909090)
Out[14]: {2: 1, 3: 3, 5: 1, 7: 1, 13: 1, 37: 1}
 
factorint(3628800)
Out[26]: {2: 8, 3: 4, 5: 2, 7: 1}

#EJERCICIO 5

from math import gcd

a=3454

b=4666

gcd(a,b)
Out[42]: 2

c=9999

d=11111

gcd(c,d)
Out[45]: 1

#EJERCICIO 8

from sympy import totient

totient(39)
Out[47]: 24

totient(81)
Out[48]: 54

totient(88)
Out[49]: 40

totient(101)
Out[50]: 100

totient(126)
Out[51]: 36

totient(143)
Out[52]: 120

totient(289)
Out[53]: 272

totient(512)
Out[54]: 256

totient(729)
Out[55]: 486

totient(899)
Out[56]: 840

totient(1001)
Out[57]: 720

totient(1111)
Out[58]: 1000

totient(909090)
Out[59]: 186624

totient(3628800)
Out[60]: 829440

#EJERCICIO 10

from sympy import nextprime,randprime, isprime

isprime(2047)
Out[6]: False

#EJERCICIO 12

from	sympy.ntheory.modular	import	crt

crt([2,3,5,11],[1,2,3,4])
Out[12]: (323, 330)

#EJERCICIO 13

from	sympy.ntheory.modular	import	crt

crt([17,16,15],[3,10,0])
Out[16]: (3930, 4080)

#EJECICIO 14


#Hallar dos numeros primos distintos, uno de dos cifra p
# y otro de tres cifras q, hallar n=p*q y la funcion de Euler
#Phin(n), hallar un numero aleatorio e estrictamente entre 1 
# y Phin(n), y hallar el inverso d de e modulo Phin(n).
	
from sympy import nextprime,randprime,isprime

p=nextprime(50)
p=53

q=nextprime(120)
q=127

n=p*q
n=6731

from sympy import totient

totient(n)
Out[36]: 6552

from random import randint

e=randint(1,6552)
e=107
 
 
def modInv(n,e):
    x,X=0, 1
    y,Y=1, 0
    while(e!=0):
        E=e
        d=n//e
        n,e=e,n% b
        x,X=X-d*x,x
        y,Y=Y-q*y,y
    return([E,X,Y])

def modInverse(n,e):
    d=egcd(n,e)
    return d[1]% m

#Hallar un número entero aleatorio de 4 
#cifras y factorizalo

from random import randint
 
a=randint(1000,9999)
a=8765

from sympy import factorint

factorint(a)
Out[16]: {5: 1, 1753: 1}

 
%history -n -o -f practica_2 1-200
 
 
 





