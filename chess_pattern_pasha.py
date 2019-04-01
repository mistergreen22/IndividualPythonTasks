

def chess_pattern(length: int, width: int):
    for x in range(length):
        if x % 2 == 0:
            print('* ' * (width // 2)) if width % 2 == 0 else print("*" + (" *" * (width // 2)))
        else:
            print(' *' * (width // 2)) if width % 2 == 0 else print('' + ('* ' * (width//2)))


def main():
    while True:
        try:
            input_1 = int(input('Enter an integer value from 1 to 100: '))
            input_2 = int(input('Enter a value from 1 to 100: '))
        except ValueError:
            print('Enter an integer value between 1 and 100')
            continue
        if input_1 > 100 or input_1 < 1:
            print('Enter an integer value between 1 and 100')
            continue
        if input_2 > 100 or input_2 < 1:
            print('Enter an integer value between 1 and 100')
            continue
        else:
            break

    chess_pattern(input_1, input_2)


main()

