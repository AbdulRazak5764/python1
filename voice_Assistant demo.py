import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

# Initialize speech engine globally
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Recognizer
r = sr.Recognizer()

# Data dictionaries
phone_numbers = {
    "chicha": "9381631552",
    "razak": "8919701520",
    "riyaz": "8328006647",
    "dad": "9381785463",
    "siddique": "9908092736"
}

bank_account_numbers = {
    "SBI": "23456789987",
    "Andhrabank": "34567903456",
    "icici": "45678934502"
}

# Function to speak a command
def speak(command):
    engine.say(command)
    engine.runAndWait()

# Function to process voice commands
def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('listening... Ask now...')
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin).lower()
            print(my_text)

            # Exit command
            if 'exit' in my_text:
                speak("Goodbye!")
                exit()  # Exits the program

            # Play song
            elif 'play' in my_text:
                song = my_text.replace('play', '').strip()
                speak(f'Playing {song}')
                pywhatkit.playonyt(song)

            # Get today's date
            elif 'date' in my_text:
                today = datetime.date.today().strftime("%B %d, %Y")
                speak(f"Today's date is {today}")

            # Get current time
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%H:%M')
                speak(f"The time is {timenow}")

            # Get details about a person
            elif 'tell about' in my_text:
                person = my_text.replace('tell about', '').strip()
                info = wikipedia.summary(person, sentences=1)
                speak(info)

            # Get phone numbers
            elif 'phone number' in my_text:
                for name in phone_numbers:
                    if name in my_text:
                        speak(f"{name}'s phone number is {phone_numbers[name]}")
                        break
                else:
                    speak("I couldn't find that name in your phone list.")

            # Get bank account numbers
            elif 'account number' in my_text:
                for bank in bank_account_numbers:
                    if bank.lower() in my_text:
                        speak(f"{bank}'s account number is {bank_account_numbers[bank]}")
                        break
                else:
                    speak("I couldn't find that bank in your list.")

            # Unrecognized commands
            else:
                speak("I didn't understand that. Please ask a correct question.")

    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        speak(f"Could not request results; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("An error occurred while processing your request.")

# Start the system
speak("Welcome to the project")
while True:
    commands()

