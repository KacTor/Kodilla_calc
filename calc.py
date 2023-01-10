import sys
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', filename='logfile.log')

mathOperations = ['Addition', 'Subtraction', 'Multiplication', 'Division']


def select_operation(listOfOperation):
    while True:
        for index, operation in enumerate(listOfOperation, 1):
            print(index, operation)

        try:
            index = int(input("Choose the number for the math operation:"))

            if index <= len(listOfOperation):
                return index

            else:
                logging.info("Number not in range ")
                continue

        except ValueError:
            logging.info("Wrong type of input")
            continue


if __name__ == "__main__":

    index = select_operation(mathOperations)

    # Calculator

    result = 0
    resultMult = 1

    i = 1

    # Addition
    if index == 1:
        print('If you want to exit, enter any non-number character.')
        while True:
            try:
                numbToAdd = int(input(f'Enter {i} number: '))
                logging.debug(f'Add {numbToAdd} to {result} ')
                result += numbToAdd
                i += 1
            except ValueError:
                print(f'Your result is {result}')
                break

    # Subtraction
    elif index == 2:
        while True:
            try:
                numbToSub1 = int(input(f'Enter 1 number: '))
                numbToSub2 = int(input(f'Enter 2 number: '))
                result = numbToSub1 - numbToSub2
                logging.debug(f'Sub {numbToSub2} from {numbToSub1} ')
                print(f'Your result is {result}')
                break

            except ValueError:
                print('Enter correct number!')
                continue

    # Multiplication
    if index == 3:
        print('If you want to exit, enter any non-number character.')
        while True:
            try:
                numbToMult = int(input(f'Enter {i} number: '))
                logging.debug(f'Mult {numbToMult} by {resultMult} ')
                resultMult *= numbToMult
                i += 1
            except ValueError:
                print(f'Your result is {resultMult}')
                break

    # Division
    elif index == 4:
        while True:
            try:
                numbToSub1 = int(input(f'Enter 1 number: '))
                numbToSub2 = int(input(f'Enter 2 number: '))
                result = numbToSub1 / numbToSub2
                logging.debug(f'Sub {numbToSub1} by {numbToSub2} ')
                print(f'Your result is {result}')
                break

            except ValueError:
                print('Enter correct number!')
                continue
