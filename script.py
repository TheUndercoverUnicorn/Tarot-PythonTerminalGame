#import the random module so you can use the function .randint()
import random

#functions
#have user think of a question and provide input to let you know when they are ready
def ask_a_question():
    print("Think of a question.")
    ready = input("Are you ready to draw a card? Y/N\n")
    return ready

#generate a random_number between 0 (inclusive) and 22(exclusive) 
def draw_a_card():
    random_number = random.randint(0,22)
    return random_number

#run function to determine your_card from the random number and print the answer
def your_reading(card_number): 
    if card_number == 0:
        reading = ""
    elif card_number == 1:
        reading = ""
    elif card_number == 2:
        reading = ""
    elif card_number == 3:
        reading = ""
    elif card_number == 4:
        reading = ""
    elif card_number == 5:
        reading = ""
    elif card_number == 6:
        reading = ""
    elif card_number == 7:
        reading = ""
    elif card_number == 8:
        reading = ""
    elif card_number == 9:
        reading = ""
    elif card_number == 10:
        reading = ""
    elif card_number == 11:
        reading = ""
    elif card_number == 12:
        reading = ""
    elif card_number == 13:
        reading = ""
    elif card_number == 14:
        reading = ""
    elif card_number == 15:
        reading = ""
    elif card_number == 16:
        reading = ""
    elif card_number == 17:
        reading = ""
    elif card_number == 18:
        reading = ""
    elif card_number == 19:
        reading = ""
    elif card_number == 20:
        reading = ""
    elif card_number == 21:
        reading = ""
    else:
        reading = "Indeterminate. Your future cannot be divined at this time."
    print("Your Card is:\n" + reading + "\n")


#ASCII Name of Game: TAROT BY SAGEUS
print("   *****    *    ****    ***   *****")
print("     *     * *   *   *  *   *    *  ")
print("     *    *   *  *   *  *   *    *  ")
print("     *    *****  ****   *   *    *  ")
print("     *    *   *  *   *  *   *    *  ")
print("     *    *   *  *   *  *   *    *  ")
print("     *    *   *  *   *   ***     *  \n")

#disclaimer
print("Note:")
print("According to Wikipedia, Tarot was not originally created as a tool of divination,")
print("but as a permanent trump suit for card games. Knowing that, understand that this is")
print("for entertainment purposes only.\n")

#define global variables
exit = False

#ask questions and provide answers until the user Quits the game
while exit == False:
    ask_a_question
    draw_status = ask_a_question()

    if draw_status == "N":
        gameOver = input("Do you want to QUIT the game? Y/N\n")
        if gameOver == "Y":
            exit = True
    elif draw_status == "Y":
        draw_a_card()
        card_number = draw_a_card()
        your_reading(card_number)
        gameOver = input("Do you want to draw another card? Y/N\n")
        if gameOver == "N":
            exit = True
        elif gameOver == "Y":
            draw_status = False
    else:
        print("That is not a valid entry. Please try again")

#print exit message when user quits the game
if exit == True:
    print("Thank you for playing!\n")
