# Python Project Template

This is a sample repository that I will be using when making Python projects.


___

### Virtual Environments

When creating/starting a new python project, it is always considered best practice to use a virtual environment. Doing so allows you track project dependencies and list them in `requirements.txt`. Doing so will make sharing your project with others (i.e. working collaboratively much easier). Furthermore, it will prevent your main python module folder from getting cluttered.

To create a virtual environment ensure that these files are visible:

```
my_project/  
README.md  
requirements.txt  
test/  
venv/
```

This means we are at the top-level view for this project. The next step is to run the following in the terminal:

``` 
python -m venv venv
```

This creates a virtual environment called 'venv'. 

The next step is to ensure that this virtual environment is activated within the terminal/IDE/editor instance.

To do so run the following in the terminal:

```
./venv/Scripts/activate
```

(*Note: the activation of a venv will vary depending on your OS; I use windows, so the command to use for MacOS/Unix devices will differ slightly).
____

### Folder Structure

This repository has two main folders:

1. `my_project/`

2. `test/`

The `my_project/` folder has a file named `app.py`. This module contains a funtion named `plus_one()` -- it increments a value passed in by one.

_____

### Testing

This project defaults to using the `unittest` package -- as it is part of the standard library for python.

The folder `test/` contains a file named `test_app`.

When writing future tests, all files should be named with the following convention in mind:

```
test_*.py
```

Where the asterix should ideally refer to the name of the package/file that is to be tested.

Before we can run any tests we need to execute the following in the terminal:

```
python -m unittest discover
```

To Run Tests, execute the following in the terminal:

```
python -m unittest
```

The resulting output should look like:

```
.F
======================================================================
FAIL: test_plus_one_fail (test.test_app.appTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\micha\Documents\Code\py_template\test\test_app.py", line 10, in test_plus_one_fail
    assert app.plus_one(1) == -1
AssertionError

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

One of the test cases has been designed to fail intentionally.

___

That should just about cover everything...