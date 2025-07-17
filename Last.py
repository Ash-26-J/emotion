import re
import os

def get_first_sentence(text):
    """
    Extracts the first sentence from a given text.
    A sentence is considered to end with '.', '!', or '?'.
    """
    # Use regex to find the first occurrence of a sentence-ending punctuation.
    # re.DOTALL makes '.' match newlines as well, ensuring it works across lines.
    match = re.match(r'(.+?[.!?])(?:\s|$)', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # If no punctuation is found, consider the whole text as one sentence.
    return text.strip()

def check_emotional_first_sentence(emotion_keywords_filepath, input_text_filepath):
    """
    Checks if the first sentence of a given text file contains emotional words
    based on a dictionary from another file.

    Args:
        emotion_keywords_filepath (str): The absolute path to the text file
                                         containing emotional keywords,
                                         one word per line.
        input_text_filepath (str): The absolute path to the text file containing
                                   the paragraph to be analyzed.

    Returns:
        int: 1 if emotional words are found in the first sentence, 0 otherwise.
    """
    # 1. Read emotional keywords
    emotional_words = set()
    try:
        with open(emotion_keywords_filepath, 'r', encoding='utf-8') as f:
            for line in f:
                word = line.strip().lower()
                if word: # Add only non-empty lines
                    emotional_words.add(word)
    except FileNotFoundError:
        print(f"Error: Emotion keywords file not found at '{emotion_keywords_filepath}'.")
        print("Please ensure 'emotion_words.txt' is uploaded to /content/ in Colab, or manually created.")
        return 0
    except Exception as e:
        print(f"Error reading emotion keywords file: {e}")
        return 0

    if not emotional_words:
        print("Warning: No emotional keywords found in the dictionary file. Cannot perform check.")
        return 0

    # 2. Read input text and extract the first sentence
    full_text = ""
    try:
        with open(input_text_filepath, 'r', encoding='utf-8') as f:
            full_text = f.read() # Read full text first
    except FileNotFoundError:
        print(f"Error: Input text file not found at '{input_text_filepath}'.")
        print("Please ensure your input text file is uploaded to /content/ in Colab.")
        return 0
    except Exception as e:
        print(f"Error reading input text file: {e}")
        return 0

    if not full_text.strip():
        print("Warning: Input text file is empty. Cannot perform check.")
        return 0

    first_sentence = get_first_sentence(full_text).lower() # Get and lowercase the first sentence

    # 3. Process the first sentence and check for emotional words
    # Use regex to find all words (alphanumeric sequences) in the sentence
    words_in_first_sentence = set(re.findall(r'\b\w+\b', first_sentence))

    # Check for intersection between sentence words and emotional words
    if words_in_first_sentence.intersection(emotional_words):
        return 1
    else:
        return 0

if __name__ == "__main__":
    # Define the absolute path to your emotion keywords file in Colab
    # Ensure this file (emotion_words.txt) is uploaded to /content/
    emotion_file_path = "/content/emotion words.txt"

    # Define the absolute path to your input text file in Colab.
    # IMPORTANT: Ensure your input text file is named 'my_input_text.txt'
    # and uploaded to /content/ in Colab.
    input_file_name = "/content/Untitled Folder/75.txt" # You can change this name
    input_file_path = os.path.join("/content/", input_file_name)


    print("\n--- Emotional First Sentence Analyzer for Google Colab ---")
    print("This script checks if the *first sentence* of a text file contains emotional words.")
    print(f"Expecting emotion keywords from: {emotion_file_path}")
    print(f"Expecting input text from: {input_file_path}")

    # --- Colab File Setup Guidance ---
    print("\n--- File Setup Instructions (for Google Colab) ---")
    print("1. On the left sidebar, click the 'Files' icon (folder symbol).")
    print("2. Upload your 'emotion_words.txt' file to the `/content/` directory.")
    print("   (It should contain one emotional word per line, e.g., happy, sad, joy)")
    print(f"3. Upload your input text file (e.g., '{input_file_name}') to the `/content/` directory.")
    print("   (This file contains the paragraph/text you want to analyze.)")
    print("--------------------------------------------------\n")

    # Optional: Dummy file creation for emotion_words.txt if it doesn't exist
    if not os.path.exists(emotion_file_path):
        print(f"Warning: '{emotion_file_path}' not found. Creating a dummy file for demonstration.")
        print("Please replace its content with your actual emotional words after running.")
        with open(emotion_file_path, 'w', encoding='utf-8') as f:
            f.write("happy\n")
            f.write("sad\n")
            f.write("angry\n")
            f.write("joy\n")
            f.write("fear\n")
            f.write("love\n")
            f.write("frustration\n")
            f.write("delight\n")
            f.write("sorrow\n")
            f.write("excited\n")
            f.write("depressed\n")
            f.write("glee\n")
            f.write("anxiety\n")

    # Optional: Dummy file creation for input text if it doesn't exist
    if not os.path.exists(input_file_path):
        print(f"Warning: '{input_file_name}' not found. Creating a dummy file for demonstration.")
        print("Please replace its content with your actual paragraph after running.")
        with open(input_file_path, 'w', encoding='utf-8') as f:
            f.write("I am feeling very happy today. This brings me great joy and excitement!\n")
            f.write("However, the next part of the story is quite different. It gets complicated.\n")
            f.write("And finally, the conclusion arrived. The end.\n")


    # Run the check
    result = check_emotional_first_sentence(emotion_file_path, input_file_path)

    # Print the final output
    print(f"\nOutput: {result}")
    if result == 1:
        print("The first sentence of the input text contains emotional words based on the dictionary.")
    else:
        print("The first sentence of the input text does NOT contain emotional words based on the dictionary.")
