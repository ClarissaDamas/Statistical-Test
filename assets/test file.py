import pandas as pd
n = float(input('Which limit?  '))
listnumbers = list(map(float,input('Which are the numbers?  ').split()))
listnumbers_aspandas = pd.Series(listnumbers)
describe_numbers = (listnumbers_aspandas).describe()
mean = listnumbers_aspandas.mean()
min = listnumbers_aspandas.min()
std = listnumbers_aspandas.std()
#formula = round(((n - mean)/std ),2)
formula = round(((n - listnumbers_aspandas).mean() /(listnumbers_aspandas).std()),2)
# print(describe_numbers)
# print(formula)
print(std)
print(mean)
if listnumbers == []:
    # raise Exception
    print(mean)
    print('ok')

else:
    print(mean)
