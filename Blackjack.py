cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

#Deal card function - uses the list below to return a random card 
import random
from art import blackjack_logo

def deal_card():
    """Returns a random card from the deck"""
    card = random.choice(cards)
    return card

#Calculate score for cards

def calculate_score(cards):
    """Take the list of cards and return the score calculate the cards"""
    #Check for a blackjack inside calculate_score() function
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Check for an 11 ace. If the score is already over 21, remove the 11 and replace it with a 1 in the cards list.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

#Define a function called comapre(), to decide a winner 

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 😅 "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 🤯"
    elif user_score == 0:
        return "Win with a blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😃"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😠"

def play_game():
    
    print(blackjack_logo)
    
    #Deal the user and computer 2 cards using deal_card()

    user_cards = []
    computer_cards = []
    is_game_over = False 

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        #If the computer or the user has a blackjack or if the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            #If the game is not ended, ask user to draw another card.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True    

    # Defining computer's game play 
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#Restart the game 
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ") == "y":
    play_game()
