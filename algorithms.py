def linear_search(array,value):
    """
    (list, int) -> int
    Function finds first index of value. If value is not in array, function will return -1
    >>> linear_search([1,2,3,414,1424,1241,24,124,124,1,412,4,],1)
    0
    """
    for i in range(len(array)):
        if array[i]==value:
            return i
    return -1
  

def merge(lst1,lst2):
    """
    help function for merge_sort
    """
    res = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    while i < len(lst1):
        res.append(lst1[i])
        i += 1
    while j < len(lst2):
        res.append(lst2[j])
        j += 1
    return res
  
def merge_sort(lst):
    """
    lst -> lst
    returns a sorted list
    >>> merge_sort([5,7,2,1,9,7,4,8,3])
    [1, 2, 3, 4, 5, 7, 7, 8, 9]
    """
    if len(lst) == 1:
        return lst
    lst1 = merge_sort(lst[0:(len(lst)//2)])
    lst2 = merge_sort(lst[(len(lst)//2)::])
    return merge(lst1,lst2)


  
  
  def binary_search(list_of_values, value):
    pass
  
  
  
  def selection_sort(lst):
    pass
  
  
  
  def quick_sort(lst):
    pass
