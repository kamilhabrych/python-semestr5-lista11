import random

def losowa(a,n):
    if n>0:
        A = [[random.randint(1,n) for i in range(a)] for j in range(a)]
        return A
    else:
        print('Wartość n musi być większa od 0')

def det(A):
    indeksy = list(range(len(A)))
    wynik = 0
    if len(A) == 2 and len(A[0]) == 2:
        return A[0][0]*A[1][1]-A[1][0]*A[0][1]
    for i in indeksy:
        kopia_A = list.copy(A)
        kopia_A = kopia_A[1:]
        for j in range(len(kopia_A)):
            kopia_A[j]=kopia_A[j][0:i]+kopia_A[j][i+1:]
        znak=(-1)**(i%2)
        det2 = det(kopia_A)
        wynik += znak*A[0][i]*det2
    return wynik

A = losowa(5,8)

print(A)
print()
for x in A: 
    print(x)

wynik = det(A)
print()
print('det(A) = {0}'.format(wynik))