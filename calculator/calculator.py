from typing import List
from .operators.operator import Operator, GroupingOperator
from .operators.custom_operators import (
    SumOpertator,
    MineOpertator, 
    DivisionOpertator, 
    RandOpertator, 
    PowerOpertator,
    MultiplyOpertator, 
    RoundDivisionOpertator,
    ParantezOpertator, 
    RemainOpertator
)


class Solver:
    """ Main class which solve the pharse usin operators
    """

    def __init__(self, operators) -> None:
        """ OPERATORS SOULD LISTED BY THEIR PRIORITY eg: Power > Multiply > Sum
        """
        self.__operators: List[Operator] = operators

    @staticmethod
    def text_to_list(text: str):
        if isinstance(text, list):
            return text
        groups = {
            'numbers': ['1','2','3','4','5','6','7','8','9','0','.'],
            'alefba': [
                'a','b','c','d','e','f',
                'g','h','i','j','k','l',
                'm','n','o','p','q','r',
                's','t','u','w','v','y',
                'x','y','z', '(', '['
            ],
            'operators': [
                '*','!','~','@','#','$',
                '%','^','&','+','_','=',
                '/','<','>'
            ]
        }

        catcher = {
            'on': False,
            'words': '',
            'group': ''
        }

        result = []
        for x in text:
            if catcher['on']:
                if x in groups[catcher['group']]:
                    catcher['words'] += x
                    continue
                else:
                    result.append(catcher['words'])
                    catcher['on'] = False
            for a in groups:
                if x in groups[a]:
                    catcher['on'] = True
                    catcher['words'] = x
                    catcher['group'] = a
                    break
            if not catcher['on']:
                result.append(x)
        if catcher['on']:
            result.append(catcher['words'])
        return result

    def parse(self, text):
        """ Parsing the text into list of chars group, and do the math
        """

        text = Solver.text_to_list(text)
        text = [x for x in text if x != ' ']
        if text.__len__() == 1:
            return text[0]

        # Need Rework
        for word in text:
            if word.isdigit() or word in [',', ')']:
                continue

            if not any(op for op in self.__operators if word in op.pointers):
                raise ValueError(f'Operator "{word}" not found!')

        for op in self.__operators:
            to_loop = list(reversed(text)) if isinstance(op, GroupingOperator) else text

            for i, w in enumerate(to_loop):
                if w.isdigit():
                    continue

                if w in op.pointers:
                    to_i = len(text) - i - 1 if isinstance(op, GroupingOperator) else i
                    s, e = op.set_members(to_i, text)
                    calc = op.calculate()
                    text[s:e + 1] = [str(calc)]
                    if len(text) == 1:
                        return calc
                    else:
                        return self.parse(text) 


class Calculator:
    """ Something like interface class
    """
    def __init__(self, solver = None) -> None:
        if not solver:
            # See how operators are ordred by operation priority
            self.solver = Solver(
                [
                    RandOpertator(),
                    ParantezOpertator(self),   # 0
                    PowerOpertator(),          # 1
                    MultiplyOpertator(),       # 2
                    DivisionOpertator(),       # 3
                    RoundDivisionOpertator(),  # 4
                    RemainOpertator(),         # 5
                    SumOpertator(),            # 6
                    MineOpertator()            # 7
                ]
            )
        else:
            self.solver = solver
        self.__result = []

    def calculate(self, text) -> None:
        self.__result.append(
            {
                'pharse': text,
                'result': self.solver.parse(text)
            }
        )

    def direct_calculate(self, text):
        result = self.solver.parse(text)
        self.__result.append(
            {
                'pharse': text,
                'result': result
            }
        )
        
        return result

    @property
    def show_results(self):
        text = "Results:\n"
        for i, x in enumerate(self.__result):
            text += f"{i + 1}: {x['pharse']} = {x['result']}\n"
        return text

    def clear(self):
        self.__result = []

    def get_result(self, index):
        return self.__result[index]


    
