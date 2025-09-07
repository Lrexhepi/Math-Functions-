#Numerik 

EPS = 1e-8
def bissektionsverfahren(f, a, b, EPS) -> tuple:    
    assert f(a) * f(b) < 0

    while abs(b - a) > EPS: 
        m  = (a+b) / 2
        if abs(f(m)) < EPS: 
            return m 
        if f(a) * f(b) < 0: 
            b = m 
        else: 
            a = m 
    return (a+b) / 2







