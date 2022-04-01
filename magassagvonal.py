
A = None
B = None
P = []
Q = []
R = []

P.append(int(input("P pont első koordinátája: ")))
P.append(int(input("P pont második koordinátája: ")))
Q.append(int(input("Q pont első koordinátája: ")))
Q.append(int(input("Q pont második koordinátája: ")))
R.append(int(input("R pont első koordinátája: ")))
R.append(int(input("R pont második koordinátája: ")))


def egyenletszamitas(x0, y0, A, B, p0):
    print(f"\nA(z) {p0} pontból kiinduló magaságvonal egyenlete:")
    print(f"{A}x + {B}y = {A*x0 + B*y0}")
    input()


valasztottPont = str(input("\nMelyik pontból induljon a magasságvonal?\nP, Q, R: "))
if valasztottPont == "p" or valasztottPont == "P":
    x0 = P[0]
    y0 = P[1]
    A = R[0] - Q[0]
    B = R[1] - Q[1]
    egyenletszamitas(x0, y0, A, B, "P")
elif valasztottPont == "q" or valasztottPont == "Q":
    x0 = Q[0]
    y0 = Q[1]
    A = R[0] - P[0]
    B = R[1] - P[1]
    egyenletszamitas(x0, y0, A, B, "Q")
elif valasztottPont == "r" or valasztottPont == "R":
    x0 = R[0]
    y0 = R[1]
    A = P[0] - Q[0]
    B = P[1] - Q[1]
    egyenletszamitas(x0, y0, A, B, "R")
else:
    print("Érvénytelen érték")

