#Program to implement tower of Hanoi

def hanoi(n,A,B,C):
    if n > 0:
        hanoi(n-1,A,C,B)
        if A:
            C.append(A.pop())
        hanoi(n-1,B,A,C)
        
#Main
A = [1,2,3,4]
C = []
B = []

hanoi(len(A),A,B,C)
print(A,B,C) 