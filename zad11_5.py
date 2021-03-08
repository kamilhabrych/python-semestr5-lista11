import random

def losowa(a,b,n):
    if n > 0:
        A = [[random.randint(1,n) for i in range(a)] for j in range(b)]
        return A
    else:
        print('Wartość n musi być większa od 0')

def zamW(A,i,j):
    if (i > 0 and i <= len(A)) and (j > 0 and j <= len(A)):
        C = A.copy()
        C[i-1] = A[j-1]
        C[j-1] = A[i-1]
    else: 
        C = [] 
    return C

def przemW(A,i,k):
    if (i > 0 and i <= len(A)):
        C = A.copy()
        C[i-1] = [element * k for element in C[i-1]]
    else: 
        C = []
    return C

def dodajW(A,i,j,k):
    if (i > 0 and i <= len(A)) and (j > 0 and j <= len(A)):
        C = A.copy()
        C[i-1] = [C[i-1][z] + (C[j-1][z] * k) for z in range(len(C[i-1]))]
    else: 
        C = []
    return C

A = losowa(2,3,5)
C1 = zamW(A,1,3)
C2 = przemW(A,1,2)
C3 = dodajW(A,1,3,4)

print('A:')
print(A)
print()
for x in A: 
    print(x)
    
print()
print('zamW():')
print(C1)
print()
for x in C1: 
    print(x)

print()
print('przemW():')
print(C2)
print()
for x in C2: 
    print(x)

print()
print('dodajW():')
print(C3)
print()
for x in C3: 
    print(x)