import pandas as pd

#Receiving data for the Z-score calculation

try:
    dataPoint = float(input('Which is the data point?  '))
except:
    print('We got an error, please make sure you wrote a number as a data point, ex: 2.0,3 or 0')
    exit()

Question = ((input('Do you have the mean and standard deviation already? Answer Yes or No only! ')).upper())

#Function to ask more questions for the Z-score calculation if the user has the mean and std

def DataPointWith_mean(dataPoint):
    Mean = float(input('Which is the mean?  '))
    std = float(input('Which is the standard deviation?  '))
    formula = round(((dataPoint - Mean)/std ),2)
    return formula

#Function to calculate the mean and std for the user based on the list of numbers they have

def DataPointWithout_mean(dataPoint,listnumbers):
    listnumbers_aspandas = pd.Series(listnumbers)
    describe_numbers = (listnumbers_aspandas).describe()
    formula = round(((dataPoint - listnumbers_aspandas).mean() /(listnumbers_aspandas).std()),2)
    if listnumbers == []:
        print('We got an error because you wrote something we cannot calculate the mean. Please make sure to write more than one number, if you already have the mean and std run the code again and answer yes for the "Do you have the mean and standard deviation already?" question.')
        exit()

    elif listnumbers_aspandas.mean() == listnumbers_aspandas.min() :
        print('We got an error because you wrote:',(listnumbers)[0],'or',int((listnumbers)[0]),'.Please make sure to write more than one number,if you already have the mean and std run the code again and answer yes for the "Do you have the mean and standard deviation already?" question.')
        exit()

    else: return formula

#Code to return the function based on the user answer at line 11("Do you have the mean and standard deviation already?" question.)

try:
    if Question == 'YES':
        value = DataPointWith_mean(dataPoint)

    else:
        listnumbers = list(map(float,input('Which are the numbers you want to know the mean and standard deviation?  ').split()))
        value = DataPointWithout_mean(dataPoint,listnumbers)

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
    print('The std number you gave was: ',std,',please make sure to write a positive number!')
    exit()

except ValueError as error:
    print('We got an error,please make sure you wrote a number,ex: 2.0,3 or 0')
    exit()

#Get the Z-score at the Standard Normal Distribution Table based on the user data.

read_value_excel = pd.read_excel(r'Standard Normal Distribution Table.xlsx')
find_value_excel = read_value_excel.set_index('Z')
return_value_excel = find_value_excel.at[firstdecimal,seconddecimal]

#return to the user the Z-score found
print(return_value_excel)
