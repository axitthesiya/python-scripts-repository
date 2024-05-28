# Advance Topics in Python

**Reference:** [Python Modules](https://docs.python.org/3/tutorial/modules.html)

## Topics
- Decorators
- Generators and Iterators
- Context Managers
- Metaclasses
- Descriptors
- Coroutines and Asyncio
- Dynamic Code Execution
- Memory Management
- Concurrency with Threading and Multiprocessing
- Custom Containers
- Type Hinting and Annotations
- Metaprogramming

---

### 1. Decorators
--> Decorators allow you to modify or extend the behavior of functions or methods without changing their actual code.

**Example:**
```python
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")
```
# Output: I got decorated ->  I am ordinary


### 2. Generators and Iterators
--> A generator is a function that returns an iterator. Iterators are objects that can be iterated over, meaning that you can loop through them. Generators are created using the yield keyword.
When a generator is called, it returns an iterator object.An iterator is an object that contains a countable number of values.

**Example:**
```python
# Generator function
def my_generator():
    for i in range(10):
        yield i

# Iterator object
my_iterator = my_generator()

# Iterate over the generator
for i in my_iterator:
    print(i)

# Generator expression
my_generator_expression = (i for i in range(10))

# Iterate over the generator expression
for i in my_generator_expression:
    print(i)
```
# Output: 0 1 2 3 4 5 6 7 8 9 -> 0 1 2 3 4 5 6 7 8 9       


### 3. Context Managers
--> Context managers in Python generate a runtime context. This runtime context is then used to execute a block of code.
The context manager is responsible for ensuring that the runtime context is cleaned up properly, even if an exception occurs.
The context manager must have __enter__() and __exit__() methods.
*--> __enter__() :- The value returned is assigned to VAR. If no as VAR clause is present, the value is simply discarded.**
*--> __exit__()	:-method is called with three arguments, the exception details (type, value, traceback).**

**Example:**
```python
class ContextManager():
    def __init__(self):
        print('init method called')
    
    def __enter__(self):
        print('enter method called')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')

with ContextManager() as manager:
    print('with statement block')
	```
# Output: init method called
#	  enter method called
#     with statement block
#     exit method called

### 4.Metaclasses
--> A metaclass is a class that allows for other classes to be instantiated as objects of the metaclass.

**Example:**
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} with bases {bases}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass```
# Output: Creating class MyClass with bases ()


### 5. Descriptors
-->Python descriptors are a special type of object that allows you to customize the behavior of attributes. They are used to implement properties,
   class methods, static methods, and super().
 *__get__()    : This method is called when an attribute is retrieved.
 *__set__()    : This method is called when an attribute is set.
 *__delete__() : This method is called when an attribute is deleted.

**Example:**
```python
class Descriptor:
    def __init__(self, value=None, name='var'):
        self.val, self.name = value, name

    def __get__(self, obj, objtype):
        print(f'Getting {self.name}: {self.val}')
        return self.val

    def __set__(self, obj, value):
        print(f'Setting {self.name} to {value}')
        self.val = value

    def __delete__(self, obj):
        print(f'Deleting {self.name}')
        del self.val

class MyClass:
    attr = Descriptor(value=10, name='attr')

obj = MyClass()
print(obj.attr)   
obj.attr = 20       
print(obj.attr)   
del obj.attr   ```
# Output: Getting attr: 10
#10
#Setting attr to 20
#Getting attr: 20
#20
#Deleting attr


### 6. Coroutines and Asyncio
--> Coroutines are a special type of function that can be paused and resumed. They are defined using the async def syntax and used with the await keyword. 
The asyncio module provides support for asynchronous programming.

**Example:**
```python
import asyncio
import threading
import time

# Define a blocking function simulating I/O operation
def blocking_io():
    print("Starting blocking I/O")
    time.sleep(2)
    print("Blocking I/O completed")

# Define an asynchronous coroutine
async def async_coroutine():
    print("Starting asynchronous coroutine")
    await asyncio.sleep(1)
    print("Asynchronous coroutine completed")

