import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Replace 'model_name' with the name of the pre-trained model you want to use.
model_name = 'bert-base-uncased'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

keywords = [
    "banana"
    # Add more keywords as needed
]

# Tokenize the keywords
inputs = tokenizer(keywords, padding=True, truncation=True, return_tensors="pt")

# Make predictions
with torch.no_grad():
    outputs = model(**inputs)

# Get the predicted labels
predictions = torch.argmax(outputs.logits, dim=1)

category_mapping = {
    0: "Programming",
    1: "Machine Learning",
    2: "Data Science",
    3: "Artificial Intelligence",
    4: "Fruit",
    # Add more categories as needed
}

# Map the predicted label IDs to their corresponding categories
predicted_categories = [category_mapping[prediction.item()] for prediction in predictions]

print(predicted_categories)