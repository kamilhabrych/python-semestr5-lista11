# Lista 11 - Języki programowania wysokiego poziomu

**Python (11) - Tabele wielowymiarowe, macierze**

(1) W pythonie dopuszczalne są listy zawierające listy, np.:
A=[[1,2],[3,4]]
stworzy listę skłdającą się z 2 list 2-elementowych. Poszczególne elementy
uzyskamy składnią A[i][j]. W ten sposób uzyskaliśmy tablicę 2 na 2. Stwórz
takie A, wyświetl je za pomocą print oraz jako macierz (wiersz po wierszu).

(2) Aby stworzyć większe tabele wygodnie jest stosować składnię typu:
A=[[0 for i in range(5)] for j in range(6)]
co stworzy macierz 6 (wierszy) na 5 (kolumn) wypełnioną zerami. Następnie można zmieniać wartości A (bez stworzenia A nie dałoby się stosować
przykładowo A[3][4]=7).
Napisz funkcję zera(a, b) która zwraca macierz rozmiaru a na b wypełnioną
zerami oraz funkcję id(n) która zwraca macierz jednostkową n na n (jedynki
na przekątnej, poza przekątną zera). Wreszczie napisz funkcję wyswietl(A)
która wyświetla macierz A wiersz po wierszu (dla rozmiaru macierzy przyda
się funkcja len). Przetestuj czy wszystkie funkcje działają.

(3) Napisz funkcję losowa(a, b, n) która zwraca macierz rozmiaru a na b
wypełnioną losowymi liczbami naturalnymi z zakresu od 1 do n. Napisz
funkcję dodaj(A, B) która zwraca sumę macierzy A i B (i zwraca pustą listę
jeśli wymiary A i B nie są takie same).
Przetestuj tworząc macierze A i B rozmiaru 2 na 3 wypełnione losowymi
liczbami z zakresu od 1 do 10. Wyświetl A, B dodaj je i wyświetl ich sumę.

(4) Do zadania (3) dopisz funkcję pomnoz(A, B) która zwraca iloczyn macierzy A i B (lub pustą listę jeśli wymiary A i B nie pozwalają na przemnożenie
macierzy). Przetestuj na dwóch macierzach 2 na 2.

(5) Napisz funkcje dla operacji elementarnych na wierszach macierzy:
zamW(A, i, j) zwraca macierz uzyskaną z A po zamianie i-tego i j-tego wiersza.
przemW(A, i, k) zwraca macierz gdzie i-ty wiersz A jest przemnożony przez
k.
dodajW(A, i, j, k) zwraca macierz gdzie do i-tego wiersza dodany jest k razy
j-ty wiersz.
Przetestuj te funkcje na przykładowej macierzy.

(6) Napisz funkcję det(A) zwracającą wyznacznik macierzy A w sposób rekurencyjny. Przetestuj szybkość dla coraz większych macierzy kwadratowych
tworzonych np. za pomocą losowa z (3).
