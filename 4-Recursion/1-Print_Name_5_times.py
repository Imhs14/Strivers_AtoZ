def name(n,k):
    if k <= 0:
        return
    print(n)
    name(n,k-1)
name("heera",4)

"""
print_k_times("hello", 3)
  -> prints "hello", calls print_k_times("hello", 2)
       -> prints "hello", calls print_k_times("hello", 1)
            -> prints "hello", calls print_k_times("hello", 0)
                 -> k <= 0, just returns (nothing happens) 
"""

