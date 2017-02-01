import csv
from collections import Counter

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(asd):  # it must be an argument there to
    print('\nInventory: ')  # use it after the import of .csv file
    for i in asd:
        print(asd[i], i)
    print('Total number of items: ', sum(asd.values()))


def add_to_inventory(inventory, added_items):
    for j in added_items:
        if j in inventory:
            inventory[j] += 1
            #checking
        else:
            inventory[j] = 1
display_inventory(inv)
k = input("Add an item: ")  # add an item
dragon_loot.append(k)

add_to_inventory(inv, dragon_loot)
display_inventory(inv)


def print_table():
    while True:
        order = input(
            '\nOrder by count? If yes, descending or ascending? \n(Type "count,desc" or "count,asc", if you don\'t want to order it, press Enter!) ')
        if order == 'count,desc':
            print('\nInventory: ')
            column = '  count    item name'
            print(column)
            print('-' * len(column))
            # now the inventory
            s = [(k, inv[k]) for k in sorted(inv, key=inv.get, reverse=True)]
            for k, v in s:
                for line in [[v, k]]:
                    print('{:>7} {:>12}'.format(*line))
            print("-" * len(column))
            print('Total number of items: ', sum(inv.values()))
            break
        if order == 'count,asc':
            print('\nInventory: ')
            column = '  count    item name'
            print(column)
            print('-' * len(column))
            # now the inventory
            s = [(k, inv[k]) for k in sorted(inv, key=inv.get, reverse=False)]
            for k, v in s:
                for line in [[v, k]]:
                    print('{:>7} {:>12}'.format(*line))
            print("-" * len(column))
            print('Total number of items: ', sum(inv.values()))
            break
        if order is '':
            print('\nYou choosed not to order!')
            display_inventory(inv)
            break
        if order is not 'count,desc' and order is not 'count,asc' and order is not '':
            print('\nPls type only "count,desc" or "count,asc" or press Enter for not sorting!\n')
            continue

print_table()


def import_inventory(filename):
    f = open(filename)  # opens the csv file
    try:
        csv_f = csv.reader(f)  # creates the reader object
        listed = list(csv_f)
        dicted = dict(listed[1:])
        redict = dict((k, int_if_possible(v)) for (k, v) in dicted.items())
        print('\nImported items: ')
        A = Counter(inv)
        B = Counter(redict)
        for row in redict:
            print(redict[row], row)
        global inv2
        inv2 = A + B
        display_inventory(inv2)

    finally:
        f.close()      # closing .csv file


def int_if_possible(value):
    try:
        return int(value)
    except:
        return value


def export_inventory(filename):
    myfile = open(filename, 'w')
    wr = csv.writer(myfile)
    print(inv2)
    print(type(inv2))
    ex = dict(inv2)
    invnew = list(ex)
    print(type(invnew))
    print(ex)
    for m in ex:
        z = (ex[m], m)
        wr.writerow(z)
    myfile.close()

imp = input('\nDo you want to import an inventory? (press "y" or "n") ')
while imp:
    if imp == 'y':
        import_inventory('import_inventory.csv')
        exp = input('\nDo you want to export it to a file? (Press "y" or "n") ')
        if exp == "y":
            export_inventory('export_inventory.csv')
            break

        if exp == "n":
            quit()

        else:
            print('\nPls type only "y" or "n"!\n')
            continue

    if imp == 'n':
        quit()

    else:
        print('\nPls type only "y" or "n"!\n')
        continue
