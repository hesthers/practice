#Finding out whether the number is a lunar year when entering the number

def lunar_year(num):
        if 1 <= num <= 3000:
            if (num % 4 == 0) | (num % 100 != 0) & (num % 400 == 0):
                return print('It is a lunar year.')
            else:
                return print('It is not a lunar year.')
        else:
            print('wrong number')

year = int(input('Enter the year '))
lunar_year(year)

