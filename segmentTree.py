import math 

def query(node, start, end, l, r): 
        if l<=start and r>=end:
            return tree[node]
        elif l>end or r<start: 
            return 1e9 
        else: 
            mid = (start+end)//2
            return min(query(2*node+1, start, mid, l, r), query(2*node+2, mid+1, end, l, r))

def build(node, start, end): 
    if start == end: 
        tree[node] = A[start] 
    else: 
        mid = (start+end)//2
        build(node*2+1, start, mid)
        build(node*2+2, mid+1, end) 
        tree[node] = max(tree[2*node+1], tree[2*node+2])
        
def update(node,start,end,idx,val): 
    if start==end: 
        A[idx] += val 
        tree[node] += val 
    else: 
        mid = (start+end)//2 
        if start<=idx and idx<=mid: 
            update(2*node+1,start,mid,idx,val) 
        else: 
            update(2*node+2,mid,end,idx,val) 
        
        tree[node] = max(tree[2*node+1],tree[2*node+2]) 

A = list(map(int, input().split())) 
N = len(A) 
tree = [0]*(2**(int(math.log(N,2))+2)-1)
build(0,0,N-1)
print(tree)     
l, r = map(int, input().split())
print(query(0, 0, N-1, l, r))