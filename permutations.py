from collections import deque 
def perm(A):

	if len(A)==2: 
		return [A,A[::-1]]
	else:
		X = [] 
		for i in range (len(A)):
			B = [0]*len(A)
			for j in range (len(B)): 
				B[j] = A[j]
			B[0],B[i] = B[i],B[0]

			C = [0]*(len(B)-1)
			for j in range (len(B)-1): 
				C[j] = B[j+1] 

			ret = perm(C) 

			for x in ret: 
				x = deque(x) 
				x.appendleft(B[0]) 
				y = [0]*len(x) 
				for j in range (len(x)): 
					y[j]=x[j]
				X.append(y)
		return X 

T = int(input()) 
L = [i+1 for i in range (T)] 
ans = perm(L)
print(len(ans))
for a in ans: 
	print(a) 
