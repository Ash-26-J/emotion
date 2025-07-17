import re
import os

def check_emotional_content(emotion_keywords_filepath, input_text_filepath):
    """
    Checks if a given text file contains emotional words based on a
    dictionary from another file.

    Args:
        emotion_keywords_filepath (str): The absolute path to the text file
                                         containing emotional keywords,
                                         one word per line.
        input_text_filepath (str): The absolute path to the text file containing
                                   the paragraph to be analyzed.

    Returns:
        int: 1 if emotional words are found, 0 otherwise.
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

    # 2. Read input paragraph
    input_paragraph = ""
    try:
        with open(input_text_filepath, 'r', encoding='utf-8') as f:
            input_paragraph = f.read().lower() # Convert to lowercase for case-insensitive comparison
    except FileNotFoundError:
        print(f"Error: Input text file not found at '{input_text_filepath}'.")
        print("Please ensure your input paragraph file (e.g., 'input_paragraph.txt') is uploaded to /content/ in Colab, or manually created.")
        return 0
    except Exception as e:
        print(f"Error reading input text file: {e}")
        return 0

    # 3. Process the paragraph and check for emotional words
    # Use regex to find all words (alphanumeric sequences) in the paragraph
    # This also handles punctuation by effectively ignoring it for word extraction
    words_in_paragraph = set(re.findall(r'\b\w+\b', input_paragraph)) # \b for word boundaries

    # Check for intersection between paragraph words and emotional words
    # If there's at least one common word, it's considered emotional
    if words_in_paragraph.intersection(emotional_words):
        return 1
    else:
        return 0

if __name__ == "__main__":
    # Define the absolute path to your emotion keywords file in Colab
    emotion_file_path = "/content/emotion_words.txt"

    # Define the absolute path to your input text file in Colab.
    # You should upload your file to Colab's /content/ directory,
    # or specify the path if you've mounted Google Drive.
    # For demonstration, we'll suggest a default name.
    input_file_path = "/content/input_paragraph.txt" # Change this if your file has a different name

    print("\n--- Emotional Text Analyzer for Google Colab ---")
    print("This script checks if a text file contains emotional words from a predefined dictionary.")
    print(f"Expecting emotion keywords from: {emotion_file_path}")
    print(f"Expecting input paragraph from: {input_file_path}")

    # --- Colab File Setup for Demonstration (Optional but helpful for first run) ---
    # This block creates dummy files if they don't exist.
    # In a real scenario, you'd replace their content or upload your own.
    if not os.path.exists(emotion_file_path):
        print(f"\nCreating a dummy emotion keywords file at '{emotion_file_path}' for demonstration.")
        print("ACTION REQUIRED: Please edit this file in Colab's file browser with your actual emotional words.")
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

    if not os.path.exists(input_file_path):
        print(f"Creating a dummy input paragraph file at '{input_file_path}' for demonstration.")
        # FIX: Corrected the unterminated string literal here
        print("ACTION REQUIRED: You can edit this file or upload your own text file to /content/ and rename it to 'input_paragraph.txt'.")
        with open(input_file_path, 'w', encoding='utf-8') as f:
            f.write("I am feeling very happy today. This brings me great joy and excitement!\n")
            f.write("The weather is quite neutral and calm. Nothing special is happening.\n")
    # --- End Colab File Setup ---

    # Run the check
    result = check_emotional_content(emotion_file_path, input_file_path)

    # Print the final output
    print(f"\nOutput: {result}")
    if result == 1:
        print("The input text contains emotional words based on the dictionary.")
    else:
        print("The input text does NOT contain emotional words based on the dictionary.")
