def bin_search(arr,n):
    mid = len(arr)//2
    # print(mid)

    if arr[mid] == n:
        return mid
    if n > arr[mid]:
        return bin_search(arr[mid+1:], n) + mid
    else:
        return bin_search(arr[:mid], n) + mid
# print(bin_search([1,2,3,4,5, 12, 34,221, 567],5 ))


print(bin_search([1,2,3,4,5],4))