'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:

    age = 0
    name = ""

    #initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #method to increase age by 1
    def increase_age(self):
        self.age = self.age + 1
        print(self.age)

    #method to print greeting
    def say_greeting(self):
        print("Hello world! My name is", self.name)
    
    #method to count up to age by 1
    def count_to_age(self):
        count = 1
        while count <= self.age:
            print (count)
            count = count + 1



# You won't need to call anything here.