from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/cards")
def cards():
    connection = sqlite3.connect("smartstudy.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM flashcards")
    flashcards = cursor.fetchall()

    connection.close()

    card_count = len(flashcards)

    return render_template(
        "cards.html",
        flashcards=flashcards,
        card_count=card_count
    )

@app.route("/cards/<int:card_id>")
def card(card_id):
    connection = sqlite3.connect("smartstudy.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM flashcards WHERE id = ?",
        (card_id,)
    )

    flashcard = cursor.fetchone()

    connection.close()

    if flashcard is None:
        return "Flashcard not found.", 404

    return render_template(
        "card.html",
        flashcard=flashcard
    )

@app.route("/create-card", methods=["GET", "POST"])
def create_card():
    if request.method == "POST":
        question = request.form["question"]
        answer = request.form["answer"]
        topic = request.form["topic"]

        connection = sqlite3.connect("smartstudy.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO flashcards (question, answer, topic) VALUES (?, ?, ?)",
            (question, answer, topic)
        )

        connection.commit()
        connection.close()

    return render_template("create_card.html")


@app.route("/study")
def study():
    connection = sqlite3.connect("smartstudy.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM flashcards LIMIT 1")
    flashcard = cursor.fetchone()

    connection.close()

    return render_template(
        "study.html",
        flashcard=flashcard
    )

@app.route("/test-form", methods=["GET", "POST"])
def test_form():

    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"

    return render_template("test_form.html")


if __name__ == "__main__":
    app.run(debug=True)