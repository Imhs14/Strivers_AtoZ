def pattern20(n):
        for i in range(1,n+1):
            for j in range(1,(n*2)+1):
                if j <= i:
                    print("*",end="")
                elif (n*2) - j < i:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        
        for i in range(n-1,0,-1):
            for j in range(1,(n*2)+1):
                if j <= i:
                    print("*",end="")
                elif (n*2) - j < i:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
pattern20(5)