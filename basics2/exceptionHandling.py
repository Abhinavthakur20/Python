# error handling 

a=10
b=0 
# ans = n/m
# print(ans)

try:
    ans = a/b
    print(ans)
except ZeroDivisionError:
    print("Error: Division by zero")



# try: Runs the risky code that might cause an error.
# except: Catches and handles the error if one occurs.
# else: Executes only if no exception occurs in try.
# finally: Runs regardless of what happens useful for cleanup tasks like closing files.

try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")








try:
    # x = int("25")
    x = int("str")  # This will cause ValueError
    inv = 1 / x   # Inverse calculation
    
except ValueError:
    print("Not Valid!")
    
except ZeroDivisionError:
    print("Zero has no inverse!")
else:
    print("complete")







a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
    
except (ValueError, TypeError) as e:
    print("Error", e)
    
except IndexError:
    print("Index out of range.")







try:
    res = "100" / 20 # Risky operation: dividing string by number
    
except ArithmeticError:
    print("Arithmetic problem.")
    
except:
    print("Something went wrong!")











def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)