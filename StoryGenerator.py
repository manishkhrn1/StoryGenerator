"""
Made by: Manish Khurana
"""
import random
import tkinter as tk

nouns = ['king','queen','warrior','demon','wizard']
verbs=['fought','explored','kicked','kissed','ate','played']
vehicles=['Tesla','horse','donkey','ferrari','hatchback']
things = ['snake','car','helicopter','mouse','teddy-bear']

def StoryOne():
    name = str(input("Please Enter your name: "))
    hobby = str(input("Please Enter a hobby of yours: "))
    food = str(input("Please Enter what you like to eat the most: "))
    adjective = str(input("how would you describe your friend in one word: "))
    vehicle=random.choice(vehicles)
    noun = random.choice(nouns)
    verb= random.choice(verbs)
    thing=random.choice(things)

    story = ("Once upon a time, there was a {0} named {1}, who owned a {2} of black colour. One day {1} decided to {3} and later on {1} got tired and went" +
    " to eat some {4} and found a {5} restaraunt for that and the food {1} got was {5} too, So {1} went to the {5} chef who made the {5} {4} and {6} him."+
    "The Chef {6} {1} back and {1} ran away on {1}'s {2}. Then {1} went to the market to buy {7} and found it {5} as well. So overall {1} had a {5} day.").format(noun,name,vehicle,hobby,food,adjective,verb,thing)

    root = tk.Tk()
    root.title("Your Random Story")
    root.geometry("600x600")

    story_label= tk.Label(root, text=story ,font=("Helvetica",22) , wraplength=600)
    story_label.pack()

    root.mainloop()

StoryOne()
   
