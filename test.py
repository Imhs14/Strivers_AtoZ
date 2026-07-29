from collections import defaultdict
def twoddoccr(n):
    ans = []
    hsh = defaultdict(int)
    for i in range(0,len(n)):
        hsh[n[i]] += 1 

    print(hsh)
    for key, value in hsh.items():
        if value % 2:
            ans.append(key)
    return ans
print(twoddoccr([1,2,3,4,5,4,3,2]))

# time = O(n), space = O(n)