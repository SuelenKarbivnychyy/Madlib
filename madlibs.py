"""A madlib game that compliments its users."""

from email.mime import nonmultipart
import random
# from tkinter.ttk import Separator
# from turtle import color
from unicodedata import name

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return """Hi! This is the home page."
    <p>
    <a href="/hello">Click me to go to the game's page</a></p> """


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = random.choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)



@app.route("/game")
def show_madlib_form():

    wants_to_play = request.args.get("play")     
  
    if wants_to_play == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")  


@app.route("/madlib")
def show_madlib():  

    # name = request.args.get("name")
    # color = request.args.get("color")
    # noun = request.args.get("noun")
    # adjective = request.args.get("adjective")
    # animals_list = request.args.getlist("animal")
    # action = request.args.get("action")
    # # print("HERE IS A HINT")
    # # print(request.args.getlist("animal"))
    # animals_formatted = ", ".join(animals_list[:-1]) #use join to make string from list and separate them using comma, except element
    # animals_formatted += " and " + animals_list[-1]

    # return render_template("madlib.html",name=name, color=color, noun=noun, adjective=adjective, animals_formatted=animals_formatted, action=action)     
    
    # new madlib
    random_choise = random.randint(2,4)    
    random_choise = 3
    
    if random_choise == 2:

        plural_noun = request.args.getlist("plural_noun")
        verb = request.args.get("verb")
        transitive_verb = request.args.get("transitive_verb")
        noun1= request.args.get("noun1")
        noun2=request.args.get("noun2")

        return render_template("madlib2.html", plural_noun=plural_noun, verb=verb, transitive_verb=transitive_verb, noun1=noun1, noun2=noun2)

    elif random_choise == 3:

        plural_noun = request.args.getlist("plural_noun")
        verb = request.args.get("verb")
        transitive_verb = request.args.get("transitive_verb")
        noun1= request.args.get("noun1")
        noun2=request.args.get("noun2")

        return render_template("madlib3.html", plural_noun=plural_noun, verb=verb, transitive_verb=transitive_verb, noun1=noun1, noun2=noun2)

    else:
        
        plural_noun = request.args.getlist("plural_noun")
        verb = request.args.get("verb")
        transitive_verb = request.args.get("transitive_verb")
        noun1= request.args.get("noun1")
        noun2=request.args.get("noun2")

        return render_template("madlib4.html", plural_noun=plural_noun, verb=verb, transitive_verb=transitive_verb, noun1=noun1, noun2=noun2)



if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
