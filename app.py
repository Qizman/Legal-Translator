from flask import Flask, render_template, request
import oAI

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#route to create connection to chatgpt
@app.route('/chat', methods=['POST'])
def chat():
    return "test complete"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')