def grocery_to_do(money, *grocery_items): #the use of * before grocery_items is to allow an arbitrary number of arguments
    acronym = ''
    for i in grocery_items:
        acronym += i[0].title()
    print('You have {}$'.format(money)) # this is another way to write "print('You have ' + str(money) + '$')" using place holder {}
    print('Your acronym is', acronym)