def realQuickSort(array):
    quickSort(array, 0, len(array) - 1)

def quickSort(alist, left, right):

    if left<right:
        splitpoint = partition(alist, left, right)  # rightmark
        quickSort(alist, left, splitpoint-1)        # Small Group
                # 피봇 = k번째 작은 숫자
        quickSort(alist, splitpoint+1, right)       # Large Group

def partition(a, left, right):

    pivotValue = a[left]
    leftmark = left+1
    rightmark = right
    print("pivot : ", pivotValue)
    print("left : ", leftmark, " right : ", rightmark)
    done = False
    while not done:
        while leftmark <= rightmark and a[leftmark] <= pivotValue:
            leftmark = leftmark + 1
            print(a)
        while a[rightmark] >= pivotValue and rightmark >= leftmark:
            rightmark = rightmark - 1
            print(a)
        if rightmark < leftmark: # 오른쪽 끝에서 온 rightmark가 leftmark보다 작아질 때
            done = True
        else:                   # swap했다 swap(leftmark,rightmark)
            temp = a[leftmark]
            a[leftmark] = a[rightmark]
            a[rightmark] = temp

    # swap(first,rightmark)
    temp = a[left]
    a[left] = a[rightmark]
    a[rightmark] = temp

    return rightmark

data = [8, 2, 4, 1, 5, 9, 7, 18, 15, 12]
realQuickSort(data)
print(data)
