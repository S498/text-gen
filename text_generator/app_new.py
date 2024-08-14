# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from transformers import pipeline
# from transformers import AutoModelForSeq2SeqLM
# from huggingface_hub import login

# # Authenticate with Hugging Face
# login(token="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")

# app = FastAPI()

# class Prompt(BaseModel):
#     text: str

# # Ensure the model name is correct and exists on Hugging Face
# generator = pipeline('text-generation', model='Or4cl3/Or4cl3', use_auth_token=True)

# def preprocess_text(text):
#     # Add your text preprocessing logic here
#     return text

# def filter_harmful_output(text):
#     # Add your filtering logic here
#     return text

# @app.post("/generate")
# def generate_text(prompt: Prompt):
#     processed_text = preprocess_text(prompt.text)
#     generated_text = generator(processed_text, max_length=100)[0]['generated_text']
#     filtered_text = filter_harmful_output(generated_text)
#     return {"generated_text": filtered_text}

import torch

print(torch.backends.mps.is_available())
print(torch.cuda.is_available())