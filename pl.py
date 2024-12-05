def add(m,n):
    return m+n

def sub(m,n):
    return m-n

def mul(m,n):
    return m*n

def quo(m,n):
    return m/n

def rem(m,n):
    return m%n

def pow(m,n):
    return m**n

def quo_int(m,n):
    return m//n

def euclid_algorithm(m,n):
    if m < n:
        (m,n) = (n,m)
    if (m%n)==0:
        return n
    else:
        return euclid_algorithm(n,m%n)