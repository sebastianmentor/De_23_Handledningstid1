run_program = True
while run_program == True:
    print('Meny\n1. gör något\n2. Avsluta')
    var = input('Gör ett val: ')
    if var == '1':
        pass
    elif var == '2':
        run_program = False
    else:
        print('Försök igen! Och läs menyn ordentligt!!!!')

for i in range(4):
    print(i)