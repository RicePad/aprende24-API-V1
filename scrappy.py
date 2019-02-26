# #create a tuple of nodes
# nodes = ('A', 'B', 'C', 'D', 'E')

# #create a double dicitionary of distances
# distances = {
#   'C': {"A": 1, "B": 7, "D": 2},
#   'A': {"B": 3, "C": 1},
#   'D': {"B": 5, "C": 2, "E": 7},
#   'B': {"A": 3, "B": 7, "B": 5},
#   'E': {"B": 1, "D": 7},
#   }

# #loop through a dictionary of array
# unvisited = {node: float("inf") for node in nodes }
# #create an empty dictionary 
# visited = {}
# #choose a start point
# current = "C"
# #set distance 
# currentDistance = 0 
# #set starting and distance in dictionary
# unvisited[current] = currentDistance

# #Djikstra's Algorithm:

# while True:
#     for neighbour, distance in distances[current].items():
#         print("k:{0}, v:{1}".format(neighbour, distance))

#         if neighbour not in unvisited: continue
#         newDistance = currentDistance + distance
        
#         if unvisited[neighbour] is float("inf") or unvisited[neighbour] > newDistance:
#             unvisited[neighbour] = newDistance
#     visited[current] = currentDistance
#     print("visited", visited)

#     del unvisited[current]
#     print("unvisited:", unvisited)      

#     if not unvisited: break
#     candidates = [node for node in unvisited.items() if node[1]]
#     print("candidates:", candidates)

#     current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]
#     print("current:", current)
#     print("currentDistance:", currentDistance)
# print(visited)


# from collections import deque
# 2	
# 3	def person_is_seller(name):
# 4	      return name[-1] == 'm'
# 5	
# 6	graph = {}
# 7	graph["you"] = ["alice", "bob", "claire"]
# 8	graph["bob"] = ["anuj", "peggy"]
# 9	graph["alice"] = ["peggy"]
# 10	graph["claire"] = ["thom", "jonny"]
# 11	graph["anuj"] = []
# 12	graph["peggy"] = []
# 13	graph["thom"] = []
# 14	graph["jonny"] = []

# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]

#     while search_queue:
#         person = search_queue.pop_left()

#         if person not in searched:
#             if person_is_seller(person):
#                 print("person is seller")
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False
    
#two sum algorithms
# list = [2, 7, 11, 15]
# target = 9
# #brute force 
# def twoSum_brute(list, target):
#     for i in range(len(list) - 1): #output: 0,1,2  -array index
#         for k in range(i+1, len(list)): # selects indexes starting at position 1
#             if list[i] + list[k] == target:
#                 return[i,k]
#     return False




# result = twoSum_brute(list, target)
# print(result)    

# def twoSum_hash(list, target):
#     hash_table = {}

#     for i in range(len(list)): #outputs all array indexes
#         if list[i] in hash_table:
#             return [hash_table[list[i]], list[i]]
#         else:
#             hash_table[target - list[i]] = list[i]
#     return False

# result = twoSum_hash(list, target)
# print(result) 


#Reverse integer
# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

# numbers = 123 
# numberString = str(numbers)
# reverseString = numberString[::-1]
# reverseNumber = int(reverseString)
# print(type(reverseNumber))

# def reverseNumber(number):
#     numberToString = str(number)
#     reverseString = numberToString[::-1]
#     stringToNumber = int(reverseString)
    
#     return stringToNumber
    

# x = reverseNumber(numbers)
# print(x)

# def reverseNumber(number):
#     reverse = 0
    
#     while (number > 0):
#         lastDigit = number % 10 #d
#         reverse = (reverse * 10) + lastDigit #r
#         number = int(number / 10)
#     return reverse


# def reverseNumber(number):
#         reverse = 0

#     # Handling negative numbers  
#         negativeFlag = False
#         if (number < 0): 
        
#             negativeFlag = True
#             number = -number

#         while number != 0:   
#             last_digit = number % 10
#             reverse = (reverse * 10) + last_digit
#             number = int(number/10)
#         return -reverse if (negativeFlag == True) else reverse

