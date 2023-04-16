############### Blackjack Project #####################

import random
import os

logo = """


          oooooooooo.  oooo                      oooo             
          `888'   `Y8b `888                      `888             
           888     888  888   .oooo.    .ooooo.   888  oooo       
           888oooo888'  888  `P  )88b  d88' `"Y8  888 .8P'        
           888    `88b  888   .oP"888  888        888888.         
           888    .88P  888  d8(  888  888   .o8  888 `88b.       
          o888bood8P'  o888o `Y888""8o `Y8bod8P' o888o o888o      
                                                                  
                                                                  
                                                                  
   oooo                     oooo             88   .oooo.     .o   
   `888                     `888            .8' .dP""Y88b  o888   
    888  .oooo.    .ooooo.   888  oooo     .8'        ]8P'  888   
    888 `P  )88b  d88' `"Y8  888 .8P'     .8'       .d8P'   888   
    888  .oP"888  888        888888.     .8'      .dP'      888   
    888 d8(  888  888   .o8  888 `88b.  .8'     .oP     .o  888   
.o. 88P `Y888""8o `Y8bod8P' o888o o888o 88      8888888888 o888o  
`Y888P                                                            
                                                                  
"""

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

seed = random.randint(0, 5000)
random.seed(seed)

end_of_game = False

def user_deal(cards):
    return random.choice(cards)

def computer_deal(cards):
    return random.choice(cards)

def clear():
    os.system('cls')
    os.system('clear')


while end_of_game == False:
    clear()

    user_cards = []
    user_total = 0

    computer_cards = []
    computer_total = 0

    print(logo)
    user_response = input("\nWould you like to play a game of blackjack?\nType 'y' for Yes or 'n' for No : ") 

    if user_response == 'y':
        end_of_game = False
    else:
        end_of_game = True
        break
    
    user_cards.append(user_deal(cards))
    user_cards.append(user_deal(cards))
    user_total = sum(user_cards)

    computer_cards.append(user_deal(cards))
    computer_cards.append(user_deal(cards))
    computer_total = sum(computer_cards)

    print(f"\nYour cards are: {user_cards}, and your current score is: {user_total}")
    print(f"The computer's first card is: {computer_cards[0]}")

    hit_or_stay = input("\nType 'h' for Hit if you want another card or 's' for stay if you want to take your chances: ")

    if hit_or_stay == 'h':
        user_cards.append(user_deal(cards))
        if 11 in user_cards:
            ace = input("\nYou have an Ace!. How would you like to use it towards your total? Type '1' to use it as the value 1 and '11' to use its value as 11: ")
            if ace == '1':
                index = user_cards.index(11)
                user_cards[index] = 1
                user_total = sum(user_cards)
            else:
               user_total = sum(user_cards) 
        else:
            user_total = sum(user_cards)
       

        if user_total > 21:
            print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
            print(f"The computer's hand is: {computer_cards}")
            print("\nYou are over 21. Sorry, You Lose!\n")
            user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
            if user_response == 'y':
                end_of_game = False
            else:
                end_of_game = True
                break
        else:
            if computer_total < 17:
                computer_cards.append(user_deal(cards))
                computer_total = sum(computer_cards)
                if computer_total > 21:
                    print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                    print(f"The computer's hand is: {computer_cards}")
                    print("\nYou Win!\n")
                    user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                    if user_response == 'y':
                        end_of_game = False
                    else:
                        end_of_game = True
                        break
                else: 
                    if user_total > computer_total:
                        print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                        print(f"The computer's hand is: {computer_cards}")
                        print("\nYou Win!\n")
                        user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                        if user_response == 'y':
                            end_of_game = False
                        else:
                            end_of_game = True
                            break
                    elif user_total < computer_total:
                        print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                        print(f"The computer's hand is: {computer_cards}")
                        print("\nThe Computer has a better hand! You Lose!\n")
                        user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                        if user_response == 'y':
                            end_of_game = False
                        else:
                            end_of_game = True
                            break
            else:
                if computer_total > 21:
                    print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                    print(f"The computer's hand is: {computer_cards}")
                    print("\nYou Win!\n")
                    user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                    if user_response == 'y':
                        end_of_game = False
                    else:
                        end_of_game = True
                        break
                else: 
                    if user_total > computer_total:
                        print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                        print(f"The computer's hand is: {computer_cards}")
                        print("\nYou Win!\n")
                        user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                        if user_response == 'y':
                            end_of_game = False
                        else:
                            end_of_game = True
                            break
                    elif user_total < computer_total:
                        print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                        print(f"The computer's hand is: {computer_cards}")
                        print("\nThe Computer has a better hand! You Lose!\n")
                        user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                        if user_response == 'y':
                            end_of_game = False
                        else:
                            end_of_game = True
                            break
    else:
        if user_total > 21:
            print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
            print(f"The computer's hand is: {computer_cards}")
            print("\nYou are over 21. Sorry, You Lose!\n")
            user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
            if user_response == 'y':
                end_of_game = False
            else:
                end_of_game = True
                break
        else:
            if computer_total < 17:
                computer_cards.append(user_deal(cards))
                computer_total = sum(computer_cards)
                if computer_total > 21:
                    print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                    print(f"The computer's hand is: {computer_cards}")
                    print("\nYou Win!\n")
                    user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                    if user_response == 'y':
                        end_of_game = False
                    else:
                        end_of_game = True
                        break
                else: 
                    if user_total > computer_total:
                        print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                        print(f"The computer's hand is: {computer_cards}")
                        print("\nYou Win!\n")
                        user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                        if user_response == 'y':
                            end_of_game = False
                        else:
                            end_of_game = True
                            break
                    elif user_total < computer_total:
                        print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                        print(f"The computer's hand is: {computer_cards}")
                        print("\nThe Computer has a better hand! You Lose!\n")
                        user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                        if user_response == 'y':
                            end_of_game = False
                        else:
                            end_of_game = True
                            break
            else:
                if computer_total > 21:
                    print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                    print(f"The computer's hand is: {computer_cards}")
                    print("\nYou Win!\n")
                    user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                    if user_response == 'y':
                        end_of_game = False
                    else:
                        end_of_game = True
                        break
                else: 
                    if user_total > computer_total:
                        print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                        print(f"The computer's hand is: {computer_cards}")
                        print("\nYou Win!\n")
                        user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                        if user_response == 'y':
                            end_of_game = False
                        else:
                            end_of_game = True
                            break
                    elif user_total < computer_total:
                        print(f"\nYour final hand is: {user_cards}, and your current score is: {user_total}")
                        print(f"The computer's hand is: {computer_cards}")
                        print("\nThe Computer has a better hand! You Lose!\n")
                        user_response = input("\nWould you like to play again?\nType 'y' for Yes or 'n' for No : ") 
                        if user_response == 'y':
                            end_of_game = False
                        else:
                            end_of_game = True
                            break


print("\nThank you for playing!!\n\n")
                        







    


    

