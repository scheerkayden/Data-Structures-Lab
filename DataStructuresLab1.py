#Kayden Scheer
#8/28/2026
#Data Structures Lab 1

# import time

# start = time.time()

# total = 0
# for i in range(1_000_000):
#     total += i

# end = time.time()

# print("Time:", end - start)

#Measured Time: 0.1388871669769287 seconds
#Did not receive the same time each run.
#The measured time might change because it's looking in different ranges so it takes longer to look
#Predicted Complexity: O(n)

# import time

# numbers = list(range(1_000_000))

# start = time.time()
# x = numbers[999999]
# end = time.time()

# print(x)
# print("Time:", end - start)

#The work increases as the list grows
#Time Complexity: O(1)
#Space Complexity: O(n)

# import time

# numbers = list(range(1_000_000))

# start = time.time()

# total = 1000000
# for x in numbers:
#     total += x

# end = time.time()

# print("Total:", total)
# print("Time:", end - start)

#Measured Time at 1000: 0.07543492317199707
#Measured Time at 100000: 0.14976978302001953
#Measured Time at: 1000000: 0.06891536712646484

#As n increaes, the time decreases. Although I don't think that's supposed to happen.
#Time Complexity: O(n)
#Space Complexity: O(n)

# import time

# numbers = list(range(2000))

# start = time.time()

# count = 0
# for i in numbers:
#     for j in numbers:
#         count +=1

# end = time.time()

# print(count)
# print("Time:", end - start)

#The inner operation is performed n^2 times.
#When n doubles, the time quadruples.
#Time Complexity: O(n^2)
#Space Complexity: O(n)

# for i in range(n):
#     print(i)

# for j in range(n):
#     print(j)

# for i in range(n):
#     for j in range(n):
#         print(i, j)

#Code A Complexity: O(n)
#Code B Complexity: O(n^2)
#Code A isn't O(n^2) because the two loops are separate and not nested.

# def search(numbers, target):
#     for x in numbers:
#         if x == target:
#             return True
#     return False

# numbers = [10, 20, 30, 40, 50]

#Case 1. Finds number immediately, O(1)
#Case 2. Searches till middle of list, O(n/2)
#Case 3. Searches entire list, O(n)
#Case 4. See Case 3.
#The same algorithm can have different time complexities depending on the input.
#Best case: O(1), Worst case: O(n), Average case: O(n/2)

# def first_element(numbers):
#     x = numbers[0]
#     return x

#There is no additional memory created.
#Space complexity: O(1)

# def copy_list(numbers):
#     result = []
#     for x in numbers:
#         result.append(x)
#     return result

#Result grows as input grows.
#Space complexity: O(n)

def mystery(numbers):
    for i in numbers:
        print(i)

    for i in numbers:
        print(i)

    for i in numbers:
        for j in numbers:
            print(i, j)

#Before running Time Complexity: O(n^2)
#Before running Space Complexity: O(1)

#I think I am correct in my time complexity because the inner loop is nested and will run n^2 times. I think I am correct in my space complexity because there is no additional memory being created.