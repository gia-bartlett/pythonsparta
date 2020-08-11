ENCAPSULATION:  
One of the four pillars of OOP  
Restricts access to methods and variables.  
This prevents data from direct modification.  
In Python, we denote protected and private attributes using underscore as the prefix i.e single _ or double __ (dunder).  
```
class Child(Parent):
    def __init__(self, a, b, c):
        self.a = a  (public)
        self._b = b  (protected)
        self.__c = c  (private)        
```
Public (default. no prefix):  
* Accessible from outside the class.  
* The object of the same class is required to invoke a public method.  

Protected (_ prefix):  
* Accessible from within the class and are also available to its sub-classes.  
* No other environment is permitted access to it.  
* This enables specific resources of the parent class to be inherited by the child class.  

Private (__ prefix):  
* Private members of a class are denied access from the environment outside the class.  
* They can be handled only from within the class.  
* Gives a strong suggestion not to touch it from outside the class.  
* Any attempt to do so will result in an AttributeError.  

My example:  
created a class Apples  
These apples have a set maximum purchase price and minimum sale price (to maximise profit)  
The maximum and minimum prices are set using dunder so that they can't be accidentally changed.    
If we want to change the prices we must use the setter function to set the new price  

ABSTRACTION:  
One of the four pillars of OOP  

Abstraction means hiding the complexity and only showing the essential features of the object.  
Achieved by using abstract classes and interfaces.  
An abstract class is a class that generally provides incomplete functionality and contains one or more abstract methods.  
Abstract methods are the methods that generally don’t have any implementation,  
It is left to the sub classes to provide implementation for the abstract methods.  

My example:  
Created a class Payment (which handles the main payment method)  
Set up 3 functions EPay (free), CreditCard (5% surcharge) and DebitCard (£1 fee)  
They are imported to Payment and are implemented behind the scenes when Payment is invoked.  

POLYMORPHISM:  
One of the four pillars of OOP  
 
The literal meaning of polymorphism is the condition of occurrence in different forms.  
Polymorphism is a very important concept in programming:  
It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.  
Polymorphism in Operators:  
```
print(1 + 2) = 3
print("num" + "ber") = number
print("O"*2 + "P") = OOP
```
Operators are polymorphic as they do not have a single usage:  
They can be used for simple arithmetic operations  
They can be used for string concatenation  
etc.  

Polymorphism in Functions:
```
print(len("Hello World!")) = 12
print(len(["Python", "Java", "SQL"])) = 3
print(len({"Name": "Georgina", "Address": "Osaka"})) = 2
```  
Some functions are polymorphic and can run with multiple data types:  
The len() function can be used on many data types in Python including (but not limited to):  
strings (length of string), lists (number of items), dictionaries (number of keys)  

Polymorphism in Classes:  
Python allows different classes to have methods with the same name.  
We can then later generalize calling these methods by disregarding the object we are working with.  

My example:  
Four separate classes (Human, Dog, Cat, Bird)  
All classes will have a name and age provided in the init.  
All classes will have a method to introduce themselves (intro()).  
All classes will have a method to show off their unique noise (make_noise()).   
The methods intro() and make_noise() are reused for each class but produce a unique output for each. 

INHERITANCE:  
One of the four pillars of OOP  
It refers to defining a new class with little or no modification to an existing class.  
The new class is called derived (or child, or sub) class.  
The one from which it inherits is called the base (or parent) class.  

```
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
```
My example:  
Parent class Employee  
All employees will have a first and last name, base pay and email.  
Email calculated from initial variables  
Method included to create Full Name.  
Child class Coders   
Fully inherits from the Employees class  
Coders earn a bonus on top of their base pay based on their coding language.  
repr used to recreate the object if necessary  
str used to output full name, email, and full pay.
