class CustomException(Exception):
    """Custom exception for demonstration purposes."""


def handle_exceptions():
    try:
        # ZeroDivisionError
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    
    try:
        # IndexError
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError:
        print("Error: Index out of range.")

    try:
        # TypeError
        num = 10
        print(num + "5")
    except TypeError:
        print("Error: Unsupported operand type(s) for +: 'int' and 'str'.")

    try:
        # FileNotFoundError
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: File not found.")
    
    try:
        # KeyError
        my_dict = {"a": 1, "b": 2}
        print(my_dict["c"])
    except KeyError:
        print("Error: Key not found in dictionary.")

    try:
        # ValueError
        num = int("hello")
    except ValueError:
        print("Error: Invalid literal for int() with base 10: 'hello'.")

    try:
        # AttributeError
        class MyClass:
            pass
        obj = MyClass()
        print(obj.attribute)
    except AttributeError:
        print("Error: Object has no attribute 'attribute'.")

    try:
        # NameError
        print(undefined_variable) # type: ignore
    except NameError:
        print("Error: Name 'undefined_variable' is not defined.")

    try:
        # TypeError
        numbers = [1, 2, 3]
        print(numbers + 5)
    except TypeError:
        print("Error: Unsupported operand type(s) for +: 'list' and 'int'.")

    try:
        # ValueError
        age = int("twenty")
    except ValueError:
        print("Error: Invalid literal for int() with base 10: 'twenty'.")


        #USER DEFINED EXCEPTION
    try:
        # CustomException
        raise CustomException("This is a custom exception.")
    except CustomException as e:
        print("Custom Exception:", e)

if __name__ == "__main__":
    handle_exceptions()
