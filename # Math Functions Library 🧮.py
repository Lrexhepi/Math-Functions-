# Math Functions Library 🧮

"""
Dieses Projekt ist eine Sammlung mathematischer Funktionen in reinem Python 
(ohne externe Libraries). Ziel ist es, grundlegende Konzepte wie Fakultät, 
Skalarprodukt, Integrale und Ableitungen zu üben und gleichzeitig sauberen 
Code und Teststrukturen aufzubauen.
"""
"""
## Features
- Fakultät (rekursiv & iterativ)
- Skalarprodukt, Vektoraddition, Skalarmultiplikation
- Numerische Ableitung & Integral (Rechteck-/Trapezregel)
- Checks für Axiome des Skalarprodukts
"""

EPS = 1e-12
def fak(n: int) -> int: 
    "Berechnet n! rekursiv"
    assert(n>0)

    if n == 0: 
        return 1
    if n == 1: 
        return 1
    
    else: 
        return n * fak(n-1)
    
def potenz(a: int , b: int) -> int:
    """"
    Rechnet die Potenz von a, rekursiv   

    Args: 
        a (int): Basis. 
        b (int): Exponent. 

    Returns: 
        int: a^b, Exponent von a
    """

    if b == 0: return 0

    return a * potenz(a,b - 1)
    

def abs(n: int) -> int: 
    """
    Berechnet den Betrag einer Zahl 

    Args:
        n int: Eingabezahl. 

    Returns: 
        Int: |n|, der Betrag von n 
    """

    if n < 0: 
        n *= -1
        return n
    
    else: 
        return n
    
def gcd(a: int, b: int) -> int: 
    """Gröster gemeinsamer Teiler (Euklidischer Alghorithmus) """
    a, b  = abs(a), abs(b)

    while b: 
        a, b = a, a % b
    return  a

def kgV(a: int, b: int) -> int: 
    """Kleinstes gemeinsames Vielfaches"""
    return abs(a*b) // gcd(a,b)


def fib(n : int) -> int: 
    """ Rechnet die n-te Fibonacci Zahl aus, rekursiv"""
    if n == 0: 
        return 0 
    if n == 1: 
        return 1
    
    else: 
        return fib(n-1) +  fib(n-2) 
    

def is_prime(n: int): 
    if  n <= 1: 
        return False
    
    if n == 2: 
        return True
    
    i = 2

    while i * i <= n: 
        if n % i == 0: 
            return False
    i += 1 
    return False 


def sum_of_a_row(n : int) -> int:
    """Summe einer Reihe"""
    sum = 0
    for i in range(n, 1, -1): 
        sum += i
    
    return sum

def min_max(lst) -> tuple[int, int]: 
    """ Minimum und das Maximum einer Liste"""
    minimum = lst[0]
    maximum = lst[0]


    for i in lst: 
        if (i < minimum): 
            minimum = i 
        if (i > maximum): 
            maximum = i 
    
    return(minimum, maximum)


def derivative(f, x, h): 
    """Rechnet den Wert einer Ableitung einer Funktion hab

        Args: 
            f: Funktion f(x)
            x: Auswertungstelle
            h: kleiner Schritt (h>0)

        Retuns :
            float: Approximation von f'(x)
    """
    assert h > 0
    y = f(x+h) - f(x-h)/ (2*h)
    return y

def integral_left_rectangle(f, a, b, n):
    """
    Numerisches Integral mit linker Rechteckregel.
    Args:
        f: Funktion f(x)
        a, b: Integrationsgrenzen (a < b)
        n: Anzahl Teilintervalle (n >= 1)
    Returns:
        float: Approximation des Integrals
    """
    assert n >= 1, "n muss >= 1 sein."
    assert b > a, "Es muss b > a gelten."
    h = (b - a) / n
    s = 0.0
    for i in range(n):          
        x_i = a + i * h
        s += f(x_i)
    return s * h

def integral_trapezoid(f, a, b, n):
    """
    Numerisches Integral mit Trapezregel (genauer als linke Rechteckregel).
    Returns:
        float: Approximation des Integrals
    """
    assert n >= 1, "n muss >= 1 sein."
    assert b > a, "Es muss b > a gelten."
    h = (b - a) / n
    # f(a) und f(b) einmal, innere Punkte doppelt
    s = f(a) + f(b)
    for i in range(1, n):       # i = 1 ... n-1 (innere Stützstellen)
        x_i = a + i * h
        s += 2 * f(x_i)
    return 0.5 * h * s

def scalar(list1, list2) -> float: 
    assert len(list1) == len(list2)
    summe = 0
    for i in range(0, len(list1)): 
        summe += list1[i] * list2[i]
    
    return summe

def isscalar(list1, list2, summe) ->  bool: 
    assert(list1 == list2)
    checker = 0
    #Symmetrie 
    sym =  scalar(list1, list2) == scalar(list2, list1)
    #Positivität: 
    pos = scalar(list1, list1) >= 0 
    if abs(scalar(list1, list1)) <= EPS: 
        pos = is_zero(list1)

    return pos and sym 

def vektoraddition(list1, list2) -> list: 
    assert(len(list1)== len(list2))
    list3 = []
    for i in range(0, len(list1)): 
        list3.append(list1[i]+ list2[i])
    
    return list3 

def scalar_mult(alpha: float, v: list[float]) -> list[float]:
    return [alpha * x for x in v]

def is_zero(v: list[float]) -> bool: 

    for x in v: 
        if abs(x) > EPS: 
            return False 
    return True 


def check_scalar_axioms(alpha, u, v, w) -> bool: 
    lhs = scalar(vektoraddition(scalar_mult(alpha, u), v), w)
    rhs = alpha * scalar(u, w) + scalar(v, w)
    return abs(lhs - rhs) <= EPS

    

    


