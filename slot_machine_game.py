print('--------Text based slot machine------')

import random

max_line = 3
max_bet = 100
min_bet = 1

rows = 3
cols = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row], end='')
        print()


def deposit():
    while True:
        amount = input('what would you like to deposit: $')
        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print('------Amount must be greater than 0-------')
            else:
                break
        else:
            print('-----enter a valid amount-----')
    return amount


def get_line_number():
    while True:
        print('Number of line should be within 1 -', max_line)
        lines = input('Number of lines you want to bet on? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_line:
                break
            else:
                print('----Enter a valid number of lines----')
        else:
            print('-----Enter a valid a number-----')
    return lines


def get_bet():
    while True:
        sum = input('Amount of money you want to bet on each line? $')
        if sum.isdigit():
            sum = int(sum)
            if min_bet <= sum <= max_bet:
                break
            else:
                print(f"Amount should be within ${min_bet} - ${max_bet}.")
        else:
            print('-----Enter a valid a number-----')
    return sum

def spin(balance):
    line = get_line_number()
    while True:
        bet = get_bet()
        total_bet = line * bet
        if total_bet > balance:
            print(f'The bet amount ${total_bet} is out of your current balance ${balance}')
            break
        else:
            break
    print(f'You are betting ${bet} on {line} lines. Total bet: ${total_bet}')

    slots = get_slot_spin(rows, cols, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, line, bet, symbol_value)
    print(f'You won {winnings}.')
    print(f'You won on lines:', *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f'current balance is ${balance}')
        ans = input('Press enter to spin (q to quit).')
        if ans == 'q':
            break
        balance += spin(balance)
        if balance < 0:
            print('your $', balance)
            balance += deposit()

    print(f'You left with ${balance}')


main()
