# from flask import Flask, request, jsonify
# from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelForSeq2SeqLM, AutoModel
# from flask_cors import CORS
# import nltk
# from nltk.tokenize import word_tokenize
# import torch

# # Download NLTK data
# nltk.download('punkt')

# # Initialize the model and tokenizer
# model_name = "google/gemma-2b"  # Update with the correct model name if different
# device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

# try:
#     # Uncomment the appropriate model type
#     model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
#     # model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
#     # model = AutoModel.from_pretrained(model_name).to(device)
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
# except ValueError as e:
#     print(f"Error loading model: {e}")

# # Initialize Flask app
# app = Flask(__name__)
# CORS(app)

# # Preprocessing function
# def preprocess_text(text):
#     tokens = word_tokenize(text)
#     cleaned_text = " ".join(tokens)
#     return cleaned_text

# # Safety filter function
# def filter_harmful_content(text):
#     # Implement your safety filter logic here
#     return text

# # API endpoint
# @app.route('/generate', methods=['POST'])
# def generate_text():
#     data = request.json
#     print(request.json, 'request in backend')
#     prompt = preprocess_text(data.get('prompt', ''))
#     inputs = tokenizer(prompt, return_tensors="pt").to(device)
    
#     with torch.no_grad():
#         outputs = model.generate(inputs.input_ids, max_length=2000)
    
#     generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
#     # Integrate safety module here
#     safe_text = filter_harmful_content(generated_text)
#     return jsonify({"generated_text": safe_text})

# # Main function
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5001, debug=True)


# import os
# from flask import Flask, request, jsonify
# from transformers import AutoModelForCausalLM, AutoTokenizer
# from flask_cors import CORS
# import nltk
# from nltk.tokenize import word_tokenize
# import torch

# # Set environment variable for MPS memory management
# os.environ['PYTORCH_MPS_HIGH_WATERMARK_RATIO'] = '0.0'

# # Download NLTK data
# nltk.download('punkt')

# # Initialize the model and tokenizer
# model_name = "cognitivecomputations/samantha-mistral-7b"  # Update with the correct model name if different
# device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

# try:
#     model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
#     tokenizer = AutoTokenizer.from_pretrained(model_name)
# except ValueError as e:
#     print(f"Error loading model: {e}")

# # Initialize Flask app
# app = Flask(__name__)
# CORS(app)

# # Preprocessing function
# def preprocess_text(text):
#     tokens = word_tokenize(text)
#     cleaned_text = " ".join(tokens)
#     return cleaned_text

# # Safety filter function
# def filter_harmful_content(text):
#     # Implement your safety filter logic here
#     return text

# # API endpoint
# @app.route('/generate', methods=['POST'])
# def generate_text():
#     data = request.json
#     print(request.json, 'request in backend')
#     prompt = preprocess_text(data.get('prompt', ''))
#     inputs = tokenizer(prompt, return_tensors="pt").to(device)
    
#     try:
#         with torch.no_grad():
#             outputs = model.generate(inputs.input_ids, max_length=2000)
#     except RuntimeError as e:
#         print(f"RuntimeError during generation: {e}")
#         return jsonify({"error": "Memory error during text generation"}), 500
    
#     generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
#     # Integrate safety module here
#     safe_text = filter_harmful_content(generated_text)
#     return jsonify({"generated_text": safe_text})

# # Main function
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5001, debug=True)


import os
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask_cors import CORS
import nltk
from nltk.tokenize import word_tokenize
import torch

# Set environment variables
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
os.environ['PYTORCH_MPS_HIGH_WATERMARK_RATIO'] = '0.0'

# Download NLTK data
nltk.download('punkt')

# Initialize the model and tokenizer
model_name = "google/gemma-2b"  # Update with the correct model name if different
# device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
device = 'cpu'

try:
    model = AutoModelForCausalLM.from_pretrained(model_name).to(device)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
except ValueError as e:
    print(f"Error loading model: {e}")

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Preprocessing function
def preprocess_text(text):
    tokens = word_tokenize(text)
    cleaned_text = " ".join(tokens)
    return cleaned_text

# Safety filter function
def filter_harmful_content(text):
    # Implement your safety filter logic here
    return text

# API endpoint
@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    print(request.json, 'request in backend')
    prompt = preprocess_text(data.get('prompt', ''))
    inputs = tokenizer(prompt, return_tensors="pt")
    
    # Add attention_mask
    inputs = {key: value.to(device) for key, value in inputs.items()}
    
    with torch.no_grad():
        outputs = model.generate(inputs['input_ids'], attention_mask=inputs['attention_mask'], max_length=2000)
    
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Integrate safety module here
    safe_text = filter_harmful_content(generated_text)
    return jsonify({"generated_text": safe_text})

# Main function
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
