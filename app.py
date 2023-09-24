from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = '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'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    
    response = openai.Completion.create(
      engine="davinci",
      prompt=message,
      max_tokens=150
    )
    
    return jsonify({'response': response.choices[0].text.strip()})


if __name__ == '__main__':
    app.run(debug=True)


from flask_cors import CORS

...

CORS(app)
