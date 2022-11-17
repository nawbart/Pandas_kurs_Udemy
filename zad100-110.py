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