### Part C

#**Is there a difference between the two lines below? Why?**


name = "john"
name = 'john'


#**Answer:**

#There is no functional difference between using double quotes (`"`) and single quotes (`'`) in Python for defining string literals. Both can be used interchangeably to create strings.

#The choice between single and double quotes is usually a matter of style or convenience. For example:
#- Double quotes (`"`) can be used if the string itself contains a single quote.
#- Single quotes (`'`) can be used if the string itself contains double quotes.

#Here's an example illustrating this:


# Using double quotes to enclose a string with a single quote
message1 = "John's book"

# Using single quotes to enclose a string with double quotes
message2 = 'He said, "Hello!"'

print(message1)
print(message2)


#This flexibility helps avoid the need for escape characters in simple cases, making the code easier to read and write.