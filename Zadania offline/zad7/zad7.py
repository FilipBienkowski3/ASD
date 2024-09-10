#Filip Bieńkowski
#Algorytm polega na wypełnieniu 3 tablic wartością -1, T jest głowną tablicą z najdłuższymi drogami do danych punktów od poczatkowego.
#Na początku wypełniam pierwszą kolumnę kolejnymi liczbami naturalnymi aż wejścia na pole z #, na dalsze pola nie będziemy w stanie dojść.
#Dla pozostałych kolumn (pętla for o zmiennej j) wywołuję kolejne pętle. Reprezentuje to przejście w prawo. Następnie mamy 2 opcje iść w górę albo w dół.
#Pętla z k to przejście w dół po kolejnych wierszach, do tablicy pomocniczej DOWN wpisuje maksymalną wartość (by jak najbardziej wydłużyć scieżkę) z pól z których da się dojść na to pole (pola z lewej oraz pola nad),dodając 1.
#Pętla z r jest analogiczna do tej z k, reprezentuje ona przejście w góre.
#Na koniec porównuje wartości z 2 tablic pomocniczych, większą wpisuję do ostatecznej tablicy T.
#Jeżeli będzie ścieżka do T[n-1][n-1] funkcja zwróci nadłuższą możliwą, a jeśli nie to zwróci -1.
#złożoność 0(n^2)
from zad7testy import runtests


def maze(L):
    n = len(L)
    T = [[-1] * n for _ in range(n)]
    DOWN = [[-1] * n for _ in range(n)]
    UP = [[-1] * n for _ in range(n)]
    for i in range(n):
        if L[i][0] == '#':
            break
        else:
            T[i][0] = i
    for j in range(1, n):
        for k in range(n):
            if L[k][j] == '#':
                continue
            left = T[k][j - 1]
            if k - 1 >= 0:
                up = DOWN[k - 1][j]
            else:
                up = -1
            if left == -1 and up == -1:
                continue
            DOWN[k][j] = max(left, up) + 1

        for r in range(n - 1, -1, -1):
            if L[r][j] == '#':
                continue
            left = T[r][j - 1]
            if r + 1 <= n - 1:
                down = UP[r + 1][j]
            else:
                down = -1
            if left == -1 and down == -1:
                continue
            UP[r][j] = max(left, down) + 1

        for z in range(n):
            T[z][j] = max(DOWN[z][j], UP[z][j])

    return T[n - 1][n - 1]
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
