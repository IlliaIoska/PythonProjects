

# import math
#
# def isPalindrome(phrase):
#     phraseModified = phrase.replace(" ", "")
#     if (len(phraseModified) % 2 == 0):
#         print("Not a polindrome")
#     else:
#         middleIndex = len(phraseModified) // 2
#         print(middleIndex)
#         firstHalfOfPhrase = phraseModified[:middleIndex]
#         secondHalfOfPhrase = phraseModified[middleIndex + 1]
#         secondHalfOfPhraseReversed = secondHalfOfPhrase[::-1]
#         if (firstHalfOfPhrase.lower() == secondHalfOfPhraseReversed.lower()):
#             print(f"{phrase} Is a palindrome")
#         else:
#             print(f"{phrase} is not a palindrome")
#
# isPalindrome("za z")

# x = 50
#
# def printX(x):
#     global x
#     print(f"x is {x}")
#
#     x = 34
#     print(f"new x is {x}")
#
# print(x)
# array = [1, 2, 3]
# squaredNumbers = list(map(lambda num: num ** 2, array))
# print(squaredNumbers)
#
# def isLessThan4(num):
#     if (num < 4):
#         return num
# print(list(filter(isLessThan4, squaredNumbers)))
# def play_spy(array):
#     if(len(array) < 3):
#         print("The array is too short")
#     else:
#         array_007 = []
#         for i in range(0, len(array)):
#             if (array[i] == 0 and array[i + 1] == 0 and array[i + 2] == 7):
#                 array_007.append(array[i])
#                 array_007.append(array[i + 1])
#                 array_007.append(array[i + 2])
#             else:
#                 pass
#         print(array_007)
#
# play_spy([0, 0, 0, 7])

# import math
#
#
# primes = [1, 2]
#
# def count_primes_upto(num):
#     if(num <= 2):
#         return 0
#     else:
#         divisors = 0
#         for i in range(3, num):
#             divisors = 0
#             print(f"i is {i}")
#             for j in range(2, math.ceil(math.sqrt(i)) + 1):
#                 if (i % j == 0):
#                     print(f"{i}/ {j}")
#                     print(f"{i}'s not a prime")
#                     divisors += 1
#                     continue
#                 else:
#                     pass
#             if (divisors > 0):
#                 continue
#             else:
#                 primes.append(i)
#
#         print(primes)
#
# count_primes_upto(10)


# def is_prime(number):
#     if(number <= 0):
#         return False
#     else:
#         for i in range(2, math.sqrt(number)):
#             if (number % i == 0):
#                 return False
#             else:
#                 return True

# import math
# primes = []
# def count_primes_up_to(num):
#     x = 3
#     if (num <= 1):
#         return 0
#     else:
#         while(x < num):
#             for y in range(2, x, 2):
#                 if (x % y == 0):
#                     break
#             else:
#                 primes.append(x)
#             x += 2
#         print(primes)
#
#
#
# count_primes_up_to(100)

# def has_9(array):
#     if (array.index(9) >= 0):
#         return array.index(9)
#     else:
#         return False
#
# def has_6(array):
#     if (array.index(6) >= 0):
#         return array.index(6)
#     else:
#         return False
#
# def sum_num_in_array(array):
#     sum = 0
#     if (has_6(array) != False and has_9(array) != False):
#         new_array = array[:has_6(array)]
#         for i in new_array:
#             sum += i
#         print(sum)
#
# array = [1, 2, 3, 6, 5, 9]
# sum_num_in_array(array)

# def is_sum_20(num1, num2):
#     if (num1 + num2 == 20):
#         return True
#     else:
#         return False
#
# num1 = 20
# num2 = 0
#
# print(is_sum_20(num1, num2))



# def does_start_with_s(string1, string2):
#     char1 = string1[0]
#     char2 = string2[0]
#     if (char1.lower() == char2.lower()):
#         return True
#     else:
#         return False
# string1 = "Sex"
# string2 = "six"
#
# print(does_start_with_s(string1, string2))


# def is_even(num):
#     if (num % 2 == 0):
#         return True
#     else:
#         return False
#
# def compare_even_nums(even_num1, even_num2):
#     if (even_num1 > even_num2):
#         print(f"{even_num1} is greater")
#     elif (even_num2 > even_num1):
#         print(f"{even_num2} is greater")
#     else:
#         print("equal")
#
# num1 = 4
# is_even(num1)
# num2 = 2
# is_even(num2)
# compare_even_nums(num1, num2)







# st = 'Create a list of the first letters of every word in this string'
# firstLetterList = [x[0] for x in st.split(" ")]
# print(firstLetterList)


# for i in range(1, 100):
#     if ((i % 5 == 0) and (i % 3 == 0)):
#         print("{} Divisible by 3 as well as by 5. FizzBuss".format(i))
#     elif(i % 3 == 0):
#         print("Number {} is devisible by 3. Fizz".format(i))
#     elif(i % 5 == 0):
#         print("Number {} is divisible by 5. Buzz".format(i))




# st = 'Print every word in this sentence that has an even number of letters'
# for i in st.split(" "):
#     if (len(i) % 2 == 0):
#         print("Even")


# list = [i for i in range(1, 50) if (i % 3 == 0)]
# print(list)



# for i in range(0, 10):
#     if (i % 2 == 0):
#         print(i)

# st = 'Print only the words that start with s in this sentence'
# for s in st.split(" "):
#     if (s[0].lower() == "s"):
#         print(s)


# list = [li for li in range(0, 11)]
#
# dict = {
#     "key1": "value1",
#     "key2": "value2"
# }
#
# listOfTuples = [(1, 2), (3, 4), (5, 6)]
# listOfTuplesCopy = [(a, b) for (a, b) in listOfTuples]
# print(listOfTuplesCopy)
# for item in listOfTuples:
#     for subItem in item:
#         print(subItem)
# print("\n")
# for (a, b) in listOfTuples:
#     print(a)
#     print(b)



# l_one = [1,2,[3,4]]
# l_two = [1,2,{'k1': 4}]
# print(l_one[2][0] >= l_two[2]['k1'])

# print(4**0.5 != 2)


# list5 = [1,2,2,33,4,4,11,22,3,3,2]
# print(set(list5))





# dictionary = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# print(dictionary["k1"][2]["k2"][1]["tough"][2][0])
