#PRACTICA 3

#EJERCICIO 13 

P= ((((p & q) & r) | ((p & r) & ~r)) | ~q) >> s

P
Out[38]: Implies(~q | (p & q & r) | (p & r & ~r), s)

from sympy.logic import simplify_logic

from sympy.abc import p, q, r, s

P= ((((p & q) & r) | ((p & r) & ~r)) | ~q) >> s

P
Out[43]: Implies(~q | (p & q & r) | (p & r & ~r), s)
symply(P)

simplify_logic(P)
Out[45]: s | (q & ~p) | (q & ~r)

#EJERCICIO 32

P= ((p | ~q) & ~r) | ((p | q | r) & (~q | ~r))

P
Out[47]: (~r & (p | ~q)) | ((p | q | r) & (~q | ~r))

simplify_logic(P)
Out[48]: ~q | ~r

Q= (~q | ~r)

satisfiable(Not(Equivalent (P, Q)))
Out[50]: False

#EJERCICIO 33

P= (p | q) & ((q |(r & r)) | ( ~q & (~r | ~s) & (~r | s)))

P
Out[52]: (p | q) & (q | r | (~q & (s | ~r) & (~r | ~s)))

simply_logic(P)

simplify_logic(P)
Out[54]: p | q

#EJERCICIO 18
#a

from sympy.logic import simplify_logic

from sympy.abc import p, q, r, s, t, u

P=(p>>q)

R=(~r|(~t|u))

Q=(q>>(r&s))

S=(p&t)

from	sympy.logic.inference	import	satisfiable
 
satisfiable (P & Q & R & S)
Out[19]: {p: True, q: True, r: True, s: True, t: True, u: True}

satisfiable (P & Q & R & S & ~u)
Out[21]: False

#b
from	sympy.logic.inference	import	satisfiable

from sympy.logic import simplify_logic

from sympy.abc import p, q, r, s, t

P=(~p|~q)>>(r&s)

Q=r>>t

R=~t

satisfiable (P & Q & R)
Out[31]: {p: True, q: True, s: True, t: False, r: False}

satisfiable (P & Q & R & ~p)
Out[33]: False

#c


#EJERCICIO 19

from	sympy.logic.inference	import	satisfiable

from sympy.logic import simplify_logic

from sympy.abc import p, q, r

#A

P=p>>q

satisfiable (p & P & r)
Out[39]: {p: True, q: True, r: True}

Q=((p|q)>>r)

satisfiable(p & P & r & ~Q)
Out[42]: False

#B

P=((p&q)>>r)

Q=~q

R=(p>>~r)

satisfiable(P & Q & R)
Out[47]: {r: False, q: False, p: False}

S=(~p|~q)

satisfiable(P & Q & R & ~S)
Out[50]: False

#C

P=(p|(q|r))

Q=~q

R=(p|r)

satisfiable(P & Q)
Out[54]: {p: True, r: True, q: False}

satisfiable( P & Q & ~R)
Out[56]: False

#EJERCICIO 20

from	sympy.logic.inference	import	satisfiable

from sympy.logic import simplify_logic

from sympy.abc import p, q, r, s

P=p&q

satisfiable(P & ~p)
Out[61]: False

Q=(p|q)

satisfiable(p & ~Q)
Out[63]: False

P=p|q

Q=~p

satisfiable(P & Q & ~q)
Out[66]: False

P=p>>q

Q=r>>s

R=p|r

S=q|s

satisfiable(P & Q & R & ~S)
Out[72]: False

P=p>>q

Q=r>>s

R=~q|~s

S=~p|~r

satisfiable(P & Q & R & ~S)
Out[77]: False

#EJERCICIO 21

P=p>>q

Q=q>>r

S=p>>r

satisfiable(P & Q & S)
Out[91]: {r: True, p: False, q: False}

satisfiable(P & Q & ~S)
Out[93]: False

P= p>>q

p
Out[95]: p

satisfiable(P & p)
Out[96]: {p: True, q: True}

satisfiable(P & p & ~q)
Out[97]: False

P=p>>q

Q=~q

satisfiable(P & Q )
Out[100]: {q: False, p: False}

satisfiable(P & Q & ~p)
Out[101]: {q: False, p: False}

P=p>>r

Q=q>>r

S=(p|q)>>r

satisfiable(P & Q)
Out[105]: {r: True, q: False, p: False}

satisfiable(P & Q & ~S)
Out[107]: False

#EJERCICIO 23

 P=p>>(q>>r)

Q=(p&~s)

R=q|s

satisfiable(P & Q & R)
Out[81]: {p: True, q: True, r: True, s: False}

satisfiable(P & Q & R & ~r)
Out[82]: False

#EJERCICIO 24

P=p>>q

Q=(q|r)>>~s

R=p>>(~s)

satisfiable(P & Q & r & ~R)
Out[87]: False

#EJERCICIO 25

P=p&~q

Q=p>>(q>>r)

R=~r

satisfiable(P & Q & ~R)
Out[111]: {p: True, r: True, q: False}

P=(p& q)>>r

Q=~q|r

satisfiable(P & Q & ~P)
Out[117]: False

P=p>>r

Q=p>>(q|~r)

R= ~q|~s

satisfiable(p & P & Q & R & ~s)
Out[121]: {p: True, q: True, r: True, s: False}


















#PRACTICA 4

#EJERCICIO 1

A = set ('123')

B = set ('231')

C = set ('12')

D = set ('12231')

A == B
Out[27]: True

A == C
Out[28]: False

A == D
Out[29]: True

B == C
Out[30]: False

B == D
Out[31]: True

#EJERCICIO 6

U = FiniteSet(*list(Range(1,11)))

A = FiniteSet(1,2,3,4,5)

B = FiniteSet(1,2,4,8)

C = FiniteSet(1,2,3,5,7)

D = FiniteSet(2,4,6,8)

(A|B)&C
Out[61]: {1, 2, 3, 5}

A|(B&C)
Out[62]: {1, 2, 3, 4, 5}

(C.complement(U))&(D.complement(U))
Out[63]: {9, 10}

(C&D).complement(U)
Out[64]: {1, 3, 4, 5, 6, 7, 8, 9, 10}

(A|B)-C
Out[65]: {4, 8}

A|(B-C)
Out[66]: {1, 2, 3, 4, 5, 8}

(B-C)-D
Out[67]: EmptySet()

B-(C-D)
Out[68]: {2, 4, 8}

(A|B)-(C&D)
Out[69]: {1, 3, 4, 5, 8}

#EJERCICIO 7

U = FiniteSet(S.Reals)

A = Interval(0,3)

B = Interval(2,7,False,True)

A&B
Out[73]: Interval(2, 3)

A|B
Out[74]: Interval.Ropen(0, 7)

n [77]: A.complement(U)
Out[77]: {S.Reals} \ Interval(0, 3)

A^B
Out[78]: Union(Interval.Ropen(0, 2), Interval.open(3, 7))

A-B
Out[79]: Interval.Ropen(0, 2)

B-A
Out[80]: Interval.open(3, 7)
‌