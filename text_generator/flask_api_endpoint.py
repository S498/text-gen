from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    prompt = preprocess_text(data.get('prompt', ''))
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Integrate safety module here
    safe_text = filter_harmful_content(generated_text)
    return jsonify({"generated_text": safe_text})

def filter_harmful_content(text):
    # Implement your safety filter logic here
    return text

if __name__ == "__main__":
    app.run(debug=True)
