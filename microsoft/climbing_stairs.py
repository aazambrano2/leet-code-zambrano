
def climbStairs( n):
    """
    :type n: int
    :rtype: int
    """
    if n <= 3: return n
    A = [0]*(n+1)
    A[0],A[1],A[2],A[3]  = 1,1,2,3
    acc = 0
    for i in range(3,len(A)):
        acc = A[i] + A[i-1]
        A[i+1] = acc
        if A[-1] != 0:
            break

        
    return A[-1]

print(climbStairs(5))
        
        
