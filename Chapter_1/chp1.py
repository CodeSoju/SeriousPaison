'''
VERSIONS OF PYTHON
------------------
Each new version of Python introduces new features and deprecates old ones. 

- Verion 3.7 is the most recent version of the Python 3 branch as of this writing (2019)

LAYING OUT YOUR PROJECTS
------------------------
Organize your files. 
Use packages and hierarchy wisely: a deep hierarchy can be a nightmare to navigate, while a flat hierarchy 
tends to become bloated. 
Then avoid making the mistake of storing unit tests outside the packge directory. These tests should be
included in a subpackage of your software so that they aren't automatically  installed as a 
tests top-level module by setuptools ( or som eother packaging library) by accident. By placing
them in a subpackage, you ensure they can be installed and eventually used by other packages
so users can build their own unit tests. 

The standard name for a Python installation script is setup.py. It comes with its own companion
setup.cfg, which should contain the installation script configuration details. When run, 
setup.py will install you package using the Python distribution utilities. 

The docs directory shold contain the package's documentation in reStructuredText format, which
will be consumed by the Sphinx. 

Packages will often have to provide extra data for the software to use, such as images, shell scripts, 
and so forth. Unfortunately, there's no universally accepted standard for where these files shold be 
stored, so you shuld just put them wherever makes the most sense for your project depending on their
functions. 

The following top-level directories also frequently appear:
- etc     -> for sample configuration files
- tools   -> for shell scripts or related tools
- bin     -> for binary scripts you've written that will be installed by setup.py

WHAT NOT TO DO:
----------------
Some devs will create files or modules based on the type of code they will store (NO NO)

Organize your code based on features, not on types. 

It is also a bad idea to create a module directory that contains only an __init__.py file, because
it's unneccessary nesting. For example, you shouldn't create a directory named hooks with a single
file named hooks/__init__.py in it, where hooks.py would have been enough. If you create a directory, it 
should contain several other Python files that belong to the category the directory represents. 

You should be very careful about the code that you put in the __init__.py file. This file will be called
and executed the first time that a module contained in the directory is loaded. 
In fact, __init__.py files should be empty for the most part, unless you know what you are doing. 
Don't try to remove __init__.py files altogether though, or you won't be able to import your Python
module at all.Python required an __init__.py file to be present for the diretory to be considered
a submodule. 

VERSION NUMBERING
------------------
PEP 440 defines the following regular expression for version numbering:
    N[.N]+[{a|b|c|rc}N][.postN][.devN]

This allows for standard numbering such as 1.2 or 1.2.3

CODING STYLE AND AUTOMATED CHECKS
-------------------------------
PEP 8 : Style Guide for Python Code:
    - Use four spaces per indentation level
    - Limit all lines to a maximum of 79 characters
    - Separate top-level function and class definitions with two blank lines. 
    - Encode files using ASCII or UTF-8
    - Use one module import per import statement and per line. Place import statements at the top
    of the file, after comments and docstrings, grouped first by standard, then by third party, and 
    finally by local librayr imports. 
    - Do not use extraneous whitespaces between (), [], {}, or before commas
    - Write class names in camel case,  suffix exceptions with Error (if applicable), and name functions

    If you write C code for Python (e.g. modules), the PEP7 standard describes the coding style that you
    should follow

TOOLS TO CATCH CODING ERRORS:
============================
- Pyflakes: extendable via plugins
- Pylint: checks PEP8 conformance while performing code error checks by default; can be extended via
plugins
To simplify things, Python has a project names flake8 (https://pypi.org/project/flake8/) that
combines pyflakes and pep8 into a single command. 

Some issues with Python(according to a Python dev):
    - Python2 to 3 transition
    - Lambdas are too simplistic and should be made more powerful. 
    - The lack of a decent package installer ( pip needs some work lie a real dependency resolver)
    - the global interpreter lock (GIL) and the need for it. 
    - the lack of native support for multithreading-currently you need the addition of an explicit asyncio model. 
    - the fracturing of the py community: CPython and PyPy (and other variants)
    Cpython: is the reference implementtion of the Python programming lanaguage. Written in C and Python, 
    CPython is the default and most widely used implementation of the language. Can be used as both an 
    intepreter and a compiler as it compiles Python code into bytecode before interpreting it. 

    Just-in-Time compilation (JIT): a feature of the run-time intrepreter that instead of interpreting bytecode every time
    a method is invoked, will compile the BC into the machine code instructions of the running machine and then invke this object code instead.

    Python can also use a strong set of concurrency patters; not just the low level asyncio and threading
    styles of patterns, but higher-level concepts that help make applications that work performantly at larger scale. 
'''

