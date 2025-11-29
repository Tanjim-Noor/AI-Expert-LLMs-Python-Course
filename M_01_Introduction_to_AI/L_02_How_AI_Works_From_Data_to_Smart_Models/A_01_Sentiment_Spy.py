import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for colored output
colorama.init()

# Welcome message for the program
print(f"{Fore.CYAN}🔍🎯 Welcome to Sentiment Spy! 🎯🔍{Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Enter your agent name: {Style.RESET_ALL} ").strip()
if not user_name:
    user_name = "Secret"  # Fallback if user doesn't provide a name

# Store conversation as a list of tuples: (text, polarity, sentiment_type)
conversation_history = []

print(f"\n{Fore.CYAN}Greetings, Agent {user_name}!")
print(f"Enter any sentence and I'll analyze the sentiment using TextBlob. 🧠")
print(f"Commands: {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, "
      f"or {Fore.YELLOW}'exit'{Fore.CYAN} to leave.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    # Check for commands
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}👋 Exiting Sentiment Spy. Goodbye, Agent {user_name}! 🎬{Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🔄 Conversation history has been cleared!{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No history available yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📝 Your Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # Choose color & emoji based on sentiment
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😡"
                else:
                    color = Fore.YELLOW
                    emoji = "😶"

                print(f"{idx}. {color}{emoji} {text} "
                      f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😠"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😶"

    # Store in history
    conversation_history.append((user_input, polarity, sentiment_type))

    # Print result with color, emojis, and polarity
    print(f"{color}{emoji} Sentiment: {sentiment_type}! "
          f"(Score: {polarity:.2f}){Style.RESET_ALL}")