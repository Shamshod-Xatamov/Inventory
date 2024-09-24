import random
print('             Welcome to Grocery 🏪         ')
print('In the end you can make some changes')
print('Please,Enter your login and password!')
login=['Shamshodbek','Bilol','Anna','Bob','Micheal']
password=['0000','1111','2222','3333','4444']
login_in=input('Enter your login: ')
password_in=input('Enter password: ')
condition = False
for i in range(len(login)):

    if login_in==login[i] and password_in==password[i]:
        condition=True
        break


def fun():
    print(f"{'Product':<12} {'Amount':<8} {'Price($)':<10} {'Total($)':<10}")
    for i in range(len(bought)):
        print(f"{bought[i]:<12} {amounts[i]:<8} {prices[i]:<10} {total[i]:<10}")
if condition:

    print("Once you finish your shopping,you need to enter 'exit' keyword ")
    inventory = {
        'apple': [1.5, 50],
        'bananas': [2, 60],
        'orange': [1, 40],
        'melon': [0.3, 60],
        'watermelon': [0.5, 35],
        'peach': [1, 80],
        'carrot': [1, 50],
        'tomato': [0.4, 90]

    }
    new_str = ''
    product_list = list(inventory.keys())

    for i in product_list:
        new_str = new_str + i + ','

    new_str = new_str.strip(',')
    print(f'We have {new_str}')
    product = ''
    bought = []
    prices = []
    amounts = []
    total = []
    while product != 'exit':

        product = input('What would you like purchase: ')
        new_product = product.lower()
        if new_product == 'exit':
            break
        price = ''

        if new_product in product_list:
            price = inventory[new_product][0]

            print(f'Price of {product} is ${price}')
            amount = int(input('How much?'))
            if amount > inventory[new_product][1]:
                print(f'Sorry!!!,but {new_product} is available only {inventory[new_product][1]}stocks')
                continue
            rest = inventory[new_product][1] - amount
            sum_price = amount * price
            print(f'You bought {amount}.Current stock: {rest} {product}')

            bought.append(new_product)
            amounts.append(amount)
            prices.append(price)
            total.append(sum_price)
            if rest < 10:
                restock_amount = random.randint(20, 50)
                rest += restock_amount
                inventory[new_product][1] = rest
                print(
                    f'{new_product.capitalize()} restocked with {restock_amount} units. New stock: {inventory[new_product][1]} {new_product}(s).')


        else:
            print('Unfortunately,this product is not available in the store')
    if not bought:
        data = {
            'Product': ['None'],
            'Amount': [0],
            'Price($)': [0],
            'Total($)': [0]
        }
    else:
        data = {
            'Product': bought,
            'Amount': amounts,
            'Price($)': prices,
            'Total($)': total
        }

    if bought:
        print("\nYour Shopping Summary:")
        fun()

        print('Do you want to make some changes?')
        yes_no=input('YES/NO: ').lower()
        if yes_no=='yes':
            print('-----MENU-----')
            print('1----Add product----')
            print('2----Remove product----')
            change=input('What change do you want:')
            if change=='1':
                print(f'Available products: {new_str}')
                new_product = input('Which product would you like to add? ').lower()
                if new_product in inventory:
                    price = inventory[new_product][0]
                    amount = int(input(f'How much {new_product} do you want to add? '))
                    if amount > inventory[new_product][1]:
                        print(f'Sorry, only {inventory[new_product][1]} units are available.')
                    else:
                        inventory[new_product][1] -= amount
                        bought.append(new_product)
                        amounts.append(amount)
                        prices.append(price)
                        total.append(price * amount)
                        print(f'{amount} units of {new_product} added.')
                        print('New shopping summary ')
                        fun()


            elif change == '2':
                remove_product = input('Which product would you like to remove? ').lower()
                if remove_product in bought:
                    idx = bought.index(remove_product)
                    del bought[idx]
                    del amounts[idx]
                    del prices[idx]
                    del total[idx]
                    print(f'{remove_product} has been removed from your list.')
                    print('New shopping summary ')
                    fun()
        sum_all=0
        for n in total:
            sum_all = sum_all + n
        print(f'Total price of shopping is ${sum_all}')
        print('Thank you for shopping with us!')

    else:
        print("You didn't buy anything!")


else:
    print('Invalid login or password!')