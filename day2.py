#leetcode problem 33

#rotated sorted array

# arr=[4,5,6,1,2,3]
# t=6
# low=0
# high=len(arr)-1
# while (low<=high):
#     mid=(low+high//2)
#     if arr[mid]==t:
#         print(mid)
#         break
#     if arr[mid]>arr[low]:
#         if arr[low]<t and t<=arr[mid]:
#             high=mid-1
#         else:
#             low=mid+1
#     else:
#         if t>=arr[mid] and t<=arr[high]:
#             low=mid+1
#         else:
#             high=mid-1
# else:
#     print(-1)



#bubble sort

# a=[2,5,3,8,9,6,1]
# for x in range(len(a)):
#     for y in range(1,len(a)):
#         if a[y-1]>a[y]:
#             a[y],a[y-1]=a[y-1],a[y]
# print(a)

# #odd and even using bubble sort
# a=[1,2,5,3,8,9,6,1,4,8,2,6]
# for x in range(len(a)):
#     for y in range(len(a)-1):
#         if a[y]%2==0:
#             a[y],a[y+1]=a[y+1],a[y]
# print(a)



# #selection sort::
# a=[2,5,3,8,9,6,1,4,8,11]
# for x in range(len(a)):
#     for y in range(x,len(a)):
#         if a[x]>=a[y]:
#             a[x],a[y]=a[y],a[x]
# print(a)

    
# insertion sort
# a=[2,10,6,5,24,3,7,8,1,0.5]
# for x in range(1,len(a)):
#     if a[x]<a[x-1]:
#         a[x],a[x-1]=a[x-1],a[x]
#         while x>0:
#             if a[x]<a[x-1]:
#                 a[x],a[x-1]=a[x-1],a[x]
#             x-=1
# print(a)


#small in ROTATED sorted array
# arr=[4,5,6,1,2,3]
# low=0
# ans=arr[0]
# high=len(arr)-1
# while(low<=high):
#     mid=(low+high)//2
#     if arr[mid]>=arr[low]:
#         if (arr[low]<ans):
#             ans=arr[low]
#         low=mid+1
#     else:
#         if arr[mid]<ans:
#             ans=arr[mid]
#         high=mid-1
# print(ans)
