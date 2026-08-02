from itertools import groupby
import string
import random

# x= random.choices(string.ascii_lowercase, k=20)
# print(x)
# x=sorted(x)
# print(x)
# print(groupby(x))
# for key, group in groupby(x):
#     print('Key : ', key, 'group : ',list(group))

data = [
    ('11013331', 'KAT'),
    ('9085267',  'NOT'),
    ('5238761',  'ETH'),
    ('5349618',  'ETH'),
    ('11708544', 'NOT'),
    ('962142',   'ETH'),
    ('7795297',  'ETH'),
    ('7341464',  'ETH'),
    ('9843236',  'KAT'),
    ('5594916',  'ETH'),
    ('1550003',  'ETH'),
]

data=sorted(data,key =lambda x: x[1])
grp= groupby(data, key= lambda x: x[1])
summary = {}
for key, group in grp:
    nums=[int(item[0]) for item in group]
    summary[key]={'count': len(nums), 'sum': sum(nums), 'max': max(nums)}

print(summary)

