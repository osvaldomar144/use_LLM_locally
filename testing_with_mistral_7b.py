from transformers import AutoModelForSequenceClassification
import torch

# Caricare il modello
model = AutoModelForSequenceClassification.from_pretrained("jncraton/Mistral-7B-Instruct-v0.2-ct2-int8")

# Preprocessare i dati
tokenizer = model.config.tokenizer
input_ids = tokenizer.encode("Ciao mondo!")

# Eseguire il modello
outputs = model(input_ids)

# Ottenere i risultati
logits = outputs.logits

# Use PyTorch's softmax function
probabilities = torch.nn.functional.softmax(logits, dim=1)

# Stampare i risultati
print(probabilities)
