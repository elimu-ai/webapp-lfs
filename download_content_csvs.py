import os
import pandas

# Supported languages: https://github.com/elimu-ai/model/blob/main/src/main/java/ai/elimu/model/v2/enums/Language.java
languages = [
    'ENG',
    'HIN',
    'TGL'
]
print(f'languages: {languages}')

# Download datasets for each language
for language in languages:
    print()
    print(f'language: {language}')

    os.makedirs(f'lang-{language}', exist_ok=True)

    letters_csv_url = f'http://{language.lower()}.elimu.ai/content/letter/list/letters.csv'
    print(f'letters_csv_url: {letters_csv_url}')
    letters_dataframe = pandas.read_csv(letters_csv_url)
    print(f'letters_dataframe: \n{letters_dataframe}')
    letters_file_path = f'lang-{language}/letters.csv'
    print(f'letters_file_path: {letters_file_path}')
    letters_dataframe.to_csv(letters_file_path, index=False)

    sounds_csv_url = f'http://{language.lower()}.elimu.ai/content/sound/list/sounds.csv'
    print(f'sounds_csv_url: {sounds_csv_url}')
    sounds_dataframe = pandas.read_csv(sounds_csv_url)
    print(f'sounds_dataframe: \n{sounds_dataframe}')
    sounds_file_path = f'lang-{language}/sounds.csv'
    print(f'sounds_file_path: {sounds_file_path}')
    sounds_dataframe.to_csv(sounds_file_path, index=False)

    letter_sounds_csv_url = f'http://{language.lower()}.elimu.ai/content/letter-sound/list/letter-sounds.csv'
    print(f'letter_sounds_csv_url: {letter_sounds_csv_url}')
    letter_sounds_dataframe = pandas.read_csv(letter_sounds_csv_url)
    print(f'letter_sounds_dataframe: \n{letter_sounds_dataframe}')
    letter_sounds_file_path = f'lang-{language}/letter-sounds.csv'
    print(f'letter_sounds_file_path: {letter_sounds_file_path}')
    letter_sounds_dataframe.to_csv(letter_sounds_file_path, index=False)

    syllables_csv_url = f'http://{language.lower()}.elimu.ai/content/syllable/list/syllables.csv'
    print(f'syllables_csv_url: {syllables_csv_url}')
    syllables_dataframe = pandas.read_csv(syllables_csv_url)
    print(f'syllables_dataframe: \n{syllables_dataframe}')
    syllables_file_path = f'lang-{language}/syllables.csv'
    print(f'syllables_file_path: {syllables_file_path}')
    syllables_dataframe.to_csv(syllables_file_path, index=False)
