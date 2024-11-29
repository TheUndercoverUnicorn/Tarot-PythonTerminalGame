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
    if card_number <= 21:
        reading = "test"
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

while exit == False:
    ask_a_question
    draw_status = ask_a_question()

    if (draw_status == "N"):
        gameOver = input("Do you want to QUIT the game? Y/N\n")
        if (gameOver == "Y"):
            exit = True
        if (gameOver == False):
            break
    elif (draw_status == "Y"):
        draw_a_card()
        card_number = draw_a_card()
        your_reading(card_number)
    else:
        print("That is not a valid entry. Please try again")
        break


