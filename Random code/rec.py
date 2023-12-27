def bin_search(arr,n):
    mid = len(arr)//2

    if arr[mid] == n:
        return mid
    if n > arr[mid]:
        return bin_search(arr[mid+1:], n) + mid
    else:
        return bin_search(arr[:mid], n)
print(bin_search([1,2,3,4,5],4))