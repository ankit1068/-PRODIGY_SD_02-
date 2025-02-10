from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global number_to_guess
    data = request.get_json()
    user_guess = data.get('guess')

    if user_guess < number_to_guess:
        return jsonify({"message": "Too low! Try again.", "correct": False})
    elif user_guess > number_to_guess:
        return jsonify({"message": "Too high! Try again.", "correct": False})
    else:
        return jsonify({"message": f"🎉 Congratulations! You guessed the number {number_to_guess}.", "correct": True})

if __name__ == "__main__":
    app.run(debug=True)
