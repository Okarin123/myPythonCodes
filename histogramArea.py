def maxArea(hist): 
    maxArea = -1e9
    hStack, pStack = list(), list()
    for pos in range(len(hist)): 
        h = hist[pos] 
        if not hStack or h>hStack[len(hStack)-1]: 
            hStack.append(h)
            pStack.append(pos)
        elif h<hStack[len(hStack)-1]:
            while hStack and h<hStack[len(hStack)-1]: 
                tempH = hStack.pop()
                tempPos = pStack.pop() 
                maxArea = max(maxArea, tempH*(pos-tempPos))
            hStack.append(h)  
            pStack.append(tempPos) 
    pos += 1
    while hStack: 
        tempH = hStack.pop()
        tempPos = pStack.pop() 
        maxArea = max(maxArea, tempH*(pos-tempPos))
    return maxArea

A = list(map(int, input().split()))
print(maxArea(A)) 