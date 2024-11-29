#import the random module so you can use the function .randint()
import random

#import textwrap so that you can control the line length of the reading strings
import textwrap

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
        reading = "The Fool: Seize this opportunity to move forward and try something new. You may not succeed by you will have valuable experiences along the way."
    elif card_number == 1:
        reading = "The Magician: Look to the tools you already have. You have what you need to change this situation to be one of benefit to you, examine your resources and MacGyver this."
    elif card_number == 2:
        reading = "The High Priestess: You know in your heart what you must do. Look within and follow your inutition."
    elif card_number == 3:
        reading = "The Empress: Look to the natural world for answers and then be like nature."
    elif card_number == 4:
        reading = "The Emperor: Control is important to you. Use or create structures and algorithms that will help you to consistantly achieve the results you are looking for."
    elif card_number == 5:
        reading = "The Hierophant: It's not about chaning the situation, it's about changing your attitude. Take a spiritual stance."
    elif card_number == 6:
        reading = "The Lovers: You have a difficult choice to make. Think closely about your values and the possible consequences of your decisions."
    elif card_number == 7:
        reading = "The Chariot: Where there is a will there is a way. If you put your mind to something and just do it, you become an unstoppable force."
    elif card_number == 8:
        reading = "Strength: You are brave, strong, and can get through this. You will come out even stronger on the other end."
    elif card_number == 9:
        reading = "The Hermit: Sometimes there is just too much going on, too much change, too much acitvity. Take some time alone, away from the hustle to reset your perspective. You will know what to do."
    elif card_number == 10:
        reading = "Wheel of Fortune: To quote Baz Luhrmann, \"Sometimes you're ahead, sometimes you're behind. The race is long and, in the end, it's only with yourself.\""
    elif card_number == 11:
        reading = "Justice: What goes around comes around. We pay for our actions sooner or later, so make smart choices."
    elif card_number == 12:
        reading = "The Hanged Man: You can't do anything about that right now. Nothing you do will help you get where you want to be any faster, you just have to be patient and diligent and stay the course."
    elif card_number == 13:
        reading = "Death: Let it go, it's gone, allow it to be gone. SIt with the emptiness for a while. Soon enough, something else will come to fill the void it leaves behind."
    elif card_number == 14:
        reading = "Temperance: You have to roll with the punches. Be patient and adaptable. You can only control how you respond right now and your flexibility will not only be an asset to yourself but to the situation and those around you."
    elif card_number == 15:
        reading = "The Devil: You feel powerless and trapped, like the world is against you and there is nothing you can do but that's not true, you are looking for relief in all the wrong places. You are the warden of your own jail cell. Let go of what your are clinging to and move on."
    elif card_number == 16:
        reading = "The Tower: It feels like everything is crashing down all around you and all hope is lost. Let it go. Walk away from the rubble even though it's scary. You don't need those things anymore. Focus on what you have and build something else, it will be better for you."
    elif card_number == 17:
        reading = "The Star: Everything that is happening right now, is happening for you. It's all going to work out. Don't be discouraged, trust the process."
    elif card_number == 18:
        reading = "The Moon: You are allowing your fears to control you. Self-sabotage is keeping you from achieving your goals. Examine your self-talk. If you wouldn't say it to someone you love, why would you say it to yourself?"
    elif card_number == 19:
        reading = "The Sun: Things are good right now. Take a minute to be grateful for everything you have in your life and recognize how far you've come. You are doing good."
    elif card_number == 20:
        reading = "Judgement: Everything you have done or been or experienced up until now has lead you here. Take some time to reflect on the things, good or bad, that have brought you to this point. Is this where you want to be? Are you on the path you want to be on? It's not too late to make a change."
    elif card_number == 21:
        reading = "The World: You just leveled up! Enjoy it. You get to keep the lesson, but remember, it isn't over 'til it's over. Take some time to rest and revel before you take on the next challenge."
    else:
        reading = "Indeterminate. Your future cannot be divined at this time."
    print("Your Card is:\n")
    print(textwrap.fill(reading, 70))


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
