from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/cards")
def cards():
    card_count = 12

    return render_template(
        "cards.html",
        card_count=card_count
    )

@app.route("/cards/<int:card_id>")
def card(card_id):
    return f"You are viewing flashcard {card_id}."

@app.route("/cards/create", methods=["GET", "POST"])
def create_card():

    if request.method == "POST":

        question = request.form["question"]
        answer = request.form["answer"]
        topic = request.form["topic"]

        print("Question:", question)
        print("Answer:", answer)
        print("Topic:", topic)

        return "Flashcard received!"

    return render_template("create_card.html")


@app.route("/study")
def study():
    return render_template("study.html")

@app.route("/test-form", methods=["GET", "POST"])
def test_form():

    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}!"

    return render_template("test_form.html")


if __name__ == "__main__":
    app.run(debug=True)