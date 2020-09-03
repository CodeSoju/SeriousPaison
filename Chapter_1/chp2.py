'''
CHAPTER 2: MODULES, LIBRARIES, AND FRAMEWORKS
------------------------------------------------

The Import System:
    To use modules and libs in your program, you have to import them using the 'import' keyword. 
    The import keyword is actually a wrapper around a cuntion names __import__. Here is a familiar way
    of importing a module:
        import itertools
        itertools

    This is equivalent to this method:
        itertools = __import__("itertools")
        itertools

    You can also imitate the 'as' keyword of import, as these 2 equivalent ways of importing show:
        import itertools as it
        it 
        output: <module 'itertools' from '/usr/.../>

While import is a keyword in Python, interanlly it's a simple function that's accessible through the __import__ name. 
The __import__ function is extremely useful to know. 

THE SYS MODULE:
----------------
The sys module provides access to variables and function related to Python itself and the OS it is running on. 
You can retrieve the list of modules currently imported using the sys.modules variable. The sys.module
variable is a dictionary whose key is the module name you want to inspect and whose returned value is 
the module object. 

import sys
import os
sys.modules['os']
>>> <module 'os' from '/usr/lib/python2.7/os.pyc/'>

The sys.module variable is a standard Python dictionary that contains all loaded modules. 
You cna also retrieve the list of modules that are built in by using the sys.builtin_module_names
variable. The built-in modules compiled to your interpreter can vary depending on what compilation options
were passed to the Python build system. 

IMPORT PATHS:
When importing modules, Python reies on a list of paths to know where to look for the module. This list is sorted in the sys.path variable. To check
which paths your interpreter will search for modules, just enter sys.path. 

You can modify the list by adding/removing paths or even change the PYTHONPATH environment variable. 
Adding paths to the sys.path variable can be useful if you want to install Python modules to nonstandard locations, such as a
test environment. 

import sys
sys.path.append('/foo/bar')

This would be the same as:
$ PYTHONPATH=/foo/bar python
import sys
'/foo/bar' in sys.path
>>> True

CUSTOM IMPORTERS:
-----------------
This is the technique that the Lisp-Python dialect Hy uses to teach Python how to import files other 
than standard .py or .pyc files (Hy is a Lisp implementation on top of Python, discussed later in the section)

The import hook mechanism: allows you to extend the standard import mechanism, which in turn allows
you to  modify how Python imports modules and build your own system of import. 

Python offers 2 different but related ways to broaden the import system: the meta path finders for use with sys.meta_path
and the path entry finders for use with sys.path_hooks. 

Meta Path Finders:
    IT's an object that will allow you to load custom objects as well as standard .py files. A MPF object must expose
    a find_module(fullname, path=None) method that returns a loader object. The loader object must also have a load_module(fullname) method
    responsible for loading the module from a source file. 

class MetaImporter(object):
    def find_on_path(self, fullname):
        fls = ["%s/__init__.hy", "%s.hy"]
        dirpath = "/".join(fullname.split("."))

        for pth in sys.path:
            pth = os.path.abspath(pth)
            for fp in fls:
                composed_path = fp %("%s/%s" % (pth, dirpath))
                if os.path.exists(composed_path):
                    return composed_path
    
    def find_module(self, fullname, path= None):
        path = self.find_on_path(fullname)
        if path:
            return MetaLoader(path)

sys.meta_path.append(MetaImporter())

Once Python has determined that the path is valid and that it points to a module, a MetaLoader
object is returned

class MetaLoader(object):
    def __init__(Self, path):
        self.path = path
    
    def is_package(self fullname):
        dirpath = "/".join(fullname.split("."))
        for pth in sys.path:
            pth = os.path.abspath(pth)
            composed_path = "%s/%s/__init__.hy"%(pth, dirpth)
            if os.path.exists(composed_path):
                return True
            return False
    
    def load_module(self, fullname):
        if fullname in sys.modules:
            return sys.module[fullname]
        
        if not self.path:
            return
        
        sys.modules[fullname] = None
        mod = import_file_to_module(fullname, self.path)

        ispkg = self.is_package(fullname)

        mod.__file__ = self.path
        mod.__loader__ = self
        mod.__name__ = fullname

        if ispkg:
            mod.__path__ = []
            mod.__paclage__ = fullname
        else:
            mod.__package__ = fullname.rpartition('.)[0]

        sys.modules[fullname] = mod
        return mod

    The External Lib Safety Checklist:
    ====================================
    Python3 compatibility
    Active Development
    Active Maintenance
    Packaged with OS distributions
    API compatibility commitment
    License

PROTECTING YOUR CODE WITH AN API WRAPPER:
----------------------------------------
No matter how useful an external library might be, be wary of letting it get its hooks into your
source code. Otherwise, if something goes wrong and you need to switch libs, you might have to rewrite
huge swaths of your program. A better idea is to write your own API-- a wrapper that encapsulates your external
libs and keeps them out of your source code. Your program never has to know what external libs it's using, 
only what functionality your API provides. Then, if you need to use a different lib, all you need to 
change is your wrapper. As long as the new lib provides the same functionality, you won't have to touch 
the rest of your codebase at all. 


PACKAGE INSTALLATION: gETTING MORE FROM pip:
---------------------------------------------
The pip project offers a really simple way to handle package and external lib installations. It is
actively developed, well maintains, and included w/ Python starting at version 3.4. It can install or 
uninstall packages from the Python Packaging Index (PyPI), a tarball, or a wheel archive. 

'pip install' can install any package. You can also provide a --user option that makes pip install
the package in your home directory. This avoids polluting your OS directories with package installed system-wide. 

You can list the packages you already have installed using the 'pip freeze' command, like so: 
    pip freeze

One useful feature of pip is its ability to install a package w/o copying the package's file. Typical case
is when you're actively working on a package and want to avoid the long and boring process of reinstalling
it each time you need to test a change. This can be achieved by using the -e <directory> flag:
    pip install -e .

Here, pip does not copy the files from the local source directory but places a special fule, called an egg-link, in your 
distrubtion path:
    cat /usr/local/lib/python2.7/site-packages/daiquiri.egg-link

    The 'egg-link' file contains the path to add to sys.path to look for packages. 
The result can be easily checked by running the follwowing command:
    python -c "import sys; print('/Users/jd/Source/daiquiri' in sys.path)"
>> True

USING AND CHOOSING FRAMEWORKS:
---------------------------
The main difference between frameworks and external libraries is that applications use frameworks
by building on top of them: your code will extend the framework rather than vice versa. Unlike a lib, 
which is basically an add-on you can bring in to give your code some extra oomph, a framwork forms the chassis of your code:
everything you do builds on that chassis in some way. 

There are plenty of upsides to using frameworks, such as rapid prototyping and development, but there 
are also some noteworthy downsides, such as lock-in. 

The less a framwork tries to do for you, the fewer problems you'll have with it in the future. However, 
each feature a framework lacks is another problem for you to solve, either by writing your own code or going
through the hassle of handpicking another lib to handle it. 

Useful modules from the Standard Lib:
    abc module --> used to define the APIs for dynamically loaded extensions as abstract base classes, to
    help extension authors understand which methods of the API are required and which are optional. 
    Abstract base classes are built into some other OOP languages

Advice for people planning to design their own python libs?
    Design libs and APIs from the top down applying design criteria such as the Single Responsiblity Principle
    (SRP) at each layer)

'''