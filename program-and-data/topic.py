import jieba
import jieba.analyse
import json

import codecs

class TopicExtractor(object):
    def __init__(self, filename, txt_filename):
        self.filename = filename
        self.txt_filename = txt_filename

        with open(self.filename, 'r') as f:
            self.feature_data = json.load(f)

        self.topic_word = []

    def extract(self):
        contents = self.feature_data['raw_content']
        for content in contents:
            self.topic_word.append(jieba.analyse.extract_tags(content, topK=5, withWeight=False, allowPOS=()))

    def save(self):
        self.feature_data['topic-word'] = self.topic_word
        with open(self.filename, 'w') as f:
            json.dump(self.feature_data, f)

        f.close()

        with open(self.txt_filename, 'w') as f:
            for i in range(len(self.feature_data['uid'])):
                f.writelines([self.feature_data['mid'][i], '\t',
                              self.feature_data['time'][i], '\t',
                              str(self.feature_data['forward_count'][i]), '\t',
                              str(self.feature_data['comment_count'][i]), '\t',
                              str(self.feature_data['like_count'][i]), '\t',
                              self.feature_data['raw_content'][i].encode('utf-8'), '\t',
                              str(self.feature_data['chinese-word-number'][i]), '\t',
                              str(self.feature_data['english-word-number'][i]), '\t',
                              str(self.feature_data['digit-number'][i]), '\t',
                              str(self.feature_data['question-mark-number'][i]), '\t',
                              str(self.feature_data['exclamation-mark-number'][i]), '\t',
                              str(self.feature_data['quotation-mark-number'][i]), '\t',
                              str(self.feature_data['bracket-mark-number'][i]), '\t',
                              str(self.feature_data['at-mark-number'][i]), '\t',
                              str(self.feature_data['numbersign-mark-number'][i]), '\t',
                              str(self.feature_data['link-number'][i]), '\t',
                              '/'.join(self.feature_data['topic-word'][i]).encode('utf-8'), '\n'
                              ])



if __name__ == "__main__":
    topic_extractor = TopicExtractor("./mid-data/feature_data.json")
    topic_extractor.extract()
    topic_extractor.save()
