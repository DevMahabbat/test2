#1
# a = int(input())
# b = int(input())

# c = a+b

# print(c)

#2

# def yarat():
#     n = int(input())
#     list1 =  list()
#     for i in range(n):
#         list1.append(input())
#     return list1


# listim = yarat()
# print(listim)


#3.1

# n = int(input())
# s= 0 
# for i in range(n):
#     s+= int(input())

# print(s)

#3.2
# n = int(input())
# s= 0 
# list1 = []
# for i in range(n):
#     list1.append(int(input()))

# for i in list1:
#     s+= i

# print(s)
#3.3

# s= 0 
# while True:
#     k = input()
#     if k == 'q':
#         break
#     s  += int(k)

# print(s)


#4.1
# k=list([3,5,1,56,1,6,7,21,11,1])
# k2 = k[1::2]
# s= 0
# for i in k2:
#     s+= i
# print(s)

#4.2
# k=list([3,5,1,56,1,6,7,21,11,1])
# count = 0 
# s= 0
# for i in k:
#     count += 1
#     if count %2 == 0:
#         s+= i

# print(s)

#4.3
# k=list([3,5,1,56,1,6,7,21,11,1])
# s = 0
# for count, i in enumerate(k):
#     if count %2 == 1:
#         s+= i
# print(s)

# 5.1
# k=list([3,5,1,56,1,6,7,21,11,1])
# s2 = 0
# s1 = 0 
# for count, i in enumerate(k):
#     if count %2 == 1:
#         s2+= i
#     else:
#         s1 +=i
# print(s2-s1)


# # 6.1
# n= int(input())
# n =12
# s = 0 
# for i in range(1,n+1):
#     if i % 3 == 0:
#         s += i
# print(s)

#6.2
# n = int(input())
# s = 0
# i = 0
# while True:
#     if i<=n:
#         s+=i
#         i+=3
#     else:
#         break

  
# print(s)
#6.3
# n= int(input())
# s = 0 
# for i in range(3,n+1,3):
#     s += i
# print(s)
#7.1
# soz = input()
# soz = soz[:3]
# for i in soz:
#     print(i)

