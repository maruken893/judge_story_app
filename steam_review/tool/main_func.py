import pandas as pd
# from .tokenizer import tokenizePre
import neologdn
import unicodedata
import re
import MeCab
import numpy as np




keywords = list(pd.read_csv('steam_review/tool/dictionary/keyword.csv')['keyword'])
positive_words = list(pd.read_csv('steam_review/tool/dictionary/dic.csv')['positive'])
negative_words = list(pd.read_csv('steam_review/tool/dictionary/dic.csv')['negative'])




def tokenizePre(text):
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    text = neologdn.normalize(text)
    text = unicodedata.normalize('NFKC', text)
    text = text.lower()
    text = re.sub(r'\d+', 'SOMENUMBER', text)

    node = tagger.parseToNode(text)

    results = []

    while node:
        features = node.feature.split(',')
        if features[0] != 'BOS/EOS':
            if features[0] not in ['助詞', '助動詞']:
                token = features[6] if features[6] != '*' else node.surface
                results.append(token)

        node = node.next

    return results



def scoreing(reviews):
    splited_dic = {}
    for i, review in enumerate(reviews):
        splited_sentences = []
        splited_sentences.append(str(review).split('。'))
        splited_dic[i]= splited_sentences

    review_wakati = {}
    story_state = {}

    for i in splited_dic.keys():
        texts_list = splited_dic[i]
        review_wakati[i] = []
        for texts in texts_list:
            for text in texts:
                review_wakati[i].append(tokenizePre(text))



    sentences = {}
    for i in review_wakati.keys():

        sentences[i] = []
        sentence = []
        story_state[i] = []
        for words in review_wakati[i]:
            keyword_flag = False
            feature_flag = False
            score = 0
            for num, word in enumerate(words):
                if word in keywords:
                    sentence.append(word)
                    keyword_flag = True
                elif word in positive_words:
                    #

                    sentence.append(word)
                    feature_flag = True
                    negative_flag = False
                    if num - len(words) >= 3:
                        for i in range(num, num + 3):
                            if words[i] == 'ない':
                                score -= 1
                                negative_flag =  not negative_flag
                    else:
                        for ind in range(num, len(words)):
                            if words[ind] == 'ない':
                                score -= 1
                                negative_flag = not negative_flag


                    if negative_flag == False:
                        score += 1

                #
                elif word in negative_words:
                    sentence.append(word)
                    feature_flag = True

                    #

                    positive_flag = False
                    if num - len(words) >= 3:
                        for i in range(num, num + 3):
                            if words[i] == 'ない':
                                score += 1
                                positive_flag = not positive_flag
                    else:
                        for ind in range(num, len(words)):
                            if words[ind] == 'ない':
                                score += 1
                                positive_flag = not positive_flag

                    if positive_flag == False:
                        score -= 1

                    #
            if keyword_flag == True and feature_flag == True:
                sentences[i].append(sentence)
                if score >= 1:
                    story_state[i].append(1)
                elif score <= 0:
                    story_state[i].append(-1)
            else:
                story_state[i].append(0)
                sentences[i].append([])

    for i, review in story_state.items():
        story_state[i] = int(np.sum(review))
        if story_state[i] >= 1:
            story_state[i] = 1
        elif story_state[i] == 0:
            story_state[i] = 0
        else:
            story_state[i] = -1

    return story_state
