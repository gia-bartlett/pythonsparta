TDD:  
Test Driven Development  
https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/  
What it involves:  
* Writing tests that would check the functionality of your code prior to your writing the actual code.  

<img src = "https://cdn-media-1.freecodecamp.org/images/1*FZGakHQbCUMAyDinf-KBiw.png">  

unittest and pytest modules are used  
   
```

```


Reverse engineering - writing the test first (guaranteed to fail)  
Then doing what it says we need to do.  


Calculator example:  
```
import pytest
import unittest
from calc import *  --> calc is the name of our program
class Calc_Test(unittest.TestCase):

    simple_calc = Calc()

    def test_add(self):
        self.assertEqual(self.simple_calc.add(2, 2), 4) --> addition function test (2+2=4)
```  
This will fail because we have not yet created the addition function in Calc  
We will then create our add function in Calc  
```
class Calc:

    def add(self, num1, num2):
        return num1 + num2
print(simple_calc)  # <__main__.Calculator object at 0x00000231C9D17400>
print(simple_calc.add(2, 2))  # 4
```
Then we will run the test again and it should pass.  
Then we will create a new test for subtract and so on  
Test  
Create  
Test  
Create  