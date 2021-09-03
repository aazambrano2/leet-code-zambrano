inputArr_size = 6

def largestSumSequence(inputArr):
# Write your code here
    if inputArr == 1:
        return inputArr[0]
    max_by_index = []
    maxL = []
    add = 0
    for i in range(inputArr_size):
        for j in range(inputArr_size):
            add = sum(inputArr[i:inputArr_size-j])
            if i > 0:
                add += sum(inputArr[:i])
                maxL.append(add)
                add = 0
        if maxL:
            max_by_index.append(max(maxL))
    print(max_by_index)
    pass
largestSumSequence([2,-8,3,-2,4,-10])