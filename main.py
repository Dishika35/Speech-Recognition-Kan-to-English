import speech_recognition as sr
from googletrans import Translator

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to recognize Kannada speech and translate it into English
def translate_kannada_to_english():
    translator = Translator()
    with sr.Microphone() as inputs:
        print("Please speak in Kannada now")
        listening = recognizer.listen(inputs)
        print("Analysing...")
        try:
            kannada_text = recognizer.recognize_google(listening, language="kn-IN")
            print("You said in Kannada:", kannada_text)
            # Translate Kannada text to English
            english_text = translator.translate(kannada_text, src="kn", dest="en").text
            print("Translated to English:", english_text)
            return english_text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said in Kannada.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Main function
if __name__ == "__main__":
    translated_text = translate_kannada_to_english()
