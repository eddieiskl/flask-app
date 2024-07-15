try:
    x = 1
finally:
    print("finally")
#Yes, this code is legal. The finally block will always be executed,regardless of whether an exception is raised or not.
# Here, since no exception is raised, it simply prints “finally”.