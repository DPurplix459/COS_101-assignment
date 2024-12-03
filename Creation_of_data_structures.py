#Collections/Data Structures...
#Examples are lists,tuple,Dictionary
#A dictionary is a collection of value pair

number1 = [14, 29, 7,86]

okpa_list = ['bambara nut',
             'maggi',
             'palm oil',
             'vegetable oil',
             'fish',
             ]

#to append an item (keep it aside..)

print(okpa_list)
okpa_list.append('egg')
print(okpa_list)

#to check for an item in the list..

ingredient = input('Enter an ingredient for okpa:')

for item in okpa_list:
    if item == ingredient:
        print(item, ' is in the list.')





#Creating a list...

numbers = (14,45,28,65,8,74,64 )

total=0

for number in numbers:
    total = total + number
    print(total)

#write a for loop to print the numbers in revers..
#Index and

#Assignment...
#reverse=0
#for number in numbers:
 #   reverse = reverse - number
#    print(reverse)

