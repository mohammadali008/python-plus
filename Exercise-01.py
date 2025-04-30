# get and search some words in dictionary
my_dict = {
    'book':'کتاب',
    'car':'ماشین',
    'red':'قرمز'
}
user_input = input('Enter your word :').strip().lower()
if user_input in my_dict.keys():
    print('ok; we know your word that you entered !...')
    print(f"word is {user_input}\nmeaning is {my_dict.get(user_input)}")
    #user_input = input("Enter another word :") --- if we want to make loop for input we can user while  
else:
    print("we don't know your word . please enter")
    user_input_meaning = input('Enter meaning of your word :')
    # my_dict[user_input]=user_input_meaning #Its temporary update
    my_dict.update(
        {
            user_input:user_input_meaning
        }
    )
    print('Updated dictionary :',my_dict)

# Test
# Enter 'car'
#you will get 'ماشین'
#if you enter 'hello' you should enter meaning to update the dictionary.
    
