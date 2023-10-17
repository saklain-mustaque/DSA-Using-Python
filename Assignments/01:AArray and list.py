# sort Array
# li = []
# n = int(input("How many elements you want to enter:"))
# while len(li) <= n:
#     li.append(int(input("Enter the elements:")))
# li.sort()
# print(li)

# Remove non-int from the list
# li = ['saklain',1,2,3,4.0,5,'Mustaque']
# print(f'List before removing non-int:{li}')
# for ele in li:
#     if type(ele) != int:
#         li.remove(ele)
# print(f'List after removing non-int:{li}')


# Calculate average of list elements
# li = [1,2,3,4,5]
# print("Average of list elements: ", sum(li)/len(li))

# Create a list of first N prime numbers

# N = int(input("Till what number you want prime numbers: "))
# prime_num = []
# for i in range(1,N+1):
#     count = 0
#     for j in range(1,i):
#         if i%j == 0:
#             count += 1
#     if count == 1:
#         prime_num.append(i)
# print(prime_num)


# create a list of first N terms of fibonacci series

# def firt_n_fibonacci(n):
#     a = 0
#     b = 1
#     print(a,b, end=" ")
#     for ele in range(2,n):
#         c = a + b
#         print(c, end=" ")
#         a = b
#         b = c
#     print(end="\n")
# firt_n_fibonacci(5)