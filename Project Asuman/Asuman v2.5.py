import json
import random
#Made by Kerem Çağlaroğlu#
RESPONSES_FILE = "responses.txt"

with open(RESPONSES_FILE, "r", encoding="utf-8") as f:
    responses = json.load(f)

inputs = []

def get_input():
    return input("Sen: ").lower()

def generate_response(user_input):
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "Üzgünüm, anlamadım. Tekrar söyler misin?"

print("Merhaba! Ben Asuman! Ben senin sanal sevgilinim. Sana nasıl yardımcı olabilirim?")

while True:
    user_input = get_input()
    
    if user_input == "öğret":
        new_input = input("Ne öğretmek istersin? ")
        new_response = input("Ne cevap vermeliyim? ")
        responses[new_input] = [new_response]
        with open(RESPONSES_FILE, "w", encoding="utf-8") as f:
            json.dump(responses, f, ensure_ascii=False, indent=4)
        print("Öğrettin! Ne yapmak istersin?")
        continue
        
    if user_input == "güle güle":
        response = random.choice(responses["güle güle"])
        print(response)
        inputs.append(user_input)
        inputs.append(response)
        break
    
    response = generate_response(user_input)
    print(response)
    inputs.append(user_input)
    inputs.append(response)

print("Girdiğin şeyler:")
for input in inputs:
    print(input)

with open("conversation.txt", "a", encoding="utf-8") as f:
    for input in inputs:
        f.write(input + "\n")
