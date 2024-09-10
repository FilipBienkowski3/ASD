#Filip Bieńkowski Szacowana złożoność obliczeniowa to O(n logn). Wykonanie zadania sprowadza się do posortowania wąwozu i brania śniegu od największej ilości zaczynając. Bieżemy śnieg (uwzględniając topnienie) do momentu spotkania 0 albo liczby ujemnej.
from zad2testy import runtests
def quicksort(A,p,r):
    while p<r:
        q=partition(A,p,r)
        if (q-p)<(r-q):
            quicksort(A, p, q-1)
            p=q+1
        else:
            quicksort(A,q+1,r)
            r=q-1
def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def snow( S ):
    # tu prosze wpisac wlasna implementacje
    n = len(S)
    minus = 0
    sum = 0
    quicksort(S,0,n-1)
    for i in range(n - 1, 0, -1):
        if S[i] - minus < 0:
            break
        sum += S[i] - minus
        minus += 1
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
