#!python

import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
def letter_to_num(digit):
    letters = list(string.ascii_lowercase)
    # checks if digit is a letter
    if digit in letters:
        for i in range(len(letters)):
            if digit.lower() == letters[i]:
                return 10 + i
    # if number is 0-9 return its value
    else:
        return float(digit)
def dec_for_whole_num(digits, base):
    final_value = 0
    leng = len(digits)
    for i in range(leng):
        next = digits[i]
        if not next == '.':
            decimal_value_of_single_digit = float(
                letter_to_num(next))
            final_value += (
                math.pow(base, (leng - 1)) * decimal_value_of_single_digit)
            # move down the exp for the next iteration
            leng -= 1
        else:
            pass
    return final_value

def decode_from_any_base(digits, base, decoded):
    if '.' in digits:
        index = digits.index('.')
        int_portion = digits[:index]
        fractional = digits[index:]
        if not int_portion == '0':
            decoded += dec_for_whole_num(int_portion, base)

            digits = '0' + fractional
            return decode_from_any_base(digits, base, decoded)
        elif not fractional == '.0':
            decoded += dec_for_frac_num(digits, base)
            return decoded
    else:
        return int(dec_for_whole_num(digits, base))

def decode(digits, base):

    assert 2 <= base <= 36, 'base is unacceptable {}'.format(base)
    decoded = 0
    return decode_from_any_base(digits, base, decoded)

def whole_num_leng(number, base):
    exp = 0
    pow = -1
    while pow <= number:
        exp += 1
        pow = math.pow(base, exp)
    return (exp)

def get_equivalent_for_integers(number, base, new_num_leng):
    new_value = ''
    letters = list(string.ascii_lowercase)
    for i in range(new_num_leng):
        place = math.pow(base, (new_num_leng - (i + 1)))
        next_num = int(number // place)
        if next_num > 9:
            index_of_digit = next_num - 10
            new_value += letters[index_of_digit]
        else:
            new_value += str(next_num)
        number -= next_num * place
    return new_value

def encode_whole_number(number, base):
    new_num_leng = whole_num_leng(number, base)
    equivalent_value = get_equivalent_for_integers(number, base,
                                                   new_num_leng)
    return equivalent_value


def encode(number, base):
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)
    encoded_num = ''
    return encode_whole_number(number, base)


def convert(digits, base1, base2):

    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    if base2 == 10:
        return str(decode(digits, base1))
    else:
        if not base1 == 10:
            digits = decode(digits, base1)
        return encode(float(digits), base2)


def main():
    import sys
    args = sys.argv[1:]
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {} (with sig figs)'.format(digits,
                                                                      base1,
                                                                      result,
                                                                      base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
