#need to generate random values
import random 

#constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

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
    for line in range(lines):    #looping thru every row
        symbol = columns[0][line]   #1st column in the current row
        for column in columns:      #go thru each colmn
            symbol_to_check = column[line]
            if symbol != symbol_to_check:   #if symbols are not the same
                break
        else:   #if the symbols are same
            winnings += values[symbol] * bet    #bet on each line, not the total bet
            winning_lines.append(line + 1)      # +1 coz 'line' is an index, we want 1,2,3 and not 0,1,2

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #key,values
        for _ in range(symbol_count): # underscore is anonymous var, when we don't care abt the iteration value then we use '_' as unused value 
            all_symbols.append(symbol) 

    columns = []  
    for _ in range(cols):  #values to go thru each cols
        column = []
        current_symbols = all_symbols[:] #slice operator - copy a list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): #enumerate gives index and item both
            if i != len(columns) - 1:  #max index we have to access a element in the columns list
                print(column[row], end=" | ") #pipe operator- not printing the last column
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():  #-ve numbers won't be true using this
            amount = int(amount) #default comes as str
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def numbersOfLines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
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
    lines = numbersOfLines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)  # asterisk- splat/unpack operator: pass every single line from the winning line list to print func 
    # (if we won on 2 lines- 1 2 ; if we won on 3 lines - 1 2 3 ) =output

    return winnings - total_bet  #how much they won and lost


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()