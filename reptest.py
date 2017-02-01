file_name = 'game_stat.txt'

lists = []
with open(file_name, 'r') as f:
    for each in f:
        items = each.split('\t')
        lists.append(items)

print(lists)
print('Average is:', )
