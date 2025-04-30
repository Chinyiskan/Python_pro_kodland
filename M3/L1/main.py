from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "The Earth revolves around the Sun.",
    "Honey never spoils.",
    "Octopuses have three hearts.",
    "Bananas are berries, but strawberries are not.",
    "A group of flamingos is called a 'flamboyance'.",
    "Wombat poop is cube-shaped.",
    "A day on Venus is longer than a year on Venus.",
    "The Eiffel Tower can be 15 cm taller during the summer.",
]

@app.route("/")
def index():
    return (
        '<h1>Bienvenidos a la página de los datos interesantes!</h1>'
        '<a href="/random_fact">Haz click aquí!</a>'
    )

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

if __name__ == "__main__":
    app.run(debug=True)
