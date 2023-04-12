import json
import datamuse
import time

datamuse_api = datamuse.Datamuse();
datamuse_api.set_max_default(1);

word_freq_dict = dict()
sorted_word_freq_dict = dict()

with open("allowed_wordle_words.txt") as txt_file:
    # i = 0
    for key in txt_file.read().split('\n'):
        # if i == 20:
        #     break
        try:
            # print(key)
            api_response_dict = datamuse_api.words(sp=key, md='f').pop()
            word_freq_dict[key] = float(api_response_dict['tags'].pop()[2:]) if api_response_dict['word'] == key else 0.0
        except IndexError:
            #print(key)
            word_freq_dict[key] = 0.0
        time.sleep(0.01)
        # i += 1

with open("words_freq_dict_five.json", 'w') as json_out:
    sorted_word_freq_dict = {k: v for k, v in sorted(word_freq_dict.items(), key=lambda item: item[1], reverse=True)}
    json.dump(sorted_word_freq_dict, json_out, indent=4)

 