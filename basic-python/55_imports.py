"""
Why module needed:
* Large codes needs to break into multiple functions or classes, even in multiple files
* each file can group similar or related functionality (each file here is called module)
* When multiple modules are grouped together (to full fill a single purpose), we call it a Package


Python has tons of built-in modules and packages (standard library)
* They are available (in disk as file) to use in any python code but we need to import them first.
These module code is not loaded into memory yet until we import them (increase load time consume memory).
So we need to load a small portion of it (whatever we needed to load).

Look at the standard library documentation from Python (tons of built-in things, as well as modules and packages):
https://docs.python.org/3/library/index.html
* More generic tools/functions/classes


3rd party libraries https://pypi.org/:
* Tons of packages (As of Jan 2024, there are 500K packages)
* Need to install first (use pip install)

How to find the good ones:
* See which ones are popular: mentioned in the books, posts, blogs, web sites
* Good documentation
* Actively maintained, bug fixed, release new version regularly

Avoid using junky packages: not secured, tons of bugs and not maintained properly.
So dont make a junky package as your application dependency.


Modules are in-fact objects in python (in python everything is object)
import math as mm // mm is the reference (variable) to math module

Only using 'import math' is equivalent to 'import math as math'
Use dot notation to access all the attributes of that module.


Import actually does following:
1. Find the location of the file in the disk
2. it loads it up and compiles it
3. Puts it into the memory somewhere and gives us a reference (suppose 'math' as example)


"""

import math  # cmath handles complex number as well

print(type(math), math)
# help(math.sqrt)
print(math.sqrt(16), math.factorial(5), math.pi)

from math import factorial, pi, sqrt

# Note: still loading the whole module (Some people thing its saving loading the whole math module, and only loading the sqrt function).
print(sqrt(16), factorial(5), pi)

# Some important built-in modules
