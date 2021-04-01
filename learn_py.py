# # # # # # # # # xs = [3, 1, 2]   # Create a list
# # # # # # # # # print (xs, xs[2])  # Prints "[3, 1, 2] 2"
# # # # # # # # # print (xs[-1] )    # Negative indices count from the end of the list; prints "2"
# # # # # # # # # xs[2] = 'foo'    # Lists can contain elements of different types
# # # # # # # # # print (xs   )      # Prints "[3, 1, 'foo']"
# # # # # # # # # xs.append('bar') # Add a new element to the end of the list
# # # # # # # # # print (xs )        # Prints 
# # # # # # # # # x = xs.pop()     # Remove and return the last element of the list
# # # # # # # # # print (x, xs )     # Prints "bar [3, 1, 'foo']"
# # # # # # # # animals = ['cat', 'dog', 'monkey']
# # # # # # # # for animal in animals:
# # # # # # # #     print (animal)
# # # # # # # # # Prints "cat", "dog", "monkey", each on its own line.
# # # # # # # nums = [0, 1, 2, 3, 4]
# # # # # # # squares = [x ** 2 for x in nums]
# # # # # # # print (squares)  # Prints [0, 1, 4, 9, 16]
# # # # # # # nums = [0, 1, 2, 3, 4]
# # # # # # # even_squares = [x ** 2 for x in nums if x % 2 == 0]
# # # # # # # print (even_squares  )# Prints "[0, 4, 16]"
# # # # # # d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
# # # # # # print d['cat']       # Get an entry from a dictionary; prints "cute"
# # # # # # print 'cat' in d     # Check if a dictionary has a given key; prints "True"
# # # # # # d['fish'] = 'wet'    # Set an entry in a dictionary
# # # # # # print d['fish']      # Prints "wet"
# # # # # # # print d['monkey']  # KeyError: 'monkey' not a key of d
# # # # # # print d.get('monkey', 'N/A')  # Get an element with a default; prints "N/A"
# # # # # # print d.get('fish', 'N/A')    # Get an element with a default; prints "wet"
# # # # # # del d['fish']        # Remove an element from a dictionary
# # # # # # print d.get('fish', 'N/A') # "fish" is no longer a key; prints "N/A"
# # # # # # animals = {'cat', 'dog'}
# # # # # # print 'cat' in animals   # Check if an element is in a set; prints "True"
# # # # # # print 'fish' in animals  # prints "False"
# # # # # # animals.add('fish')      # Add an element to a set
# # # # # # print 'fish' in animals  # Prints "True"
# # # # # # print len(animals)       # Number of elements in a set; prints "3"
# # # # # # animals.add('cat')       # Adding an element that is already in the set does nothing
# # # # # # print len(animals)       # Prints "3"
# # # # # # animals.remove('cat')    # Remove an element from a set
# # # # # # print len(animals)       # Prints "2"
# # # # # animals = {'cat', 'dog', 'fish'}
# # # # # for idx, animal in enumerate(animals):
# # # # #     print '#%d: %s' % (idx + 1, animal)
# # # # # # Prints "#1: fish", "#2: dog", "#3: cat"
# # # # d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
# # # # print d
# # # # t = (5, 6)       # Create a tuple
# # # # print type(t)    # Prints "<type 'tuple'>"
# # # # print d[t]       # Prints "5"
# # # # print d[(1, 2)]  # Prints "1"
# # # def sign(x):
# # #     if x > 0:
# # #         return 'positive'
# # #     elif x < 0:
# # #         return 'negative'
# # #     else:
# # #         return 'zero'

# # # for x in [-1, 0, 1]:
# # #     print sign(x)
# # # # Prints "negative", "zero", "positive"
# # def hello(name, loud=False):
# #     if loud:
# #         print 'HELLO, %s' % name.upper()
# #     else:
# #         print 'Hello, %s!' % name

# # hello('Bob') # Prints "Hello, Bob"
# # hello('Fred', loud=True)  # Prints "HELLO, FRED!"
# class Greeter(object):

#     # Constructor
#     def __init__(self, name):
#         self.name = name  # Create an instance variable

#     # Instance method
#     def greet(self, loud=False):
#         if loud:
#             print 'HELLO, %s!' % self.name.upper()
#         else:
#             print 'Hello, %s' % self.name

# g = Greeter('Fred')  # Construct an instance of the Greeter class
# g.greet()            # Call an instance method; prints "Hello, Fred"
# g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"