def stacje_1(L,S):
  N=len(S)
  poz=0
  tankowanie=0
  while poz<N:
    i=poz
    while i>=poz - L and S[i] is None:
      i-=1
    tankowanie +=1
    poz+=L-(poz-i)



def stacje_2(L,S):
  poz=0
  N=len(S)
  paliwo=0
  koszt =0
  while poz<N:
    najtansza_stacja=sorted([x for x in enumerate(S)[poz:poz+L]if x[1]],key=lambda x: x[1])[0]
    if najtansza_stacja[0]==poz:
      brakuje = min(L-paliwo,N-poz-paliwo)
      koszt+=brakuje * najtansza_stacja[1]
      paliwo+=brakuje
      poz+=min(L,N-poz)
    else:
      odl=najtansza_stacja[0]-poz
      ile_dotankowac=max(0,odl-paliwo)
      paliwo+=ile_dotankowac
      koszt+= ile_dotankowac*S[poz]
      poz+=odl