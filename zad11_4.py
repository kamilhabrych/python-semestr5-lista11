import random

def losowa(a,b,n):
    if n > 0:
        A = [[random.randint(1,n) for i in range(a)] for j in range(b)]
        return A
    else:
        print('Wartość n musi być większa od 0')

def pomnoz(A,B):
    if len(A[0]) == len(B):
        C = [[0 for i in range(len(A[0]))] for j in range(len(B))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j] 
    else: 
        C = [] 
    return C

A = losowa(2,2,10)
B = losowa(2,2,10)

print('A:')
print(A)
print()
for x in A: 
    print(x)

print()
print('B:')
print(B)
print()
for x in B: 
    print(x)

print()
print('C = A + B:')

C = pomnoz(A,B)
print(C)
print()
for x in C: 
    print(x)