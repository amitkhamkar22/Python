'''
Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py,
implement a class called Jar with these methods:

    __init__ should initialize a cookie jar with the given capacity, which represents the maximum number
    of cookies that can fit in the cookie jar. If capacity is not a non-negative int, though, __init__
    should instead raise a ValueError.
    __str__ should return a str with n 🍪, where n is the number of cookies in the cookie jar. For instance,
      if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"
    deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s
    capacity, though, deposit should instead raise a ValueError.
    withdraw should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies
    in the cookie jar, though, withdraw should instead raise a ValueError.
    capacity should return the cookie jar’s capacity.
    size should return the number of cookies actually in the cookie jar, initially 0.
'''

class Jar:

    #__init__ initializes of object variables through instantiation
    def __init__(self, capacity = 12, size = 0):

        self.capacity = capacity
        self.size = size

    #__str__returns object value (size) as a string
    def __str__(self):

        return f"{'🍪' * self.size}"

    #deposit is a method of object type Jar
    def deposit(self, add_cookies):
        if self.size + add_cookies <= self.capacity:
            self.size += add_cookies
        else:
            raise ValueError("Adding too many cookies")

    #withdraw is a method of object type Jar
    def withdraw(self, remove_cookies):
        if self.size - remove_cookies >= 0:
            self.size -= remove_cookies
        else:
            raise ValueError("Taking out too many cookies")

    #this is a getter function for capacity
    @property
    def capacity(self):
        return self._capacity

    #this is a setter function for capacity
    @capacity.setter
    def capacity(self,capacity):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError("Invalid capacity input")

    #this is a getter function for size
    @property
    def size(self):
        return self._size

    #this is a setter function for size
    @size.setter
    def size(self, size):
        if size <= self.capacity and size >= 0:
            self._size = size
        else:
            raise ValueError("incorrect value for size")
