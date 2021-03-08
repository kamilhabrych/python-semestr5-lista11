import random

def losowa(a, b, n):
    if n > 0:
        A = [[random.randint(1,n) for i in range(a)] for j in range(b)]
        return A
    else: 
        print('Wartość n musi być większa od 0')

def dodaj(A, B):
    C = []
    if (len(A) == len(B)) and (len(A[0]) == len(B[0])):
        for i in range(len(A)):
            C.append([])
            for j in range(len(A[0])):
                C[-1].append(A[i][j] + B[i][j])
    return C

A = losowa(2, 3, 10)
B = losowa(2, 3, 10)

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

C = dodaj(A,B)
print(C)
print()
for x in C: 
    print(x)