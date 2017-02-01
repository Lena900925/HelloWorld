inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory():
    print('Inventory: ')
    for i in inv:
        print(inv[i], i)
    print('Total number of items: ', sum(inv.values()))

def add_to_inventory(inventory, added_items):
    for j in added_items:
        if j in inventory:
            inventory[j] += 1
                            #checking
        else:
            inventory[j] = 1
display_inventory()
k = input("Add an item: ")   #add an item
dragon_loot.append(k)

add_to_inventory(inv, dragon_loot)
display_inventory()