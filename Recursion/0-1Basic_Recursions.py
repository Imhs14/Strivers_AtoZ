def fact(n):
    if n == 0:
        return 1 # when the n becomes 0, it will return 1 and stops the recursion
    else:
        return n * fact(n-1) # it will keep sending the new number by subtracting it with 1.
#print(fact(4))
# return 4 * fact(3)
# return 4 * 3 * fact(2)
# return 4 * 3 * 2 * fact(1)
# return 4 * 3 * 2 * 1 -> This is what it will return here at last , dry run of how the recursion works 

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(6))
"""
fibo(6)
├── fibo(5)
│   ├── fibo(4)
│   │   ├── fibo(3)
│   │   │   ├── fibo(2)
│   │   │   │   ├── fibo(1) -> 1   # count = 1
│   │   │   │   └── fibo(0) -> 0
│   │   │   └── fibo(1) -> 1        # 2
│   │   └── fibo(2)
│   │       ├── fibo(1) -> 1        # 3
│   │       └── fibo(0) -> 0
│   └── fibo(3)
│       ├── fibo(2)
│       │   ├── fibo(1) -> 1        # 4
│       │   └── fibo(0) -> 0
│       └── fibo(1) -> 1            # 5
└── fibo(4)
    ├── fibo(3)
    │   ├── fibo(2)
    │   │   ├── fibo(1) -> 1        # 6
    │   │   └── fibo(0) -> 0
    │   └── fibo(1) -> 1            # 7
    └── fibo(2)
        ├── fibo(1) -> 1            # 8
        └── fibo(0) -> 0
"""