async def main():
    print("Starting main coroutine")
    blocking_thread = threading.Thread(target=blocking_io)
    blocking_thread.start()

    await async_coroutine()
    print("Main coroutine completed")

asyncio.run(main())```

# Output: Starting main coroutine
# Starting blocking I/O
# Starting asynchronous coroutine
# Asynchronous coroutine completed
# Main coroutine completed
# Blocking I/O completed


### 7. Dynamic Code Execution
--> Dynamic code execution refers to the ability of a program to execute code during runtime that was not present in the program's source code at compile time.
 This is commonly achieved using the exec() function or the eval() function.

**Example:**
```python
code = "print('Hello, world!')"
exec(code)
```
# Output: Hello, world!


### 8. Memory Management
--> Memory management refers to the process of controlling and coordinating the use of computer memory. The memory occupied by an object is deallocated when it 
is no longer needed.

**Example:**
```python
x = 10
y = x
del x
print(y)
```
# Output: 10


### 9. Concurrency with Threading and Multiprocessing
--> Concurrency involves the execution of multiple tasks seemingly simultaneously. In Python, concurrency can be achieved using threading and multiprocessing.
*Threading involves running multiple threads within the same process, allowing them to share the same memory space but execute independently. However, 
*due to the Global Interpreter Lock (GIL) in CPython, threading may not achieve true parallelism in CPU-bound tasks.
*Multiprocessing, on the other hand, involves running multiple processes, each with its own memory space, allowing true parallelism even in CPU-bound tasks.
*Multiprocessing is suitable for tasks that can be easily divided into smaller independent units.

**Example with Threading:**
```python 
import threading

def print_numbers():
    for i in range(5):
        print(i)

def print_letters():
    for letter in 'abcde':
        print(letter)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()```
# Output: 0 1 a b c d 2 e 3 4

## Example with Multiprocessing:
** ------------------------------------------------------------------------------ **
**Example with Multiprocessing:**
```python
from multiprocessing import Process

def square(number):
    result = number * number
    print(f"The square of {number} is {result}")

if __name__ == "__main__":
    processes = []
    numbers = [1, 2, 3, 4, 5]

    for number in numbers:
        process = Process(target=square, args=(number,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
```
# Output:The square of 1 is 1
# The square of 2 is 4
# The square of 3 is 9
# The square of 4 is 16
# The square of 5 is 25


### 10. Type Hinting and Annotations
-->Type hinting and annotations in Python allow developers to specify the expected types of variables, function parameters, and return values.

**Example:**
```python
def add_numbers(x: int, y: int) -> int:
    return x + y

result = add_numbers(5, 3)
print(result)
```

```Description: In this example, the add_numbers function is annotated with type hints. It takes two parameters x and y, both of type int, and returns an int.
 The result variable is assigned the return value of add_numbers, and when printed, it outputs the sum of the two input integers.```

# Output:8


### 11. Metaprogramming
--> Metaprogramming is a programming technique where programs have the ability to treat other programs as their data. In Python, metaprogramming allows you
to write code that manipulates the structure or behavior of other code during runtime.
This modification is done at runtime, allowing for dynamic behavior changes in the program.
metaprogramming is demonstrated by dynamically replacing the greet method of the MyClass class with a new method new_greet.

**Example:**
```python
class MyClass:
    def greet(self):
        print("Hello!")

def new_greet(self):
    print("Bonjour!")

# Dynamically replacing method 'greet' with 'new_greet'
MyClass.greet = new_greet

# Creating an instance of MyClass
obj = MyClass()

# Calling the modified method
obj.greet()
```

# Output: Bonjour!


### 12. Custom Containers
--> Custom containers in Python refer to user-defined data structures that encapsulate and manipulate collections of objects. These containers can be tailored to
 specific needs, providing customized functionality not available in built-in data structures like lists, tuples, or dictionaries.
 
**Example:**
```python
class MyStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Creating a stack instance
stack = MyStack()

# Pushing elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Popping elements from the stack
print(stack.pop())  
print(stack.pop())  

```
#output:
#		3
#		2

																			###  END  ## 