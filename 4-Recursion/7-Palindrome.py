def pld(n,k=0):
    
    if n[k] != n[len(n)-k-1]:
        return False
    elif k == len(n)//2:
        return True
    return pld(n,k+1)

print(pld("level"))