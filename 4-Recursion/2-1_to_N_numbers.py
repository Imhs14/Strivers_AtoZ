"""def n_nums(n,k):
    if k < 0:
        return
    print(n-k)
    n_nums(n,k-1)
n_nums(5,4)"""

def printnumbsers(n,cur = 1):
    if cur > n:
        return
    print(cur)
    printnumbsers(n,cur+1)
printnumbsers(3)