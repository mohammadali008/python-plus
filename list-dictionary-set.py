# -- Dict --- #
# first = {
#     'A':'Ali','B':'Reza'
# }
# second = {
#     'score1':20,'score2':15
# }
#first.keys()
#first.values()
#del first['A]
#first.update(second)
####----###
value = input('Enter your Values :').split(',')
my_dict = {}
for item in value:
    keys = []
    for index in range(len(item)):
        keys[index-1] = item[0]
    print(keys)

values = input('Enter nums :').split()
for item in values:
    if 



