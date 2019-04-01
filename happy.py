

def calculate_via_easy(tickets_list: list) ->int:
    tickets_amount = 0
    for digit in tickets_list:
        first_half = int(digit[0]) + int(digit[1]) + int(digit[2])
        second_half = int(digit[3]) + int(digit[4]) + int(digit[5])
        if first_half == second_half:
            tickets_amount += 1
    return tickets_amount


def calculate_via_hard(tickets_list: list) ->int:
    tickets_amount = 0
    for digit in tickets_list:
        even = int(digit[0]) + int(digit[2]) + int(digit[4])
        odd = int(digit[1]) + int(digit[3]) + int(digit[5])
        if even == odd:
            tickets_amount += 1
    return tickets_amount


def ticket_list(start_ticket: int, stop_ticket: int) -> list:
    tickets_output = [str(_).zfill(6) for _ in range(start_ticket, stop_ticket)]
    return tickets_output


def is_valid(six_digit_value: str) -> int:
    flag = True
    while flag:
        try:
            entered_value = int(input(f'Enter {six_digit_value}: '))
            if 0 <= entered_value <= 999999:
                flag = False
        except ValueError as v_err:
            print('You entered {}'.format(v_err) + '.' + 'Please enter six digit value')
    return entered_value


def method_comparison(easy_result: int, hard_result: int) -> str:
    if easy_result == hard_result:
        return 'Draw'
    return 'Easy' if easy_result > hard_result else 'hard'


def main():

    tickets = ticket_list(is_valid('initial_value'), is_valid('end_value'))

    easy_var = calculate_via_easy(tickets)

    hard_var = calculate_via_hard(tickets)

    result_methods = method_comparison(easy_var, hard_var)

    print(
        f'{result_methods} win!\n'
        f'Easy method has {easy_var} happy tickets!\n'
        f'Hard method has {hard_var} happy tickets!'
    )


if __name__ == '__main__':
    main()
