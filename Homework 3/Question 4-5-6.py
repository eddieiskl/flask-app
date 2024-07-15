try:
     #some code
     print("Hi")
    pass
except:
    print("An error occurred")
#4.This except block will catch all exceptions, regardless of their type.
#It is equivalent to catching the base class Exception and is generally considered bad practice because it makes debugging difficult and may hide bugs.

#5. What is wrong with using the above type of exception handler?
#Using a bare except can catch unexpected exceptions, making it harder to identify the actual cause of an error. It is better to catch specific exceptions to handle them appropriately and make the code more readable and maintainable.

#6. What exceptions can be caught by the following handlers?
#a. except IOError
#Explanation:

#This handler will catch exceptions related to input/output operations, such as file not found, file read/write errors, etc.

#b. except ZeroDivisionError
#Explanation:

#This handler will catch exceptions raised when attempting to divide a number by zero.