# r = reverseNumber(-124)
# print(r)




# 123 ---> 321 reverse integer 

# def reverse(number):
#     #on/off boolean if number is negative

#     numberIsNegative = False
#     if number < 0:
#         numberIsNegative = True
#         number = -number

#     #store reverse numbers
#     reverse = 0
    
#     #if number is not zero keep looping
#     while number != 0:
#     #select last digit
#         lastDigit = number % 10
#         print("lastDigit:", lastDigit)
#     #store last digit in reverse 
#         reverse = ( reverse * 10 ) + lastDigit
#         print("reverse:", reverse)
#     #select next number in reverse
#         number = int(number/10)
#         print("number:", number)
#     return -reverse if(numberIsNegative == True) else reverse


# print(reverse(-123))

#Roman to integer 
# total = 0
# roman_dic = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000
# }

# 1 - 3999 range
# def roman_to_int(string):
#      roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#      int_val = 0
   
#      for i in range(len(string)):
#          int_val = int_val + roman_val[string[i]]
#      return int_val


# roman = roman_to_int("I")
# print(roman)
# string = "IX"
# int_value = 0
# def romanToInteger(string):
#     roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     int_value = 0

#     #loop through the string 
#     for i in range(len(string)):
#         if i > 0 and roman_val[string[i]] > roman_val[string[i - 1]]:
#             int_value = int_value + roman_val[string[i]] - 2 * roman_val[string[i - 1]]
#         else:
#             #if string in dictionary add value to int value variable
#             int_value = int_value + roman_val[string[i]]
#             print(int_value)
#     return int_value


# roman = romanToInteger(string)
# print(roman)

#Common prefix algorithm:
# list = ['flower', 'flow', 'florence']
# def commonPrefix(list):
#     for i in range(len(list[0])):
#         char = list[0][i]
#         for j in range(1,len(list)):
#             if i == len(list[j]) or list[j][i] != char:
#                 return list[0][:i] 
#     return list[0]

# print(commonPrefix(list))


#Valid parenthesis algorithm:
# string = "()"
# string2 = "()[]{}"
# string3 = "(]"

# # create a stack 
# stack = []
# #create a hash_table with k closing and v of opening
# hash_table = {
#     ")": "(",
#     "}": "{",
#     "]": "[", 
# }

# def isValid(string):
#     stack = []
    
#     hash_table = {
#     ")": "(",
#     "}": "{",
#     "]": "[", 
#         }

#     for char in string:
#         if char in hash_table:
#             top_element = stack.pop()   
#             if hash_table[char] != top_element:
#                 return False
#         else:
#             stack.append(char)
#     return not stack


#parenthesis checker
# string = "()"
# hash_table = {
#     ")": "(",
#     "}": "{",
#     "]": "[",
# }

# stack = []

# #loop and store each character of the string into a variable
# for char in string:
#     print(char)
#         #if parenthesis is closed  or in the dictionary
#     if char in hash_table:
#         #if parenthesis is opened insert into the stack
#         top_element = stack.pop() if stack else ""
#         if hash_table[char] != top_element:
#             print(False)
#     else:
#         stack.append(char)
# print(not stack)


#merge two sorted two sorted LinkedList

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(ListNode):
#     def mergeTwoLists(self, list1, list2):
#         dummy = cur = ListNode(0)

        # while list1 and list2:
        #     if list1.val < list2.val:
        #         cur.next = list1
        #         list1 = list1.next
        #     else:
        #         cur.next = list2
        #         list2 = list2.next
        #     cur = cur.next
        # cur = list1 or list2 
        # return dummy.next
        

#remove duplicates from sorted array
# list = [1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,5]

# def removeDuplicates(list):
#     if not list:
#         return 0
    
#     counter = 0 
    
#     for i in range(1,len(list)):
#         if list[i] != list[counter]:
#             counter = counter + 1
#             list[counter] = list[i]
#     return counter + 1

# print(removeDuplicates(list))