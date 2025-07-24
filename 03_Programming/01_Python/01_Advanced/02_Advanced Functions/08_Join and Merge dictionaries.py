# JOIN
l = [i for i in range(10)]

combo = '-'.join(map(str,l))

print(combo)

# MERGE
print('-'*30)
dict1 = {1:'cow', 2:'goat'}
dict2 = {2:'elephant',3:'minion', 4:'banana'}

dict3 = dict1 | dict2

print(dict3)








