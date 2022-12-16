def quick_sort(lst):
    """
    The function takes a list and sorts it using a method quick sort
    >>> quick_sort([ 23, 67, 2, 4, 7, 89])
    [2, 4, 7, 23, 67, 89]
    """
    start = 0
    end_lis = len(lst) - 1
    poil = lst[end_lis]
    while start <= end_lis:
        while lst[start] < poil:
            start = start + 1
        while poil < lst[end_lis]:
            end_lis = end_lis - 1
        if start <= end_lis:
            lst[start], lst[end_lis] = lst[end_lis], lst [start]
            start = start + 1
            end_lis = end_lis - 1
    if 0 < end_lis:
        lst[0:end_lis + 1] = quick_sort(lst[0:end_lis + 1])
    if start < len(lst):
        lst[start: len(lst)] = quick_sort(lst[start: len(lst)])
    return lst
   

