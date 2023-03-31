import json
import random
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

RESPONSES_FILE = "responses.txt"
FEEDBACK_FILE = "feedback.txt"

with open(RESPONSES_FILE, "r", encoding="utf-8") as f:
    responses = json.load(f)

inputs = []

def get_input():
    return input("Sen: ").lower()

def generate_response(user_input):
    tokens = nltk.word_tokenize(user_input)
    tagged = nltk.pos_tag(tokens)
    
    verb = None
    for word, pos in tagged:
        if pos.startswith('VB'):
            verb = word
            break
    
    if verb == 'öner':
        return "Teşekkür ederim! Gelişmemiz için öneriniz nedir?"
    
    if user_input in ["2", "3"]:
        return "Gelişmemiz için öneriniz nedir?"
    
    feedback = None
    if user_input == ",":
        feedback = input("Lütfen geri bildiriminizi yazın: ")
        with open(FEEDBACK_FILE, "a", encoding="utf-8") as f:
            f.write(feedback + "\n")
        return "Teşekkür ederim, geri bildiriminiz kaydedildi."
    
    words = user_input.split()
    for word in words:
        if word in responses["aggressive"]:
            return random.choice(responses["aggressive"])
        elif word in responses["lovely"]:
            return random.choice(responses["lovely"])
        elif word in responses["neutral"]:
            return random.choice(responses["neutral"])

    return "Üzgünüm, anlamadım. Tekrar söyler misin?"

print("Merhaba! Ben Asuman! Ben senin sanal sevgilinim. Sana nasıl yardımcı olabilirim?")

while True:
    user_input = get_input()
    
    response = generate_response(user_input)
    print(response)
    inputs.append(user_input)
    inputs.append(response)
    
    if user_input == "öğret":
        print("Öğretmek için önceki seçenekleri silmelisin.")
        continue
    
    elif user_input == "güle güle":
        break

print("Girdiğin şeyler:")
for input in inputs:
    print(input)

with open("conversation.txt", "a", encoding="utf-8") as f:
    for input in inputs:
        f.write(input + "\n")
