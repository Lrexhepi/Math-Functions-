#Lin Alg 

EPS = 1e-12

def matrixmultiplikation(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    # Ergebnis-Matrix mit 0 initialisieren
    AB = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # klassische Dreifach-Schleife
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                AB[i][j] += A[i][k] * B[k][j]

    return AB


def matrixaddition(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    # Ergebnis-Matrix mit 0 initialisieren
    assert len(A) == len(B)
    assert len(A[0]) == len(B[0])

    AB = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # klassische Dreifach-Schleife
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                AB[i][j] += A[i][k] + B[k][j]

    return AB

def norm(v: list[float]) -> float: 
    sume = 0
    for i in v: 
        sume += i * i
    
    return sume ** 0.5

def einheitsvektor(v: list[float]) -> list[float]: 
    n = norm(v)
    assert n > 0
    v = [i/n for i in v ]

def orthogonal(v: list[float], u: list[float]) -> bool: 
    assert len(v) == len(u)
    dp = 0.0

    for i in range(len(v)): 
        dp += v[i] * u[i]
    
    return abs(dp) <= EPS



def transpose(A: list[list[float]]) -> list[list[float]]:
    """Transponiert eine rechteckige Matrix A (m x n) zu A^T (n x m)."""
    assert len(A) > 0
    n_cols = len(A[0])
    # Rechteckigkeit prüfen
    for row in A:
        assert len(row) == n_cols, "Matrix muss rechteckig sein."

    m = len(A)      # Zeilen
    n = n_cols      # Spalten

    # Ergebnis (n x m) vorallozieren
    AT = [[0.0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            AT[j][i] = A[i][j]
    return AT

def determinante2x2(A: list[list[float]]) -> float: 
    assert len(A) == 2 and len(A[0]) == 2 and len(A[1]) == 2
    determinante =  A[0][0]* A[1][1] - A[0][1] * A[1][0]

    return determinante

""""
def determinante3x3(A: list[list[float]]) -> float:
    lst = []
    counter = 0 
    for i in range(0, len(A)): 
        assert len(A) == len(A[i])

    n = len(A)
    if n == 1: return A[0][0]
    if n == 2: return A[0][0]*A[1][1] - A[0][1]*A[1][0]

    for i in range(0, len(A)): 
"""        

def littleone(A: list[list[float]]) -> float: 
    littleone = A[0][0]

    for i in A: 
        for j in i: 
            if littleone > j: 
                littleone = j
    
    return littleone


