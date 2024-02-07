note = """
Generally exception means unexpected behavior, not necessarily an error.
This can be something we can expect and handle it properly.
An unhandled exceptions will cause pur program to die/crush/terminate.

Terminology:
Exception -> is an special type of object in python.
Raising -> starting an exception event flow
Exception handling -> interacting with an exception flow in some manner.
Unhandled exception -> an exception flow that is not handled by our code.


Exception Hierarchy:
*   Python exceptions forms a hierarchy
*   The top most base class is 'BaseException'
    Here is the hierarchy: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
*   This hierarchy is based on class inheritance.
*   Top level classes are more broad, whereas bottom levels are more specific.
*   We can catch/handle more broadly or more specifically.
*   We can have custom exception based (inheritance) of a python built-in exception.

List of python built-in exceptions:
https://docs.python.org/3/library/exceptions.html

How to handle unexpected behavior:
* Take action (validate/verify/test) to make sure everything is in place/perfect to prevent exception. (Look before you leap)
* Let the exception happen (no prevention) then handle it (Easier to ask forgiveness than permission)
    - No need to run code for validate/verify/test every time. This means on demand and efficient code.
    - Generally python prefer this (exception handling rather than prevention)
* Also trying to fully determine something is going to go wrong is much harder than handling things on demand.

Exception handling flow:
> an exception occurs
    > an exception object is created
    > an exception flow is started
        1. We do nothing about it, so it terminates the program OR
        2. We intercept the exception flow
            > handle the exception in some sense if possible
                > silence the exception (do nothing) and continue the program
                > or we are not going to deal with it but do logging of that exception, so at least we know it happened
                > or we can start a new exception flow (raise another exception, mostly custom ones)

Raising an exception:
*   start an exception flow by ourself
*   an exception object will be associated with an exception flow
*   We need to create that exception object first, then raise it

"""

print(note)
