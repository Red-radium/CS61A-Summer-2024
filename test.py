def divide(x, y):
    try:
        return x/y
    except ZeroDivisionError as e:
        print("Error: Division by zero is not allowed:",type(e))
        return 0
    # return ans