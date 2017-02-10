import jieba
import json

import codecs

import sys

class Segment(object):
    def __init__(self, filename):
        self.filename = filename
        self.data = dict(uid = [], mid = [], time = [], forward_count = [], comment_count = [], like_count = [], raw_content = [], segment_content = [])

    def preprocess(self):
        with open(self.filename, 'r') as f:
            raw_data = f.read().decode('utf-8')

        records = raw_data.split('\n')

        c = 0
        for record in records:
            c = c + 1
            record = record.split('\t')
            if len(record) == 1:
                continue

            self.data['uid'].append(record[0])
            self.data['mid'].append(record[1])
            self.data['time'].append(record[2])
            self.data['forward_count'].append(0)
            self.data['comment_count'].append(0)
            self.data['like_count'].append(0)
            self.data['raw_content'].append(record[3])


    def segment(self):
        raw_content = self.data['raw_content']
        for content in raw_content:
            g = jieba.cut(content)

            temp = []
            for word in g:
                temp.append(word)

            self.data['segment_content'].append(temp)

        with open("./mid-data/data.json", 'w') as f:
            json.dump(self.data, f)



if __name__ == "__main__":
    segment = Segment("./mid-data/part-raw-data.txt")
    segment.preprocess()
    segment.segment()
