from abc import ABC, abstractmethod
from typing import Any
from math import sqrt, ceil


class Rule(ABC):

    @abstractmethod
    def passed(self, value: Any) -> bool:
        pass


class IsNumber(Rule):

    def passed(self, value: Any) -> bool:
        return isinstance(value, int)


class BiggerThenZero(Rule):

    def passed(self, value: Any) -> bool:
        try:
            if value <= 0:
                return False
        except TypeError as t_err:
            print('You entered {}'.format(t_err) + ' '
                  + 'Please enter an integer '
                    'digit bigger then 0')


class Gate(Rule):

    def __init__(self, *rules: Any):
        self._checks = rules

    def passed(self, value: Any):
        passed = True
        for rule in self._checks:
            if not rule.passed(value):
                print(f'{rule.__class__.__name__} is failed')
                passed = False
            return passed


class Input(ABC):

    @abstractmethod
    def value(self) -> bool:
        pass


class AskInput(Input):

    def __init__(self, prompt: str):
        self._q = prompt

    def value(self) -> Any:
        try:
            input_value = input(self._q + '\n')
            return input_value
        except ValueError as v_err:
            print('You entered {}'.format(v_err) + ' '
                  + 'Please enter an integer '
                    'digit bigger then 0')


class IntInput(Input):

    def __init__(self, origin: Input):
        self._origin = origin

    def value(self):
        try:
            input_value = int(self._origin.value())
            return input_value
        except ValueError as v_err:
            print('You entered {}'.format(v_err) + ' '
                  + 'Please enter an integer '
                    'digit bigger then 0')


class Sequence:

    def __init__(self, sequence_length: Any, our_number: Any):
        self._sequence_length = sequence_length
        self._our_number = our_number
        self._our_sequence = list()

    def _sqrt_number(self) -> int:
        try:
            sqrt_number = ceil(sqrt(self._our_number))
            return sqrt_number
        except (TypeError, ValueError):
            print('Please enter and integer digit bigger then 0')

    def _calculate_sequence(self):
        sqrt_number = self._sqrt_number()
        try:
            for _ in range(self._sequence_length):
                self._our_sequence.append(int(sqrt_number))
                sqrt_number += 1
        except TypeError as t_err:
            print('You entered {}'.format(t_err) + ' '
                  + 'Please enter an integer '
                    'digit bigger then 0')

    def get_sequence(self) -> list:
        if len(self._our_sequence) == 0:
            self._calculate_sequence()
        return self._our_sequence


class ProgramReRunner:

    def selection(self) -> bool:
        user_choice = input('One more time? ')
        if user_choice.lower() in ('y', 'yes'):
            return True
        else:
            print('General sponsor SoftServe')
            return False


if __name__ == '__main__':

    while True:

        our_input = IntInput(AskInput('Enter an integer digit'))
        our_sequence_length = our_input.value()
        our_sqrt_number = our_input.value()
        gate = Gate(
            IsNumber(),
            BiggerThenZero())
        gate_sequence_length = gate.passed(our_sequence_length)
        gate_sequence_number = gate.passed(our_sqrt_number)

        if gate_sequence_length and gate_sequence_number:
            print(
                (Sequence
                 (our_sequence_length,
                  our_sqrt_number)
                 ).get_sequence()
            )
        if not ProgramReRunner().selection():
            break
