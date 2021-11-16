# learn-Python

## Python

- Python is a interpreted hight-level general-purpose programming language.
- Python is a hight level, cross platform language.
- Have huge community and large ecosystem(libraries, frameworks and tools).
- Python v-2 is the legacy version of Python.

## how to download and install ?

- Goto https://www.Python.org/
- Goto download and download latest version of Python.
- `sudo apt install Python3.8(version)`
- You can check version of Python installed by using `Python --version`.

### Python extension features

- Linting: Which basically means analyzing our code for potential errors.
- Debugging: Which involvs finding and fixing errors.
- Auto completion
- Code formating
- Unit testing: Writing a bunch of code for testing codes.
- Code snippets

## Python implementations

- Python language and Python particular implementation Python
- Python is a language: is a set of rules and grammer for writing Python code.
- A Python implementation: is basically a program that understands those rules and can execute Python code.
- Python implementations examples:

  - Jython(writtern in java)
  - IronPython(writtern in c#)
  - PyPy(subset of Python itself)
  - CPython is the default implementation.

  ## Python variables

  - Integers, floats, boolean and strings are the common build-in types in Python.
  - Use all letters are lowercase and using underscore as separator.
  - Boolean type values first letter are uppercase.
  - In string type you can cover strings with `single quotes(')`, `double quotes(")`, and `tripple quotes(""")`- for mutli-line.
  - In Python you can initialize multiple variables in same line.
  - Build in premitive types are immutable(which means their value cannot change). Here if we try to update value of x,
    python interpreter is going to allocate some new memory to store the updated value. But x is originally referencing the intitial location.

  ## Dynamic typing

  - Static languages: In static languages you need to specify type of the variable when we declaring a variable.
    In static languages type of a variable is always same. Eg. c++, c#, java.
  - Dynamic languages: In dynamic variables the type of a variable is determine at runtime as opposed to compile time. Eg. javascript, ruby, python.

  ## Strings

  - There are some escape sequences in python

    - `\"`
    - `\'`
    - `\\`
    - `\n`

    ## Numbers

    - `0b` helps to convert a binary number to decimal. eg: `0b10 = 2`, `0b1011 = 11`
    - bin() helps to get binary representation of a number.
    - `0x` helps to convert a hexa decimal number to decimal. eg: `0x12c = 300`
    - `hex()` helps to get hexadecimal representation of a number.
    - Python don't have increament operator.
    - Uppercase indicate the variable is a constant variable.
    - Python 3 built in functions : https://docs.python.org/3/library/functions.html

    ## Type conversion

    - `Input()` helps to get input from the terminal.
    - Python language doesn't know how to do type conversion.
    - Python is strongly typed language.
    - type conversion functions: `int()`, `float()`, `bool()`, `str()`;

    - falsy values: `"", 0, [], none(null)`

    ## conditional statements

    - In python language use indent for scoping.
    - syntax:

      ```
      if <Contition-1>:
        statement-1
      elif <Contition-2>:
        statement-2
      else:
        statement-3
      ```

  ## Logical operators

  - ADN, OR, NOT
  - string.strip() method helps to strip the white spaces

  ## Ternary operator

  - syntax: `<staement-block-1> if <contition> else <statement-block-2>`

  ## Loops in python

  - There are two types of loops in python: for loops and while loops.
  - range function take small amount of memory.
    - Keyword arguments helps to the code is more readable.

  ## Arguments

  - add an astrics(\*) before an argument then python will see that parameter as topple.

  -> In python arrays are called topple and objects are called dictionary.

  ## Variable scope

  - In python there are two type of variables: local variable with function scope and global variable with file scope.
