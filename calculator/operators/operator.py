from abc import ABC
from typing import Any

class Operator(ABC):
    """
    Abstract class for operators, you can create custome operators using it.
    """

    pointers = []
    """A list of chars that point to the operator
    """
    members = []
    """Members which operation gose over them
    """
    require_member = 0
    """Least require member for the operation
    """

    name = ''
    about = ''
    
    def __init__(self) -> None:
        if not self.pointers:
            raise ValueError('pointers required!')

        if self.require_member < 1:
            raise ValueError('require_member Should be more that 0')

    def calculate(self) -> Any:
        """Main func to calculate the result
        """
        pass

    def add_members(self, members = []):
        """Add members to attribute (Not important if field is public)"""

        self.members = members

    def check_members(self):
        """Members should be valid!
        """

        if self.members.__len__() < self.require_member:
            raise TypeError(f"Need at least {self.require_member} members")

        for x in self.members:
            if not (isinstance(x, int) or isinstance(x, float)):
                raise TypeError("Only int and float!")
        
        return True

    def set_members(self, index, text):
        """ The fun that find member on text using operator index
            Retuns the starting and ending index of whole operation 
        """

        member1 = eval(text[index - 1])
        member2 = eval(text[index + 1])

        self.add_members([member1, member2])
        return index - 1, index + 1

    def __str__(self) -> str:
        return f'Operator {self.name} ( {self.about} )'


class GroupingOperator(Operator):
    def __init__(self) -> None:
        super().__init__()

