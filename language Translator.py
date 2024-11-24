from googletrans import Translator, LANGUAGES
translator = Translator()
default_language = None
while True:
    print(" --- Translator Program ---")
    choice = input("Options:\n"
                   "1. Translate Text\n"
                   "2. Set Default Target Language\n"
                   "3. View Supported Languages\n"
                   "q. Quit\n"
                   "Enter your choice:\n").strip().lower()
    if choice == 'q':
        confirm_exit = input("Are you sure you want to exit? Type 'yes' to confirm or 'no' to return: ").lower()
        if confirm_exit == 'yes':
            print("-------Goodbye!-------")
            break
        else:
            continue
    elif choice == '1':
        if not default_language:
            target_language = input("Enter the target language code (e.g., 'ur' for Urdu)\n")
        else:
            target_language = default_language
            print(f"Using default language code: {default_language}")
        text_to_translate = input("Enter the text to translate:\n")
        try:
            translated = translator.translate(text_to_translate, dest=target_language)
            print(f"\nTranslated Text ({target_language}):\n{translated.text}\n")
        except Exception as e:
            print(f"Error: {e}. Please check the language code or the input text.\n")
    elif choice == '2':
        default_language = input("Enter the target language code to set as default (e.g., 'ur' ")
        if default_language in LANGUAGES:
            print(f"Default language set to: {LANGUAGES[default_language].title()} ({default_language})\n")
        else:
            print("Invalid language code. Please try again:( \n")
            default_language = None
    elif choice == '3':
        print("\nSupported Languages:")
        for code, language in LANGUAGES.items():
            print(f"{code}: {language.title()}")
        print()
    else:
        print("Invalid choice. Please select a valid option:( \n")
