# Language_Translator
Overview
This is a Python-based Translator Program that uses the Google Translate API via the googletrans library. The program allows users to translate text into various languages, set a default target language, and view a list of supported languages.
Features
1. Translate Text
    Translate any input text to a specified language.If a default target language is set, it will be automatically used for translation.The program handles translation errors gracefully, such as invalid language codes or incorrect text input.
2. Set Default Target Language
    Allows the user to set a default language code for subsequent translations.Validates language codes against the googletrans.LANGUAGES dictionary.
3. View Supported Languages
    Displays a comprehensive list of supported languages with their respective codes. Helpful for users to identify valid target languages for translation.
4. Quit Functionality
    Users can exit the program at any time by selecting the q option. Exit requires confirmation to prevent accidental closure.
How to Use
1. Run the Program
Execute the script in a Python environment to start the program.
2. Choose an Option
The program displays an interactive menu with the following options:
    1. Translate Text: Translate a custom input text to a specified or default language.
    2. Set Default Target Language: Define a preferred language code to avoid re-entering it for every translation.
    3. View Supported Languages: Get a list of supported languages and their respective codes.
    q. Quit: Exit the program after confirmation.
3. Translate Text
    Input the text you wish to translate.
    Specify a target language code (if no default is set).
    The program displays the translated text.
4. Set Default Language
    Enter a valid language code (e.g., es for Spanish, fr for French).
    The program verifies the language code and sets it as the default for subsequent translations.
5. View Supported Languages
    Select this option to display all supported languages along with their codes.
6. Quit the Program
    Enter q to exit the program.
    Confirm the exit by typing yes.
Dependencies
Python 3.6+
googletrans library: Install using:
       pip install googletrans==4.0.0-rc1

