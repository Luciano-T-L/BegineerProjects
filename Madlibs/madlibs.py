# Project Mad Libs

# Creating functions to each level.
def zoo():
    adjec1 = input("Adjective: ")
    noun1 = input("Noun: ")
    verb1 = input("Verb, past tense: ")
    adverb1 = input("Adverb: ")
    adjec2 = input("Adjective: ")
    noun2 = input("Noun: ")
    noun3 = input("Noun: ")
    adjec3 = input("Adjective: ")
    verb2 = input("Verb: ")
    adverb2 = input("Adverb: ")
    verb3 = input("Verb, past tense: ")
    adjec4 = input("Adjective: ")

    print(f"""Today I went to the zoo. I saw a(n) {adjec1} {noun1} jumping up and down in its tree.
He {verb1} {adverb1} through the large tunnel that led to its {adjec2} {noun2}.
I got some peanuts and passed  them through the cage to a gigantic gray {noun3} towering above my head.
Feeding that animal made  me hungry. I went to get a {adjec3} scoop of ice cream. It filled my stomach.
Afterwards I had to {verb2} {adverb2} to catch our bus.
When I got home I {verb3} my  mom for a {adjec4} day at the zoo.""")


def park():
    adject1 = input("Adjective: ")
    noun1 = input("Plural noun: ")
    noun2 = input("Noun: ")
    adverb1 = input("Adverb: ")
    number1 = input("Number: ")
    verb1 = input("Past tense verb: ")
    adject2 = input("-est adjective: ")
    verb2 = input("Past tense verb: ")
    adverb2 = input("Adverb: ")
    adject3 = input("Adjective: ")

    print(f"""Today, my fabulous camp group went to a (an) {adject1} amusement park. 
It was a fun park with lots of cool {noun1} and enjoyable play structures. 
When we got there, my kind counselor shouted loudly, "Everybody off the {noun2}."
We all pushed out in a terrible hurry. My counselor handed out yellow tickets, and we scurried in. 
I was so excited! I couldn't figure out what exciting thing to do first. 
I saw a scary roller coaster I really liked so, I {adverb1} ran over to get in the long line that had 
about {number1} people in it. 
When I finally got on the roller coaster I was {verb1}. 
In fact I was so nervous my two knees were knocking together. This was the {adject2} ride I had ever been on! 
In about two minutes I heard the crank and grinding of the gears. That’s when the ride began! 
When I got to the bottom, I was a little {verb2} but I was proud of myself. 
The rest of the day went {adverb2}. It was a(n) {adject3} day at the fun park.  """)


def arcade():
    noun1 = input("Plural noun: ")
    noun2 = input("Plural noun: ")
    verb1 = input("Verb: ")
    noun3 = input("Noun: ")
    verb2 = input("-ing verb: ")
    noun4 = input("Plural noun: ")
    noun5 = input("Noun: ")
    noun6 = input("Plural noun: ")

    print(f"""When I go to the arcade with my {noun1} there are lots of games to play. 
I spend lots of time there with my friends. In the game X-Men you can be different {noun2}. 
The point of the game is to {verb1} every robot. You also need to save people. 
Then you can go to the next level.  In the game Star Wars you are Luke Skywalker and you try to destroy every {noun3}. 
In a car racing/motorcycle racing game you need to beat every computerized vehicle that you are {verb2} against.
There are a whole lot of other cool games. When you play some games you win {noun4} for certain scores. 
Once you're done you can cash in your tickets to get a big {noun5}. You can save your {noun6} for another time. 
When I went to this arcade I didn't believe how much fun it would be. 
So far I have had a lot of fun every time I've been to this great arcade!""")


# Import random to get a random level
import random


def start_game():
    games = [zoo, park, arcade]  # random will get a value from here.
    print("")
    print("------------Welcome to Mad Libs------------")

    # While loop to the game keep running until the input != "yes"
    while True:
        print("")
        want_play = input("Do you want to play? Yes/No ").upper()

        if want_play == "YES":
            print("")
            random.choice(games)()  # Getting a random item for de list. add de () to call the function.

        else:
            print("")
            print("Bye bye!")
            return False


start_game()
