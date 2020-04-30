import pandas as pd
import datetime as dt
import numpy as np
from math import *
import time
#data = pd.read_excel (r'C:\Users\Peiran Quan\Desktop\W51.xlsx') 
#print(data)
"""
df = pd.DataFrame(data, columns=['Barcode', 'Timestamp','Date','Team Leader'])

## read columns
print (df[['Barcode','Timestamp']]) # for extracting more than 1 columns , double [] is required

## read headers
print(df.columns)

## read rows
print(df.iloc[0:5])

## read [row,column]
print(df.iloc[5,3])

counter = 0

for A,B in df.iterrows():
    print(A,B['Barcode'])
    counter += 1
    if counter >= 10:
        break

## filter by "Break Start"
BSFrame = df.loc[df['Barcode'] == 'Break Start']
#print(BSFrame)
## Summary
#print(BSFrame.describe())
## Sorting -- Both 'Date' & 'Timestamps" are descending
BSFrame_sorted = BSFrame.sort_values(['Date','Timestamp'], ascending = [False,False])
print(BSFrame_sorted)
"""

"""
def categorize_event_shift(timestamp):
    weekday_index = pd.Timestamp(timestamp).weekday()
    switcher = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    weekday = switcher.get(weekday_index,'')
    hour = pd.Timestamp(timestamp).hour
    if hour in range(6,13):
        shift = 'Morning Shift'
    elif hour in range(14,22):
        shift = 'Afternoon Shift'
    else:
        shift = 'Error'
    return weekday +' '+ shift

"""

#staged_df = pd.read_csv(r'C:\Users\Peiran Quan\Desktop\W51staged.csv')
"""
print(staged_df["Timestamp and Date"][1])
print(staged_df["Timestamp and Date"][2])

t1 = pd.to_datetime(staged_df["Timestamp and Date"][1])
t2 = pd.to_datetime(staged_df["Timestamp and Date"][2])
weekday = pd.Timestamp(staged_df["Timestamp and Date"][1]).weekday()
hour = pd.Timestamp(staged_df["Timestamp and Date"][1]).hour
weekday_shift = categorize_event_shift(staged_df["Timestamp and Date"][2])
InMin = pd.Timedelta(t2-t1).seconds/60.0

def count_pickers(picker):
    picker_array = picker.split(';')
    counter = 0
    for members in picker_array:
        counter = counter + 1
    return counter-1

print(count_pickers(staged_df["Pickers"][100]))
"""

# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("6099") # z will be 3
# print("x is {}".format(x))

# rolls = np.random.randint(low=1, high=6, size=10)
# print(rolls+10)
# print(rolls <= 3)
# xlist = [[1,2,3],[2,4,6],]
# x = np.asarray(xlist)
# print(x[1,-1])
#print("x =\n{}".format(x))
# x=[[1,2,3],[2,4,6],[1]]
# x1 = [1]
# if x.__contains__(x1):
#     print(True)
# else:
#     print(False)

# #help(list.__contains__)
# def testA(value, count):
#     if value > 21 and count > 0:
#         value = value - 10
#         count = count - 1
#         return testA(value, count)
#     else:
#         return value


# def blackjack_hand_greater_than(hand_1, hand_2):

#     dict_value = {"A":11, "2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K": 10}
#     hand1_value = 0
#     hand2_value = 0
#     countA_1 = 0
#     countA_2 = 0

#     for i in range(len(hand_1)):
#         hand1_value = hand1_value + dict_value[hand_1[i]]
#         if hand_1[i] == "A":
#             countA_1 = countA_1 + 1
#     hand1_value = testA(hand1_value, countA_1)

#     for j in range(len(hand_2)):
#         hand2_value = hand2_value + dict_value[hand_2[j]]
#         if hand_2[j] == "A":
#             countA_2 = countA_2 + 1
#     hand2_value = testA(hand2_value, countA_2)

#     print(hand1_value, '\n',  hand2_value)
#     if ((hand1_value  <= hand2_value) and hand2_value <= 21) or (hand1_value > 21):
#         return False
#     else:
#         return True


# print(blackjack_hand_greater_than(['10', '7'], ['8', '3', 'A', '5']))        
# # Check your answer
# #q3.check()



#recursion
# Solution 1
# f = lambda n:1 if n in (1,2) else f(n-1) + f(n-2)

# Solution 2
# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a,b = b, a+b
#         print(a," ", b, '\n')
#     return a

# Solution 3
def catche(f):
    memo = {}
    
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
            print(memo)
            print(x)
        return memo[x]

    return helper



def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print ('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed



@timeit
@catche
def fibR(n):
    if n == 1 or n == 2:
        return 1
    print(n)
    return fibR(n-1) +fibR(n-2)

fibR(10)