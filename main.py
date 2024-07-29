import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):  # loop throw user bet on
        symbol = columns[0][line]  # # checking first symbol in first column of current row
        for column in columns:  # checking symbol in first column of current row
            symbol_to_check = column[line]  # ta
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet  # bet on each line, not total_bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_counts in symbols.items():  # return key-pair for symbols dict
        for _ in range(symbol_counts):  # loops from symbol_count, takes pair(number)
            all_symbols.append(symbol)  # appends the symbol by symbol_count into all_symbols

    columns = []  # represent values in column, not rows
    for _ in range(cols):  # generate column for every single column
        column = []
        current_symbols = all_symbols[:]  # copies all_symbol
        for _ in range(rows):  # loop through value need to generate, equal to the number of rows
            value = random.choice(current_symbols)  # random value from current_symbols
            current_symbols.remove(value)  # removes first instance from current_symbol
            column.append(value)  # append to column
            # should have however many rows there symbols inside column
        columns.append(column)  # appends into columns as a nested list

    return columns


def print_slots(columns):  # for transposing from horizontal, to vertical
    # basically lining every value based on index position in each list/column, vertically, I think.
    for row in range(len(columns[0])):  # loop through row we have
        for i, column in enumerate(columns):  # loops through columns, gives index and item
            if i != len(column) - 1:  # for maximum index to access an element in columns list
                print(column[row], "  |  ", end="")  # print current row
            else:
                print(column[row], end="")

        print()  # for readability


def deposit():
    while True:  # continues until proper acceptable amount is inputted
        amount = input("What would you like to deposit? $")
        if amount.isdigit():  # check is if it's a digit, not letters
            amount = int(amount)
            if amount > 0:
                break  # breaks to return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on (1 - {str(MAX_LINES)})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f" You do not have enough to bet that amount, you current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} line.  Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slots(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}")
    print("You won on lines:",
          *winning_lines)  # splat/unpack operator, unpack from winning_lines list, it will add spaces
    # if won nothing, it will nothing
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()