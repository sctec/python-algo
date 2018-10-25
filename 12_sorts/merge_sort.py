def merge_sort(a):
    merge_sort_internally(a, 0, len(a) - 1)


def merge_sort_internally(a, low, high):
    # 递归终止条件
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort_internally(a, low, mid)
    merge_sort_internally(a, mid + 1, high)
    merge(a, low, mid, high)


# 合并
def merge(a, low, mid, high):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end + 1])
    a[low:high + 1] = tmp


if __name__ == '__main__':
    a1 = [4, 5, 2, 3, 8]
    a2 = [3, 6, 1, 4, 9, -1, 5, 0, -2]
    merge_sort(a1)
    merge_sort(a2)
    print(a1)
    print(a2)
