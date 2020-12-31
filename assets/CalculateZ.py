import pandas as pd

Zlimit = float(input('Which limit?  '))
Question = input('Do you have average and std already?Answer Yes or No only!  ') #let everything uppercase so dont have mistakes

def Zwith_average(n):
    Mean = float(input('Which is the mean?  '))
    std = float(input('Which is the std?  '))
    formula = round(((n - Mean)/std ),2)
    return formula

def Zwithout_average(n):
    listnumbers = list(map(int,input('Which are the numbers?  ').split()))
    listnumbers_aspandas = pd.Series(listnumbers)
    describe_numbers = (listnumbers_aspandas).describe()
    formula = round(((listnumbers_aspandas).mean() - n /(listnumbers_aspandas).std()),2)
    print(describe_numbers)
    return formula

    try:

        if Question == 'yes':
            value = Zwith_average(Zlimit)
            print(value)

        else:
            value = Zwithout_average(Zlimit)

        if value < 0 :
            value = (value)*(-1)

        if len(str(value)) >= 4:
            firstdecimal = float((str (value)[:-1]))

        else:
            firstdecimal = float (str (value))
            seconddecimal = float (str (value - firstdecimal)[:-2])

        if len(str(seconddecimal)) >= 4:
            seconddecimal =  round((seconddecimal),4)

    except:
        
        print('Sorry we got an error,please make sure you typed YES or NO,only.')

    read_value_excel = pd.read_excel(r'Tabela da distribuição normal 2.xlsx')
    print('until here is alright')
    find_value_excel = read_value_excel.set_index('Z')
    return_value_excel = find_value_excel.at[firstdecimal,seconddecimal]
    print(return_value_excel)

#NOW DO PROBABILITY
#if the (input('Do you wanna know the probability?Answer yes or no only')) == 'yes':
