menu = {
    'pizza':200,
    'pasta':30,
    'burger':70,
    'coffee':30,
    'salad':50,
    'ice cream':20,
    'chow mein':80,
    'cheese burger':120
}

print('welcome to Gadwali  cafe')
print(menu)

order_total = 0

item_1 = input('enter the name of item you want order =')
if item_1 in menu:
    order_total += menu[item_1]
    print(f'your item {item_1} has been added to your order')

else:
     print(f'ordered item {item_1} is not available yet!')

another_order = input('do you want to add another item? (yes/no)')
if another_order == 'yes':
     item_2 = input('enter name of second item = ')
     if item_2 in menu:
         order_total += menu[item_2]
         print(f'item {item_2} has been added to order')
     else:
         print(f'ordered item {item_2} is not avaialable !')
print(f'the total amount of item to is {order_total}')

