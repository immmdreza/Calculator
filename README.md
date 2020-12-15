# Calculator
A simple calculator class library written in python just for fun!

## How to
Just clone the repo, head to the directory and `(py main.py)`

You can also add your custom operators for the calculator (`See calculator/operators/custome_operator` to see current examples) 

This project can easlly extends as you wish (This is just the simple and base version)

### Example

After you copied Calculator folder into your project, Just create a file like `main.py`, copy-paste code below for quick start:

```python
from calculator import Calculator
from random import choice

if __name__ == "__main__":
    # Show time
    c = Calculator()
    print(c.direct_calculate("2*(10+5)")) 
```

Here is a example of a custom operator that takes two number and returns a random number between them

```python
class RandOpertator(GroupingOperator):
    def __init__(self, members = []) -> None:
        self.pointers = ['rand(']
        self.members = members
        self.require_member = 2
        super().__init__()

    def add_members(self, members):
        return super().add_members(members=members)

    def calculate(self):
        if self.check_members():
            import random
            return random.randint(self.members[0], self.members[1])

    def set_members(self, index, text:list):
        end_index = text.index(')', index)

        members = ''.join(text[index + 1:end_index]).split(',')
        self.add_members([int(members[0]), int(members[1])])
        return index, end_index
```

Please take a look in Operator abstract class and other operators to find out whats happend!
