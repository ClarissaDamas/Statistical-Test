import pandas as pd

try:
    Zlimit = float(input('Which limit?  '))
except:
    print('We got an error,please make sure you wrote a number as Zlimit,ex: 2.0,3 or 0')
    exit()

Question = input('Do you have average and std already?Answer Yes or No only!  ') #let everything uppercase so dont have mistakes

def Zwith_average(Zlimit):
    Mean = float(input('Which is the mean?  '))
    std = float(input('Which is the std?  '))
    formula = round(((Zlimit - Mean)/std ),2)
    return formula

def Zwithout_average(Zlimit,listnumbers):
    listnumbers_aspandas = pd.Series(listnumbers)
    describe_numbers = (listnumbers_aspandas).describe()
    formula = round(((Zlimit - listnumbers_aspandas).mean() /(listnumbers_aspandas).std()),2)
    print(listnumbers)
    print(describe_numbers)
    return formula

try:
    if Question == 'yes':
        value = Zwith_average(Zlimit)

    else:
        listnumbers = list(map(float,input('Which are the numbers?  ').split()))
        value = Zwithout_average(Zlimit,listnumbers)

    if value < 0 :
        value = (value)*(-1)

    if len(str(value)) >= 4:
        firstdecimal = float((str (value)[:-1]))

    else:
        firstdecimal = float (str (value))
    seconddecimal = float (str (value - firstdecimal))

    if len(str(seconddecimal)) >= 4:
        seconddecimal =  round((seconddecimal),4)

except ZeroDivisionError as error:
    print('The std number you gave was:',std,',please make sure to write a positive number')
    exit()

except ValueError as error:
    print('We got an error,please make sure you wrote a number,ex: 2.0,3 or 0')
    exit()

print(value)
print(seconddecimal)
read_value_excel = pd.read_excel(r'Tabela da distribuição normal 2.xlsx')
print('Until here is alright!')
try:
    find_value_excel = read_value_excel.set_index('Z')
    return_value_excel = find_value_excel.at[firstdecimal,seconddecimal]
    print(return_value_excel)

except KeyError as error:
    print('We got an error because you wrote:',(listnumbers)[0],'or',int((listnumbers)[0]),'.Please make sure to write more than one number,if you already have the mean and std run the code again and answer yes.')
    #raise IndexError(print('We got an error because you wrote:',(listnumbers),'.Please make sure to write more than one number,if you already have the mean and std run the code again and answer yes.')) from e


#NOW DO PROBABILITY
#if the (input('Do you wanna know the probability?Answer yes or no only')) == 'yes':
