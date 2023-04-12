import json
import re
from utils import constants

# Compare with json dictionary
# TODO Pop un-matching words

# Init vars
isDone = False
initialTry = True
PATTERNS = [constants.PATTERN_PREFIX for _ in range(5)]

# Load pre-computed answer set
word_dictionary = dict()
with open(constants.ANSWER_SET_FILE_NAME) as json_file:
    word_dictionary = json.load(json_file)

# Prompt user until finished
while True:
    # Get known letters so far
    hint = ''
    if initialTry:
        hint = input(constants.PROMPT_INITIAL_TRY).strip()
    else:
        hint = input(constants.PROMPT).strip()

    # Check for good input
    while len(hint) != 5 or hint.isalnum():
        print(constants.WRONG_INPUT_WARNING)
        hint = input(constants.PROMPT_INITIAL_TRY).strip()
    PATTERN_COUNT = hint.count('_')
    UNDERSCORE_INDICES = []
    for i, char in enumerate(hint):
        if char == '_':
            UNDERSCORE_INDICES.append(i)

    # Get Omitted Characters
    omit_chars_lst = list()
    if initialTry:
        omit_chars_lst = input('''Enter known, omitted letters in a space_separated list.
For letters that are not completely omitted, but have known omitted positions put in the form:
    c[0,1,...,5] where c is a character (i.e. a c[1,2] z)

Omitted Letters: ''')
    else:
        omit_chars_lst = input('''Enter NEW, known, omitted letters in a space_separated list.
For letters that are not completely omitted, but have known omitted positions put in the form:
c[0,1,...,5] where c is a character (i.e. a c[1,2] z)

Omitted Letters: ''')

    # TODO make infinite loop that will input the characters if 
    # TODO the answer was incorrect into the patterns automatically, and keep
    # TODO the program alive until the puzzle is completed
    # Add chars to pattern
    if initialTry:
        for char in omit_chars_lst.split(' '):
            if '[' in char:
                for i in char[2:-1].split(','):
                    ch = char[0]
                    if PATTERNS[int(i)].find(ch) == -1:
                        print("index" + i + " char: " + ch)
                        PATTERNS[int(i)] += ch 
                        # TODO make pattern for non-ommitted i.e. ([^ab]|[ch])
            else:
                for i in UNDERSCORE_INDICES:
                    if PATTERNS[i].find(char) == -1: 
                        PATTERNS[i] += char
    else:
        # TODO Merge new known letters to patterns
        pass


    for i in range(5):
        PATTERNS[i] += ']'

    print(f"PATTERNS: {PATTERNS}")

    hint_pattern = ''
    for i, char in enumerate(hint):
        if char == '_':
            for char in PATTERNS[i]:
                hint_pattern += char
        else: hint_pattern += hint[i]

    # debug print
    print("hint_pattern: " + hint_pattern)
    # if hint.find('_') != -1 : hint_pattern = hint.replace("_", PATTERN)
    # else: hint_pattern = hint.replace(" ", PATTERN)

    print(constants.SUGGESTIONS_HEADER)
    discard_words = []
    for word, freq in word_dictionary.items(): 
        if re.match(hint_pattern, word):
            print(f"\nword: {word}\nscore: {freq}\n-------")
        else:
            discard_words.append(word)
    
    # pop unmatching words
    for word in discard_words: word_dictionary.pop(word)
    
    isDone = True if input(constants.PLAY_AGAIN_PROMPT) == 'y' else False
    if isDone: 
        print("Hope you won :)")
        exit()
    initialTry = False