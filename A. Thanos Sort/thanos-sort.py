def FingerSnap(L):
    n = len(L)
    l1 = L[:n//2]
    l2 = L[n//2:]
    return l1, l2
 
 
def Sorted(L):
    if len(L) == 1:
        return True
    for i in range(1, len(L)):
        if int(L[i]) < int(L[i - 1]):
            return False
    return True
 
 
def ThanosSort(L):
    if Sorted(L):
        return L
    else:
        l1, l2 = FingerSnap(L)
    l1 = ThanosSort(l1)
    l2 = ThanosSort(l2)
    if len(l1) >= len(l2):
        return l1
    else:
        return l2
 
 
# main
t = int(input())
ch = str(input())
L = ch.split()
print(len(ThanosSort(L)))