# 冒泡排序
def bubbleSort(a):
    n = len(a)
    if n <= 1:
        return
    for i in range(n):
        flag = False
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = True
        if not flag:
            break


a = [1, 3, 4, 7, 9, 0, 2, 3, 4, 56]
bubbleSort(a)
print("a = " + str(a))


# 插入排序
def insertSort(a):
    n = len(a)
    if n <= 1:
        return
    for i in range(1, n):
        value = a[i]
        j = i - 1
        # 查找要插入的位置并移动数据
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value


b = [1, 3, 4, 7, 9, 0, 2, 3, 4, 56]
bubbleSort(b)
print("b = " + str(b))


# 选择排序
def selectionSort(a):
    n = len(a)
    if n <= 1:
        return
    for i in range(1, n):
        # 查找最小值
        min_index = i
        for j in range(i, len(a)):
            if a[j] < a[min_index]:
                min_index = j

        a[i], a[min_index] = a[min_index], a[i]


c = [1, 3, 4, 7, 9, 0, 2, 3, 4, 56]
bubbleSort(c)
print("c = " + str(c))
