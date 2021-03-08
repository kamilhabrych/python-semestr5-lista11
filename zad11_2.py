def zera(a,b):
    A = [[0 for i in range(a)] for j in range(b)]
    return A

def id(n):
    A = [[0 for i in range(n)] for j in range(n)]
    for i in range(n): 
        for j in range(n):
            if i==j or i == n-1-j: 
                A[i][j] = 1    
    return A

def wyswietl(l):
    for x in l: 
        print(x)

A1 = zera(7,5)
A2 = id(5)

wyswietl(A1)

print()

wyswietl(A2)