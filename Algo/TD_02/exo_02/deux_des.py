arg1 = int(input('valeur 1 : '));
arg2 = int(input('valeur 2 : '));

if ((1 <= arg1 <= 6) and (1 <= arg2 <= 6)):
    if arg1 > arg2:
        print(arg1, arg2)
    else:
        print(arg2, arg1)
