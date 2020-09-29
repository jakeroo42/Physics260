from numpy import empty,copy

def solvematrix(M,b): #M is the batrix b is the vector 

    A = copy(M)
    v = copy(b)
    N = len(v)
    
    # Gaussian elimination
    for m in range(N):
        
        #Next 3 blocks make sure the the top left element is not 0 
        
        # Partial pivoting
        maximum = abs(A[m,m])
        pivot = m
        
        # Determine which row has largest element
        for n in range(m+1,N):
            if abs(A[n,m]) > maximum:
                pivot = n
        
        # Swap rows
        for n in range(N):
            A[m,n], A[pivot,n] = A[pivot,n], A[m,n]
        v[m], v[pivot] = v[pivot],v[m]
        
        # Divide by the diagonal element
        div = A[m,m]
        A[m,:] /= div
        v[m] /= div
    
        # Now subtract from the lower rows
        for i in range(m+1,N):
            mult = A[i,m] #first element of next row
            A[i,:] -= mult*A[m,:]
            v[i] -= mult*v[m]
    
    # Backsubstitution
    x = empty(N,float) #solution to the matrix 
    for m in range(N-1,-1,-1):
        x[m] = v[m]
        for i in range(m+1,N):
            x[m] -= A[m,i]*x[i]

    return(x)

