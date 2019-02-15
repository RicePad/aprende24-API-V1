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
total = 0
roman_dic = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# 1 - 3999 range
# def roman_to_int(string):
#      roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#      int_val = 0
   
#      for i in range(len(string)):
#          int_val = int_val + roman_val[string[i]]
#      return int_val


# roman = roman_to_int("I")
# print(roman)
roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
string = "IX"
x = roman_val[string[1-1]]
print(x)


