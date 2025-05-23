from flask import Flask, request, render_template

app = Flask(__name__)

# Dummy Q&A dictionary
dummy_qa = {
    "What is an antibiotic?": "An antibiotic is a medicine that helps fight infections caused by bacteria.",
    "What is diabetes?": "Diabetes is a chronic condition that affects how your body turns food into energy.",
    "How to treat a cold?": "Rest, drink plenty of fluids, and take over-the-counter medicines to relieve symptoms.",
}

def generate_response(prompt):
    for question, answer in dummy_qa.items():
        if prompt.strip().lower() == question.lower():
            return answer
    return "Sorry, I don't have an answer for that question."

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        response = generate_response(prompt)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
