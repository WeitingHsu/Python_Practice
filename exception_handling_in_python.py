'''
Errors :
1. compile time 
eg: missing(:) wrong spelling
2. logical
eg : wrong output -> 2+3 = 4
3. run time (mistake done by user)
eg : divided by zero    


'''

a = 2
b = 5

try:
    print("resource is open")
    print(a/b)
    k = int(input("input a number"))
    print(k)
#   print("resouce is closed") This line will not be executed once the error happen, so we have to use finally to prevent this situaiton
# except block, execute only when you have error

# giving a specified error name so that excep can distinguish what kind of error it recieves so that it won't be misassigned by other error
except ZeroDivisionError as e:
    print("You cannot divide a number by zero",e)

except ValueError as e:
    print("Invalid input",e)

# Final exception to recieve error we don't know
except Exception as e:
    print("Sth went wrong....")

# finally is not affected even if your exception is executed or not
finally:
    print("resouce is closed")

print("Bye")