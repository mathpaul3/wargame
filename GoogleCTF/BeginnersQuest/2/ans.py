A = 0
B = 1
C = 1
D = 0
E = 0
F = 1
G = 0
H = 0
I = 1
J = 1

print((not (A or not B) and not((not C or D) or (E or not F))) and ((not (G or H) and (H ^ I)) and (I and J)))
