## Python

- Python support all type of programming paradigm.
- Python support functional programming, Object oriented programming, and procedure oriented programming.
- Dynamic typing - that means we can mention later for a variable.

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
- To represent super class we use super method.

### polymorphism
- poly - means 'many'
- morph - means 'form'
- polymorphism means one thing can take mutliple forms
- The 4 ways for implementing polymorphism in python, they are;
  1. Duck typing
  2. Operator overloading
  3. Method overloading
  4. Method overriding
#### Duck typing
- Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods its defines. When you use duck typing, you do not check types at all. Instead we check for the presence of a given method or attribute.

#### Operator overloading
- Operator overloading in python is the ability of a single operator to perform morethan one operation based on the class(type) of operands. For example, the + operator can be used to add two numbers, concatenate two strings or merge two lists.
- The operators still same and operends will change


  eg:  a = 5 + 4
        b = 'No' + 'Fun'
        c = { 1: 'haii'} + { 3: 'Hello}
  
  - In the above examples the operends will change in each time but the operater will remin same.

#### Method overloading
- You have same method name and you have different arguments or may be the type of arguments are different.
- Method overloading means, if your class have two methods with same name and different parameters.
- eg:
      `class student:
        def avarage(a, b):

        def avarage(a, b ,c):
      `

- But python dont have method overloading becouse we cannot create two methods with same name.

#### Method overriding
- Method overriding means you have two methods with same name and same number of parameters/or arguments.
- In the case of inheritance we  the different classes have same method with same parameters.
- eg.
      `class A:
        def sum():

       class B(A):
        def sum(): `