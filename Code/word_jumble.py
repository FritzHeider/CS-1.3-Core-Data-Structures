def test_solve_word_jumble_1():
    # Cartoon prompt for final jumble:
    # "Farley rolled on the barn floor because of his __-______."
    letters = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    circles = ['__O_O', 'OO_O_', '____O_', '___OO_']
    final = ['OO', 'OOOOOO']
    solve_word_jumble(letters, circles, final)
def test_solve_word_jumble_2():
    # Cartoon prompt for final jumble: "What a dog house is: A ____ ___."
    letters = ['TARFD', 'JOBUM', 'TENJUK', 'LETHEM']
    circles = ['____O', '_OO__', '_O___O', 'O____O']
    final = ['OOOO', 'OOO']
    solve_word_jumble(letters, circles, final)
def test_solve_word_jumble_3():
    # Cartoon prompt for final jumble:
    # "A bad way for a lawyer to learn the criminal justice system: _____ and _____."
    letters = ['LAISA', 'LAURR', 'BUREEK', 'PROUOT']
    circles = ['_OOO_', 'O_O__', 'OO____', '__O_OO']
    final = ['OOOOO', 'OOOOO']
    solve_word_jumble(letters, circles, final)
