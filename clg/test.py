# x = 'Apple Is the'
# print(x.istitle())
# ------------------------------------
# x = 'p'
# print(chr(ord(x))) #chr is used to covert ascii to characters
# ------------------------
# x = 'python'
# ans = []
# for i in x:
#     if i.islower():
#         o = ord(i)+3
#         if o>90:
#             r = o-90
#             ans.append(chr(65+r))
#         else:
#             ans.append(chr(o))

# print(ans)
# -----------------------
# nums1 = [3,4,45,5,67,7]
# nums2 = [1,34,5,7,4,2]
# num = nums1 + nums2
# print(sorted(num))

# str = 'you fucking bitch i\'ll kill you'

# for i in range(len(str)-1,-1,-1):
#     print(str[i],end="")
# prime numbers are always    
# arr = list(str)
# print(len(arr))
# def fun(num:str)->int:
#     return int(num)
    
# str = '12345678'
# arr  = list(str)
# print(arr)
# arr = list(map(fun,arr))
# print(arr)

# # for i, v in enumerate(arr):
# #     print(i, v,end=" ")


ch = 'a'
if ord(ch) + 3 > 122:  # Check if it exceeds the ASCII value for 'z'
    ascii = (ord(ch) + 3) % 122 + 96  # Wrap around to 'a'
else:
    ascii = ord(ch) + 3
print(chr(ascii))
