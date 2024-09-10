# Filip Bieńkowski
# Szacowana złożoność obliczeniowa to O(n).
# Algorytm polega na przejściu po kolejnych literach danego słowa, algorytm dla każdej litery porównuje ze sobą jej dwóch sąsiadów, jeżeli są takie same to znaczy, że znaleźliśmy środek palindromu. Następnie sprawdzamy jak długi jest nasz znaleziony palindrom.
from zad1testy import runtests

def ceasar( s ):
  # tu prosze wpisac wlasna implementacje
  n=len(s)
  maxi=1
  for i in range(n-1):
    counter=0
    if i+1<=n and i-1>=0:
      if s[i+1]==s[i-1]:
        q=i-1
        p=i+1
        while s[q]==s[p]:
            counter+=1
            if p!=n-1 and q!=0:
              p+=1
              q-=1
            else:
              break
        wartosc=counter*2+1
        if wartosc%2!=0:
          maxi=max(maxi,wartosc)
  return maxi

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
