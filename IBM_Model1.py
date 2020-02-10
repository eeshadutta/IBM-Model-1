import pickle


def create_corpus(source_lang_file, target_lang_file):
    sentence_pairs = []
    e_file = open(target_lang_file, "r")
    f_file = open(source_lang_file, "r")
    e_sentences = e_file.readlines()
    f_sentences = f_file.readlines()

    for e_s, f_s in zip(e_sentences, f_sentences):
        s_pair = {'e': e_s, 'f': f_s}
        sentence_pairs.append(s_pair)

    e_file.close()
    f_file.close()

    return sentence_pairs


def create_vocabulary(sentence_pairs):
    e_words_set = set()
    f_words_set = set()
    for pair in sentence_pairs:
        for word in pair['e'].split():
            e_words_set.add(word)
        for word in pair['f'].split():
            f_words_set.add(word)
    words = {'e': e_words_set, 'f': f_words_set}
    return words


def train_model(sentence_pairs):
    words = create_vocabulary(sentence_pairs)
    e_words_size = len(words['e'])
    f_words_size = len(words['f'])

    translation_prob = {}

    num_iterations = 20
    curr_iteration = 1
    while curr_iteration <= num_iterations:
        print("Iteration number:", curr_iteration)
        count = {}
        total = {f_word: 0 for f_word in words['f']}

        s_total = {e_word: 0 for e_word in words['e']}
        for pair in sentence_pairs:
            for e_word in pair['e'].split():
                if e_word not in translation_prob:
                    translation_prob[e_word] = {}
                if e_word not in count:
                    count[e_word] = {}
                s_total[e_word] = 0
                for f_word in pair['f'].split():
                    if f_word not in translation_prob[e_word]:
                        translation_prob[e_word][f_word] = 1 / f_words_size
                    if f_word not in count[e_word]:
                        count[e_word][f_word] = 0
                    s_total[e_word] += translation_prob[e_word][f_word]

            for e_word in pair['e'].split():
                for f_word in pair['f'].split():
                    count[e_word][f_word] += translation_prob[e_word][f_word] / \
                        s_total[e_word]
                    total[f_word] += translation_prob[e_word][f_word] / \
                        s_total[e_word]

        for e_word in translation_prob:
            for f_word in translation_prob[e_word]:
                translation_prob[e_word][f_word] = count[e_word][f_word] / \
                    total[f_word]

        curr_iteration += 1

    # for e in translation_prob:
    #     for f in translation_prob[e]:
    #         if translation_prob[e][f] > 0.1:
    #             print(e, f, translation_prob[e][f])

    return translation_prob


def main():
    data_directory = './Data'
    source_lang_file = './Data/train.hi'
    target_lang_file = './Data/train.en'

    sentence_pairs = create_corpus(source_lang_file, target_lang_file)
    translation_prob = train_model(sentence_pairs)

    outfile = open("translation_probablities", "wb")
    pickle.dump(translation_prob, outfile)
    outfile.close()


if __name__ == '__main__':
    main()
