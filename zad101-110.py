import numpy as np
import pandas as pd


print('Zad 101', '\n')

stocks1 = ['PLW', 'CDR', '11B', 'TEN']
ser1 = pd.Series(stocks1)
print(ser1, '\n')

print('Zad 102', '\n')

stocks2 = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
ser2 = pd.Series(stocks2, dtype=float)


print(ser2, '\n')

print('Zad 103', '\n')

stocks3 = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quo3 = pd.Series(data=stocks3)
quo3 = quo3.tolist()

print(quo3, '\n')

print('Zad 104', '\n')

stocks4 = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quo4 = pd.Series(data=stocks4)
quo4 = pd.DataFrame(data=quo4, index=None, columns=['price'], dtype=None, copy=None)

print(quo4, '\n')


print('Zad 105', '\n')

s5 = pd.Series(
    data = np.arange(10, 100, 10),
    index = np.arange(101, 110, 1),
    dtype='float'
)

print(s5, '\n')


print('Zad 106', '\n')

s6 = pd.Series(['001', '002', '003', '004'], list('abcd'))
s6 = s6.astype(int)

print(s6, '\n')

'''
print('Zad 107', '\n')

s7 = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quo7 = pd.Series(data=s7)

quo7 = quo7.append(pd.Series({'BBT': 25.5, 'F51': 19.2}))
print(quo7)



print(quo7, '\n')

'''

print('Zad 107 - drugie rozwiązanie za pomocą funkcji concat', '\n')

s7b = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quo7b = pd.Series(data=s7b)

s7c = {'BBT': 25.5, 'F51': 19.2}
quo7c = pd.Series(data=s7c)

r7 = pd.concat([quo7b, quo7c])
print(r7, '\n')

print('Zad 108', '\n')

s8 = {
    'PLW': 387.00,
    'CDR': 339.5,
    'TEN': 349.5,
    '11B': 391.0,
    'BBT': 25.5,
    'F51': 19.2,
}
quo8 = pd.Series(data=s8)
df8 = pd.DataFrame(quo8).reset_index()
df8.columns = ['ticker', 'price']

print(df8, '\n')

print('Zad 109', '\n')

data9 = {'company': ['Amazon', 'Microsoft', 'Facebook'],
        'price': [2375.0, 178.6, 179.2],
        'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']}

df9 = pd.DataFrame(data9)

print(df9, '\n')

print('Zad 110', '\n')

data_dict = {
    'company': ['Amazon', 'Microsoft', 'Facebook'],
    'price': [2375.00, 178.6, 179.2],
    'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']
}

companies = pd.DataFrame(data=data_dict)
companies = companies.set_index('company')

print(companies, '\n')










































































































































