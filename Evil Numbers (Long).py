#Approach 1: (58 bytes, 58 chars)
[print(i) for i in range(0,1001) if bin(i).count('1')%2<1]
