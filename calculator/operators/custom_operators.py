from .operator import Operator, GroupingOperator

class SumOpertator(Operator):
    def __init__(self, members = []) -> None:
        self.pointers = ['+']
        self.members = members
        self.require_member = 2
        super().__init__()

    def add_members(self, members):
        return super().add_members(members=members)
    
    def calculate(self):
        if self.check_members():
            return self.members[0] + self.members[1]

class MineOpertator(Operator):
    def __init__(self, members = []) -> None:
        self.pointers = ['-']
        self.members = members
        self.require_member = 2
        super().__init__()

    def add_members(self, members):
        return super().add_members(members=members)
    
    def calculate(self):
        if self.check_members():
            return self.members[0] - self.members[1]

class MultiplyOpertator(Operator):
    def __init__(self, members = []) -> None:
        self.pointers = ['*', 'to']
        self.members = members
        self.require_member = 2
        super().__init__()

    def add_members(self, members):
        return super().add_members(members=members)
    
    def calculate(self):
        if self.check_members():
            return self.members[0] * self.members[1]

class DivisionOpertator(Operator):
    def __init__(self, members = []) -> None:
        self.pointers = ['/']
        self.members = members
        self.require_member = 2
        super().__init__()

    def add_members(self, members):
        return super().add_members(members=members)
    
    def calculate(self):
        if self.check_members():
            return self.members[0] / self.members[1]

class PowerOpertator(Operator):
    def __init__(self, members = []) -> None:
        self.pointers = ['**', 'to_power']
        self.members = members
        self.require_member = 2
        super().__init__()

    def add_members(self, members):
        return super().add_members(members=members)
    
    def calculate(self):
        if self.check_members():
            return self.members[0] ** self.members[1]

class RoundDivisionOpertator(Operator):
    def __init__(self, members = []) -> None:
        self.pointers = ['//']
        self.members = members
        self.require_member = 2
        super().__init__()

    def add_members(self, members):
        return super().add_members(members=members)
    
    def calculate(self):
        if self.check_members():
            return self.members[0] // self.members[1]

class RemainOpertator(Operator):
    def __init__(self, members = []) -> None:
        self.pointers = ['%']
        self.members = members
        self.require_member = 2
        super().__init__()

    def add_members(self, members):
        return super().add_members(members=members)
    
    def calculate(self):
        if self.check_members():
            return self.members[0] % self.members[1]

class ParantezOpertator(GroupingOperator):
    def __init__(self, calculator, members = []) -> None:
        self.pointers = ['(']
        self.members = members
        self.require_member = 1
        self.__calculator = calculator
        super().__init__()

    def add_members(self, members):
        return super().add_members(members=members)
    
    def check_members(self):
        if self.members.__len__() < self.require_member:
            raise TypeError(f"Need at least {self.require_member} members")

        if not isinstance(self.members, str):
            raise TypeError("Bad formated!")

        return True

    def calculate(self):
        if self.check_members():
            return self.__calculator.direct_calculate(self.members)

    def set_members(self, index, text:list):
        end_index = text.index(')', index)

        self.add_members(''.join(text[index + 1:end_index]))
        return index, end_index

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