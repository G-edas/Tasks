# #1
# print(15//4)

# #2
# string = "We have x small boxes, y large boxes, z medium boxes"
# x = 10
# y = 25
# z = 45
# print(string.format(x= 10, y= 25, z= 45))

# #3
# chars = "<<>>"
# word = "hello"
# if((len(chars) % 2) == 0):
#     print(chars[0:(int(len(chars)/2))] 
#     + word 
#     + chars[int((len(chars)/2)):])
# else:
#     print("String must be even")


# #4
# word1 = "Vehicle"
# word2 = "Robot"
# print(word1[1:] + word2[0:1] + word2[2:])


# #5
# chars = "<[<||>]>"
# word = "mirror"
# print(chars[0:(int(len(chars)/2))] + word + chars[int((len(chars)/2)):])


# my_list = [{'Tom': 20000, 'Bill': 12000}, ['car', 'laptop', 'TV']]
# print(my_list[0]['Bill'])

# my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]
# my_list[2][0][3] = 'x'
# my_list[3] = 'Television'
# print(my_list)


# def merge_list(a, b):
#     if isinstance(a, list) and isinstance(b, list):
#         print(a+b)
#     else:
#         print("given type is not list")      
# merge_list([2,3,6], [4,5])


# def seperate(string):
#     x = list()
#     for char in str(string):
#         x.append(char)
#     return x
# print(seperate("labas"))


# def separate(text):
#     return list(text)
# print(seperate('labas'))

    
# def type_counter(*items):
    
#     x = list()
#     for item in items:
#         t = type(item)
#         x.append(t)
        
#     y = dict()
#     for n in x:
#         if n in y:
#             y[n] += 1
#         else:
#             y[n] = 1
#     return y
        
# print(type_counter(1,2,3,4, 'abc', ['a', 'b']))



# def grow_string(string):
#     lenght = len(string)
#     i = 1
#     word = ''
#     while i <= lenght:
#         word += string[0:i]
#         i += 1
#     return word

# print(grow_string('ab'))


# def growing_string(string):
#     word = ''
#     for i in range(len(string)):
#         word += string[0:i+1]
#     return word
# print(growing_string('Code'))



# def string_match(string1, string2):
    
#     # iter_count = min(len(string1), len(string2))
#     # counter = 0    
#     # for index in range(1, iter_count):   
#     #     if string1[index-1:index+1] == string2[index-1:index+1]:  
#     #         counter += 1    
#     # return counter
    
#     c = 0
#     for letter in range(min(len(string1), len(string2))-1):
#         if(string2[letter] + string2[letter+1] == string1[letter] + string1[letter+1]):
#                 c += 1
#     return c

# print(string_match('xxcaazz', 'xxbaaz'))
# print(string_match('abc', 'abcz'))
# print(string_match('abc', 'axc2'))
# print(string_match('axc', 'abxc'))

  
# class Animal:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def eat(self):
#         print("Animal eats")
            
# class Dog(Animal):

#     def move(self):
#         print("Dog moves")
  
# class Fish(Animal):
        
#     def move(self):
#         print("Fish moves")
    
# class Bird(Animal):
              
#     def move(self):
#         print("Bird movies")


# instance_dog = Dog('Harry', 10)
# instance_dog.nam

# class BankAccount():
    
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
    
#     # def __str__(self):
#     #     # return str(self.balance)
#     #     return self
    
#     def __repr__(self):
#         return str(self.balance)
        
#     def deposit(self, depo):
#         self.balance += depo
#         return depo
    
#     def withdraw(self, withdrw):
#         if withdrw > self.balance:
#             return str("Not enough amout of money in bank account.")
#         else:
#             self.balance -= withdrw
#             return withdrw


# my_account = BankAccount('Gedas', 100)
# my_account.deposit(20)
# print(my_account.balance)
# print(my_account.withdraw(121))
# print(my_account)


