# aifile/filely.py
from aifile.file_manager import FileManager
import numpy as np
import speech_recognition as sr

def text_search(file_manager, query):
    # Placeholder for text-based search functionality
    # Implement your logic for text search based on the user's query
    print(f"Performing text search for: {query}")
    # Example: list files that contain the query in their names
    matching_files = [file for file in file_manager.list_files() if query.lower() in file.lower()]
    print("Matching files:")
    print(matching_files)

def voice_search(file_manager):
    # Voice-based search using SpeechRecognition
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something for voice search:")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio).lower()
        print(f"Voice search query: {query}")
        text_search(file_manager, query)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def main():
    # Create an instance of the FileManager
    file_manager = FileManager()

    print("Welcome to AIFile - Your Intelligent File Management and Chatbot!")

    while True:
        print("\nAIFile Menu:")
        print("1. Text Search")
        print("2. Voice Search")
        print("3. Delete Temporary Files")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            query = input("Enter text for search: ")
            text_search(file_manager, query)
        elif choice == '2':
            voice_search(file_manager)
        elif choice == '3':
            print("Deleting temporary files...")
            file_manager.delete_temporary_files()
            print("Temporary files deleted successfully!")
        elif choice == '4':
            print("Exiting AIFile. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            
if __name__ == "__main__":
    main()
