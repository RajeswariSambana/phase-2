# def linear(arr,n):
#     for i in arr:
#         if i==n:
#             return 1
# arr=list(map(int,input().split()))
# n=int(input())
# res=linear(arr,n)
# if res==1:
#     print("found")
# else:
#     print("not found")        # time: O(n)


def binary(arr,key):
    arr.sort()
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif key<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
arr=list(map(int,input().split()))
key=int(input())
res=binary(arr,key)
if res==1:
    print("found")
else:
    print("not found")

    


        
    
