print('Welcome to the movies!')

adult_tix_price = 11.50
child_tix_price = 7.25
tax_rate = .075

choice = "y"

while choice == "y":
# wile loop starts here
    print('Movie List:')
    print('1 - Star Wars')
    print('2 - Top Gun Maverick')
    print('3 - Megamind')

    # snake_case, camelCase, PascalCase
    movie_choice = int(input('Which movie do you want to see? '))
    # print(movie_choice)

    adult_tix = int(input('How many adult tickets do you want to purchase? '))
    child_tix = int(input('How many child tickets do you want to purchase? '))

    # total price = (adult tix * adult price + child tix * child price) * (1 + tax rate)
    total_price = ((adult_tix * adult_tix_price) + (child_tix * child_tix_price)) * (1 + tax_rate)
    total_price_str = str(total_price)

    print(f'Thanks for your purchase! Your total is ${total_price}!')
    choice = input('Do you want more tickets (y/n)? ')
# loop ends here

print('Goodbye!')