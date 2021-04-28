int_1 = int(input("ENTER THE FRIST NUMBER"))
int_2 = int(input("ENTER THE SECOND NUMBER"))
operator = str(input("ENTER THE OPERATOR"))
if operator == '+':
    print (int_1 + int_2)
elif operator == '-':
    print (int_1 - int_2)
elif operator == '*':
    print (int_1 * int_2)
elif operator == '/':
    print (int_1 /int_2)
else:
    print('WRONG INPUT')