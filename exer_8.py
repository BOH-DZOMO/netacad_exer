try :     
    def safe_divide(a, b):
        return a/b
except ZeroDivisionError:
    raise ZeroDivisionError
except:
    raise
test = True
while test:
    try:
    
        a = int(input("enter numerator: "))
        b = int(input("enter denominator: "))
        output = safe_divide(a,b)
        print("Result: ", output)
        test = False
        
    except ZeroDivisionError:
        print("You entered 0 as a divisor")
    except:
        print("Enter a valid number")
else:
    print("No error occured")
print("Operation complete")