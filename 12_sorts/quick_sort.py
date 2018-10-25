def quick_sort(a):
    quick_sort_c(a, 0, len(a) - 1)


def quick_sort_c(a, low, high):
    if low >= high:
        return
    mid = partition(a, low, high)
    quick_sort_c(a, low, mid - 1)
    quick_sort_c(a, mid + 1, high)


def partition(a, low, high):
    pivot, i = a[high], low
    for j in range(low, high):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[high], a[i] = a[i], a[high]
    return i


if __name__ == '__main__':
    a = [6, 11, 3, 9, 8]
    quick_sort(a)
    print(a)
