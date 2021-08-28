"""
edu goorm io

a : 0
b : 0
c : 0
d : 1
e : 1
f : 0
g : 1
h : 0
i : 1
j : 0
k : 0
l : 0
m : 1
n : 0
o : 3
p : 0
q : 0
r : 1
s : 0
t : 0
u : 1
v : 0
w : 0
x : 0
y : 0
z : 0

"""
import sys

input = lambda: sys.stdin.readline().rstrip()


alphabets = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
}

sentence = list(input().lower().replace(" ", ""))

for s in sentence:
    alphabets[s] += 1

for k, v in alphabets.items():
    print(k + " : " + str(v))
