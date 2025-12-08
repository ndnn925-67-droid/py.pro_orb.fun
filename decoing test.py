
#new test
a = "%"
b = "E"
c = "7"
d = "r"
e = "O"
f = "4"
g = ")"
h = "u"
i = "W"
j = "g"
k = "P"
l = "$"
m = "y"
n = "H"
o = "9"
p = "X"
q = "a"
r = "I"
s = "1"
t = "z"
u = "f"
v = "8"
w = "Q"
x = "@"
y = "!"
z = "K"

A = "T"
B = "c"
C = "S"
D = "^"
E = "V"
F = "m"
G = "5"
H = "J"
I = "*"
J = "D"
K = "L"
L = "b"
M = "0"
N = "6"
O = "#"
P = "k"
Q = "n"
R = "Y"
S = "C"
T = "F"
U = "M"
V = "&"
W = "h"
X = "Z"
Y = "3"
Z = "U"
comma = "+"
dot = "."
backspace = "<"
# ?
qs1="?"

print("Waring! This code only works with letters a-z, A-Z, comma, dot, question mark and space.")
print("Any other characters will result in an error message.")
print("This is running in Beta version, so there may be bugs.")
a1 = input("Enter the sentence to encrypt: ")
for char in a1:
    if char == " ":
        print(backspace, end="")
    elif char == "a":
        print(a, end="")
    elif char == "b":
        print(b, end="")
    elif char == "c":
        print(c, end="")
    elif char == "d":
        print(d, end="")
    elif char == "e":
        print(e, end="")
    elif char == "f":
        print(f, end="")
    elif char == "g":
        print(g, end="")
    elif char == "h":
        print(h, end="")
    elif char == "i":
        print(i, end="")
    elif char == "j":
        print(j, end="")
    elif char == "k":
        print(k, end="")
    elif char  == "l":
        print(l, end="")
    elif char == "m":
        print(m, end="")
    elif char == "n":
        print(n, end="")
    elif char == "o":
        print(o, end="")
    elif char == "p":
        print(p, end="")
    elif char == "q":
        print(q, end="")
    elif char == "r":
        print(r, end="")
    elif char == "s":
        print(s, end="")
    elif char == "t":
        print(t, end="")
    elif char == "u":
        print(u, end="")
    elif char == "v":
        print(v, end="")
    elif char == "w":
        print(w, end="")
    elif char == "x":
        print(x, end="")
    elif char == "y":
        print(y, end="")
    elif char == "z":
        print(z, end="")
    elif char == ",":
        print(comma, end="")
    elif char == ".":
        print(dot, end="")
    elif char == "?":
        print(qs1, end="")
    elif char == "A":
        print(A, end="")
    elif char == "B":
        print(B, end="")
    elif char == "C":
        print(C, end="")
    elif char == "D":
        print(D, end="")
    elif char == "E":
        print(E, end="")
    elif char == "F":
        print(F, end="")
    elif char == "G":
        print(G, end="")
    elif char == "H":
        print(H, end="")
    elif char == "I":
        print(I, end="")
    elif char == "J":
        print(J, end="")
    elif char == "K":
        print(K, end="")
    elif char == "L":
        print(L, end="")
    elif char == "M":
        print(M, end="")
    elif char == "N":
        print(N, end="")
    elif char == "O":
        print(O, end="")
    elif char == "P":
        print(P, end="")
    elif char == "Q":
        print(Q, end="")
    elif char == "R":
        print(R, end="")
    elif char == "S":
        print(S, end="")
    elif char == "T":
        print(T, end="")
    elif char == "U":  
        print(U, end="")
    elif char == "V":
        print(V, end="")
    elif char == "W":
        print(W, end="")
    elif char == "X":
        print(X, end="")
    elif char == "Y":
        print(Y, end="")
    elif char == "Z":
        print(Z, end="")
    else:
        print("")
        print("Invalid character found.")