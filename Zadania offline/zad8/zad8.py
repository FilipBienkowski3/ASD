#Filip Bieńkowski
#Algorytm polega na pobraniu plamy z pola 0,0 (pobór plamy odbywa sie za pomoscą DFS który traktuje sąsiednie pola jako połaczenia klasycznego grafu).
#Następnie przechodzimy na kolejne pola na ktore jestesmy w stanie dojść z tą ilością paliwa, na kazdym polu gdzie nie ma 0 pobieramy cała plame i dodajemy do kolejki prioryttowej.
#Wartość 0 w kolejce priorytetowej jest pomnożona razy -1 aby ustawiała najwieksze plamy na poczatek kolejki.
#Przechodzimy na pole o najwiekszym zasobie paliwa dodająć znajdujące się tam paliwo oraz odejmująć droge do tej plamy.
#Gdy najlepsza opcja będzie indeks wczesniej to dodaje paliwo znajdujące się na wcześneijszym indeksie.
#Zwiększamy liczbe zatrzymań o 1.
#Algorytm kończy działanie gdy bedzię w stanie dojść na pole m-1 albo None gdy braknie paliwa.
#Złożoność to O(n*m)
from zad8testy import runtests
from queue import PriorityQueue

def DFSmatrix(T, x, y):
    startx=x
    starty=y
    n = len(T)
    m = len(T[0])
    add = 0

    def DFSvisitmatrix(T, x1, y1):
        nonlocal add
        for (x2, y2) in [(x1 - 1, y1), (x1, y1 + 1), (x1 + 1, y1), (x1, y1 - 1)]:
            if 0 <= x2 < n and 0 <= y2 < m:
                if T[x2][y2] != 0:
                    add += T[x2][y2]
                    T[x2][y2]=0
                    DFSvisitmatrix(T, x2, y2)

    if 0 <= x < n and 0 <= y < m:
        if T[x][y] != 0:
            add += T[x][y]
            T[x][y]=0
            DFSvisitmatrix(T, x, y)

    if add == 0:
        return T[x][y]
    else:
        T[startx][starty]=add
        return add

def plan(T):
    fuel = 0
    m = len(T[0])
    q = PriorityQueue()
    q.put((-1*DFSmatrix(T, 0, 0), 0))
    el = q.get()
    fuel = -1 * el[0]
    i = el[1]
    result = 1
    T[0][0]=0
    while (i<=m-1):
        for stop in range(1, fuel+1):
            if i +stop<=m-1:
                if i +stop==m-1:
                    return result
                if T[0][stop+i]!=0:
                    add = DFSmatrix(T,0,stop+i)
                    q.put((-1 * add, stop + i))
                    T[0][stop+i] = 0
            else:
                break
        el = q.get()
        if el[1]<i:
            fuel=fuel +(-1*el[0])
        else:
            fuel =fuel-(el[1]-i)+(-1 * el[0])
            i = el[1]
        result += 1
        if fuel < 0 and i != m - 1:
            return None
    return result
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )


