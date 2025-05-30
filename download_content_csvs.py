import os
import pandas

# Supported languages: https://github.com/elimu-ai/model/blob/main/src/main/java/ai/elimu/model/v2/enums/Language.java
languages = [
    'ENG',
    'HIN',
    'TGL',
    'THA',
    'VIE'
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

    words_csv_url = f'http://{language.lower()}.elimu.ai/content/word/list/words.csv'
    print(f'words_csv_url: {words_csv_url}')
    words_dataframe = pandas.read_csv(words_csv_url)
    print(f'words_dataframe: \n{words_dataframe}')
    words_file_path = f'lang-{language}/words.csv'
    print(f'words_file_path: {words_file_path}')
    words_dataframe.to_csv(words_file_path, index=False)

    numbers_csv_url = f'http://{language.lower()}.elimu.ai/content/number/list/numbers.csv'
    print(f'numbers_csv_url: {numbers_csv_url}')
    numbers_dataframe = pandas.read_csv(numbers_csv_url)
    print(f'numbers_dataframe: \n{numbers_dataframe}')
    numbers_file_path = f'lang-{language}/numbers.csv'
    print(f'numbers_file_path: {numbers_file_path}')
    numbers_dataframe.to_csv(numbers_file_path, index=False)

    emojis_csv_url = f'http://{language.lower()}.elimu.ai/content/emoji/list/emojis.csv'
    print(f'emojis_csv_url: {emojis_csv_url}')
    emojis_dataframe = pandas.read_csv(emojis_csv_url)
    print(f'emojis_dataframe: \n{emojis_dataframe}')
    emojis_file_path = f'lang-{language}/emojis.csv'
    print(f'emojis_file_path: {emojis_file_path}')
    emojis_dataframe.to_csv(emojis_file_path, index=False)

    images_csv_url = f'http://{language.lower()}.elimu.ai/content/image/list/images.csv'
    print(f'images_csv_url: {images_csv_url}')
    images_dataframe = pandas.read_csv(images_csv_url)
    print(f'images_dataframe: \n{images_dataframe}')
    images_file_path = f'lang-{language}/images.csv'
    print(f'images_file_path: {images_file_path}')
    images_dataframe.to_csv(images_file_path, index=False)

    storybooks_csv_url = f'http://{language.lower()}.elimu.ai/content/storybook/list/storybooks.csv'
    print(f'storybooks_csv_url: {storybooks_csv_url}')
    storybooks_dataframe = pandas.read_csv(storybooks_csv_url)
    print(f'storybooks_dataframe: \n{storybooks_dataframe}')
    storybooks_file_path = f'lang-{language}/storybooks.csv'
    print(f'storybooks_file_path: {storybooks_file_path}')
    storybooks_dataframe.to_csv(storybooks_file_path, index=False)

    videos_csv_url = f'http://{language.lower()}.elimu.ai/content/video/list/videos.csv'
    print(f'videos_csv_url: {videos_csv_url}')
    videos_dataframe = pandas.read_csv(videos_csv_url)
    print(f'videos_dataframe: \n{videos_dataframe}')
    videos_file_path = f'lang-{language}/videos.csv'
    print(f'videos_file_path: {videos_file_path}')
    videos_dataframe.to_csv(videos_file_path, index=False)
