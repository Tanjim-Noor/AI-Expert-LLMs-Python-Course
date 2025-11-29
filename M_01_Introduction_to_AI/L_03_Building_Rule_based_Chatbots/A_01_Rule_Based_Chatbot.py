import re, random
from colorama import Fore, init

# Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# Destination & joke data
destinations = {
    "beaches": [
        "Bali", "Maldives", "Phuket", "Santorini", "Maui",
        "Bondi Beach", "Copacabana", "Boracay", "Goa", "Tulum"
    ],
    "mountains": [
        "Swiss Alps", "Rocky Mountains", "Himalayas", "Andes", "Dolomites",
        "Caucasus", "Atlas Mountains", "Carpathians", "Sierra Nevada"
    ],
    "cities": [
        "Tokyo", "Paris", "New York", "London", "Barcelona",
        "Singapore", "Seoul", "Dubai", "Sydney", "Rome"
    ],
    "deserts": [
        "Sahara", "Gobi", "Atacama", "Mojave", "Thar"
    ],
    "forests": [
        "Amazon", "Black Forest", "Daintree", "Białowieża", "Sinharaja"
    ]
}
jokes = [
    "Why don't programmers like nature? Too many bugs 🐛!",
    "Why did the computer visit the doctor? It caught a virus 🤒!",
    "Why do travelers always feel warm? Because of all their hot spots 🔥!",
    "I tried to catch a flight, but it had too many layovers ✈️😅!",
    "Why did the suitcase go to school? It wanted to be a smart carry-on 🎒📚!",
    "Maps are great at parties—they always know where the vibe is 🗺️🎉!",
    "Airports are so uplifting—they’re full of terminal optimism 🛫😄!",
    "Why did the tourist bring a ladder? To see high-lights of the city 🪜🏙️!",
    "The beach called—said tide and seek is on 🌊😉!",
    "I told a mountain joke, but it was too peak comedy 🏔️😆!"
]

# Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, cities, deserts, or forests? 🌊⛰️🏙️🏜️🌳")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)
    
    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion} ✨?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()
        
        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion} 🎒!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: No worries, let's try another 🔁.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: Got it, I'll suggest again 🔄.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Hmm, I don't have that type of destination 🤔.")
    
    show_help()

# Offer packing tips based on user’s destination and duration
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to 📍?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days ⏱️?")
    days = input(Fore.YELLOW + "You: ")
    
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location} 📦:")
    print(Fore.GREEN + "- Pack versatile clothes 👕.")
    print(Fore.GREEN + "- Bring chargers/adapters 🔌.")
    print(Fore.GREEN + "- Check the weather forecast 🌤️.")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

# Display help menu
def show_help():
    print(Fore.MAGENTA + "\nHere's what I can do:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommend' or 'suggest') 🌍")
    print(Fore.GREEN + "- Offer packing tips (say 'pack' or 'packing') 🧳")
    print(Fore.GREEN + "- Tell a joke (say 'joke' or 'funny') 😄")
    print(Fore.GREEN + "- Show this help menu (say 'help') ❓")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot 🤖.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}! ✈️")
    
    show_help()
    
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye 👋!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase that a bit? 🗣️")

# Run the chatbot
if __name__ == "__main__":
    chat()
