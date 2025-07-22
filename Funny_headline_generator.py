import random

subjects = [
    "Angry cat", "Dancing grandma", "Invisible man", "Talking dog", "Flying toaster",
    "Alien tourist", "Confused chicken"
]

actions = [
    "steals", "eats", "sings to", "argues with", "throws", "paints", "challenges"
]

doings_places = [
    "a microwave in public", "a statue of liberty", "the moon’s shadow",
    "a bowl of cereal", "at a yoga class", "on live TV", "during a wedding"
]

def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(doings_places)
    return f"{subject} {action} {place}!"

# Loop to keep generating headlines
while True:
    print("\nGenerated Headline:")
    print(generate_headline())

    user_input = input("\nDo you want to generate another headline? (yes/no): ").strip().lower()
    if user_input != "yes":
        print("Okay, no more headlines. Bye!")
        break
