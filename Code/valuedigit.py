hexa = {
		"a" : 10,
        "b" : 11,
        "c" : 12,
        "d" : 13,
        "e" : 14,
        "f" : 15,
	}


print(hexa['a'])

hexa_to_dec = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}
def convert(value):
    i = 0
    for key in value:
        i = i *16 + hexa_to_dec[key]
    return i

print(convert('FF'))
