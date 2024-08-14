from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Or4cl3/Or4cl3"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
