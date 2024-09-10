# Filip Bieńkowski Złożoność czasowa O(n+nlogn). Algorytm zawiera elementy z quickosrta zrobione iteracyjnie. Polega na wyborze pivota i ustawienu po lewej stronie tablicy wszystkich słow takich samych jak nasz pivot albo po odwroceniu takich samych. Algorytm zlicza ile jest słow po lewej stronie, algorytm wykonuje sie ponownie dla prawej czesci tablicy, funkcja zwraca moc najsilniejszego słowa.
from zad3testy import runtests

def strong_string(T):
    # tu prosze wpisac wlasna implementacje
    maxi = 1
    counter = 0
    n = len(T)
    low = 0
    high = n - 1
    while low < high:
        pivot = T[high]
        i = low - 1
        for j in range(low, high):
            if T[j] == pivot or T[j][::-1] == pivot:
                i = i + 1
                T[i], T[j] = T[j], T[i]
        T[i + 1], T[high] = T[high], T[i + 1]
        pi = i + 1
        maxi = max(maxi, pi + 1 - counter)
        counter += (pi + 1)-counter
        low = pi + 1
    return maxi

# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
