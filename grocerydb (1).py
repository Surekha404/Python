#---------------- Surekha Mart MGMT System ---------------


import mysql.connector
# establishing the connection with mysql
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='grocery'
    )
# getting the cursor object to execute queries
c = mydb.cursor()

items = []
t_qty = 0
ts_qty = 0
ts_price = 0


while True:
    print('****************************************************')
    print('*                                                  *')
    print("-$-$-$-$-$-$Welcome to Surekha's Mart $-$-$-$-$-$-$-")
    print('*                                                  *')
    print('****************************************************')
    print('1. View items \n2. Add new items \n3. Purchasing\n4. Searching \n5. Editing \n6. Exit')
    option = input('Enter the number of your choice : ')
    if option == '1':
        print('_____View Items_____')
        print('Total Items are : ', len(items))
        while len(items) != 0:
            print('Available Items : ')
            for item in items:          # for display in dict
                for key, value in item.items():
                    print(key, ':', value)
            break
    elif option == '2':
        print('_____ADD Items_____')
        print('Adding new Items')
        item = {}
        item['name'] = input('Item name : ')
        c.execute ( 'CREATE TABLE IF NOT EXISTS grocery(quantity int,price int,name varchar(90))' )

        name = item [ 'name' ]

        while True:
            try:
                item['qty'] = int(input('Item quantity : '))
                t_qty = t_qty + item['qty']                  # used for Sale as per quantity pi graph
                break
            except ValueError:                                # If the user put in the no numerical values
                print('Enter Numeric Figure')

        while True:
            try:
                item['price'] = int(input('Price Rupees : '))
                break
            except ValueError:                                # If the user put in the no numerical values
                print('Enter Numeric Figure')
        print('Item has successfully added.')
        sql = 'INSERT INTO grocery VALUES(%s,%s,%s)'  # %s=place holder for string
        quantity = item [ 'qty' ]
        price = item [ 'price' ]
        val = (name, quantity, price)

        items.append(item)

    elif option == '3':
        y1 = [0]             # Used for Sales Pyplot graph
        print('_____Purchase Items_____')
        print(items)
        pur_item = input(' Which item do you want to purchase ? Enter name : ')
        pur_qty = int(input(' How much do you want to purchase ? : '))
        pur_price =0
        for item in items:
            if pur_item.lower() == item['name'].lower():   # User can write a name with capital and small letter
                pur_price = pur_qty * item['price']
                if item['qty'] != 0:
                    print('Pay', pur_price, 'Rupees at checkout counter.')
                    item['qty'] -= pur_qty

                else:
                    print('Item Out of Stock.')
            y1.append(int(pur_price))                # Used for Sales Pyplot graph

        ts_qty = ts_qty+pur_qty                      # Used for Sales Pyplot graph

    elif option == '4':
        print('_____Search Items_____')
        fd_item = input ('Enter the Item\'s name to search in the List : ')
        for item in items:
            if fd_item.lower() == item['name'].lower():
                print('The item named ' + fd_item + ' is displayed below with its details')
                print(item)
            else:
                print('Item Not Found.')
    elif option == '5':
        print('_____Edit Items_____')
        ed_item = input ('Enter the name of the Item that you want to edit : ')
        for item in items:
            if ed_item.lower() == item['name'].lower():
                print('Current details of ' + ed_item)
                print(item)
                item['name'] = input('Item name : ')
                while True:
                    try:
                        item['qty'] = int(input('Item Quantity : '))
                        break
                    except ValueError:                 # If the user put in the no numerical values
                        print('Enter Numeric Figure')
                while True:
                    try:
                        item['price'] = int(input('Price Rupees : '))
                        break
                    except ValueError:               # If the user put in the no numerical values
                        print('Enter Numeric Figure')
                print('Item has successfully updated.')
                print(item)
            else:
                print('Item Not Found.')
    elif option == '6':
        print('_____Exit_____')
        break
    else:
        print(' You Entered an Invalid option')





# Bar Chart for the Items and its Quantity
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for item in items:
    x.append(item.get('name'))
    y.append(item.get('qty'))

plt.bar(x, y)
plt.show()
# Pie Chart for the Sales as per Quantity
x = ['Total_Quantity', 'Total_Sold_Quantity']
y = [t_qty, ts_qty]
myexplode = [0.1, 0.1]
color = ['red', 'green']
plt.pie(y, labels = x, explode = myexplode, colors=color)
plt.show()

# PyPlot of the Sales
plt.plot(y1)
plt.legend(["Sales"], loc = "lower right")
plt.show()

#execute queries

'''
#sql='INSERT INTO user VALUES(%d,%s,%s,%s)'  # %d is not supported


c.execute(sql, val)
mydb.commit() # accept the changes, without this data will not be added
'''