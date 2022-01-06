import neologdn
import unicodedata
import re
import MeCab


def tokenizePre(text):
    # tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/')
    tagger = MeCab.Tagger("-Owakati")
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