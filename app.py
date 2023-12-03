from flask import Flask, render_template, request

app = Flask(__name__)

import random

def generate_answer(question):
    answers = [
        "It is certain.",
        "Without a doubt.",
        "Yes, definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "No.",
        "Ask again later.",
        "Cannot predict now.",
        "Don't count on it.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    random_index = random.randint(0, len(answers) - 1)
    return answers[random_index]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_question = request.form['question']
        answer = generate_answer(user_question)
        return render_template('index.html', question=user_question, answer=answer)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
