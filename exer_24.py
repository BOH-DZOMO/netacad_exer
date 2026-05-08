def counter_working():
    count = 0
    def click():
        nonlocal count
        # This throws an UnboundLocalError! 
        # Python tries to create a local 'count' but sees you're reading it on the same line.
        count = count + 1 
        return count
    return click


clicker = counter_working()
print(clicker()) 
print(clicker())