
#convert decimal to binary  with recursion
def DecToBin(num):

    if num > 1:
        DecToBin(num // 2)
    print(num % 2, end = '')


if __name__ == '__main__':

    # decimal value\
    dec_val = 10

    # Calling function
    DecToBin(dec_val)
#     DecToHex(dec_val)
