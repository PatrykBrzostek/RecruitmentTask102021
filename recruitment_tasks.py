import itertools


def task_1(number):
    """
    :param number: 32-bit long integer
    :return: number with its digits in reversted form or 0 if the modified value will go over the 32 bit integer range
    """
    is_negative = True if number < 0 else False  # saving the sign of a number
    number = abs(number)

    #reversing the number
    reversed_number = 0
    while number != 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = int(number / 10)
    reversed_number = -1 * reversed_number if is_negative else reversed_number

    #checking if the number is over the 32 bit integer range
    int_32_ranges = -2147483648, 2147483647
    if int_32_ranges[0] <= reversed_number <= int_32_ranges[1]:
        return reversed_number
    else:
        return 0




def task_2(digits):
    '''
    :param digits: string containing digits
    :return: list of all the possible letter combinations for phone numbers
    '''
    phone_dial = {'1': [''],
                  '2': ['a', 'b', 'c'],
                  '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'],
                  '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'],
                  '9': ['w', 'x', 'y', 'z'],
                  '0': ['+'] # literally '+' isn't a letter, but I decided to treat this sign as a letter in this case
                  }

    possible_values_of_each_successive_digit = [phone_dial[digit] for digit in digits]
    combinations = list(itertools.product(*possible_values_of_each_successive_digit))
    combinations = [''.join(combination) for combination in combinations]

    combinations = [] if combinations == [''] else combinations
    return combinations


def task_3(words, maximum_width):
    '''
    :param words: text to be justified
    :param maximum_width: the width of formatted text
    :return: list of single formatted lines
    '''
    text = words.split()

    lines = []
    new_line = ''
    while text:
        word = text[0]
        if len(new_line) + len(word) + 1 <= maximum_width + 1:
            new_line = new_line + ' ' + word
            text.pop(0)
            if not text:
                lines.append(justify_line(new_line, maximum_width))
        else:
            lines.append(justify_line(new_line, maximum_width))
            new_line = ''
    return lines


def justify_line(line, width):
    '''
    :param line: text to be justified
    :param width: the width of formatted line
    :return: string containing the formatted line
    '''
    line = line[1:]
    spaces = line.count(' ')
    delta = width - len(line)
    if spaces:
        quotient = int(delta / spaces)
    else:
        quotient = 0
    nr_of_spaces = [quotient] * spaces
    suma_of_spaces = sum(nr_of_spaces)
    delta2 = delta - suma_of_spaces
    for i, space in enumerate(nr_of_spaces):
        if delta2 > 0:
            nr_of_spaces[i] += 1
            delta2 -= 1
        else:
            break

    word_of_this_line = line.split(' ')
    new_line = ''
    for i, space in enumerate(nr_of_spaces):
        new_line += word_of_this_line[i] + ' ' * (space + 1)
    new_line += word_of_this_line[-1]
    return new_line
