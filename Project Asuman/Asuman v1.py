import json
import random

with open("responses.txt", "r", encoding="utf-8") as f:
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

with open("conversation.txt", "a", encoding="utf-8") as f:
    while True:
        user_input = get_input()

        if user_input == "öğret":
            new_input = input("Ne öğretmek istersin? ")
            new_response = input("Ne cevap vermeliyim? ")
            responses[new_input] = [new_response]
            print("Öğrettin! Ne yapmak istersin?")
            continue

        if user_input == "güle güle":
            response = random.choice(responses["güle güle"])
            print(response)
            inputs.append(user_input)
            inputs.append(response)
            inputs.append("")
            break

        response = generate_response(user_input)
        print(response)
        inputs.append(user_input)
        inputs.append(response)
        inputs.append("")

    print("Girdiğin şeyler:")
    for input in inputs:
        f.write(input + "\n")

    f.write(json.dumps(responses, ensure_ascii=False, indent=4))
