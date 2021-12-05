## Python

- Python support all type of programming paradigm.
- Python support functional programming, Object oriented programming, and procedure oriented programming.

# Oops introduction

- Oops ina programming paradigm that uses objects and classes in programming.
- OOP helps to development faster and cheaper, with better software maintainability.
- OOPS uses the concept of objects and classes.
  A class can be thought of as a 'blueprint' for objects. these can have their own attributes and methods.
- Simply, class is a design and object is real stuff.

### Object

- An object will have something that you can store data and an object will have some behaviour.
- If you want to store something in object, you need to declare variables.
- An object is an instance of a class.
- Every objects have certain attributes and every objects have certain behaviour.
- Everytime you create an object it is allocated to new space.
- Size of objects is depends on number of the variables.
- Constructor allocate size to object.

### Methods

- Functions in the object oriented programming called methods.

### How to create a class ?

- To create a class in python You can use `class` keyword, followed by the classname and colon.
- Inside the class, an `__init__` method has to be defined with `def`. This is the initializer that you can later use to instantiate objects.
- `__init__` method take one argument called `self`, which refers to object itself.
- `self` keyword helps to refer the object inside class.

### Type of variables in python

- In oops there are two types of variables: instance variables and class/static variables.
- If you change one instance variable in one object is only changed in that spceific object variables value.
- ```python
    class car:
    wheels = 4
    def __init__(self):
      self.mil = 10
      self.com = "BMW"
  ```
  => In the above example, the variable with name `wheels` is a `class variable`. And the variables named `mil,com` are called `instance variables`.

### Type of methods

- Instance methods
- Class methods
- Static methods

- instances - If you want to just fetch the values of the instance variable we will be using access methods.
- If you want to modify the values you will use mutaters.
- getters and setters
- Getters only get the values or fetch the value thats why called accecers.
- Setter set the values or change the value thats why called mutators.

- Instance variables can be used with instants methods.
- Class variables can be used with class methods.

### Inehritance

- A class using features of existing class.
- One class wll extends from different classes or multiple classes called multiple inheritance.
- subclasses can access all the features of super class.
