import jieba
import json

import codecs

class FeatureExtractor(object):
    def __init__(self, test_data_filename):
        with open(test_data_filename, 'r') as f:
            self.feature_data = json.load(f)

        self.chinese_word_number = [0]*len(self.feature_data['uid'])
        self.english_word_number = [0]*len(self.feature_data['uid'])
        self.digit_number = [0]*len(self.feature_data['uid'])
        self.question_mark_number = [0]*len(self.feature_data['uid'])
        self.exclamation_mark_number = [0]*len(self.feature_data['uid'])

        self.quotation_mark_number = [0]*len(self.feature_data['uid'])
        self.bracket_mark_number = [0]*len(self.feature_data['uid'])
        self.at_mark_number = [0]*len(self.feature_data['uid'])
        self.numbersign_mark_number = [0]*len(self.feature_data['uid'])
        self.link_number = [0] * len(self.feature_data['uid'])



    def counter(self):
        contents = self.feature_data['segment_content']
        for i in range(len(contents)):
            for part in contents[i]:
                #chinese_word
                if self.is_all_chinese(part):
                    self.chinese_word_number[i] = self.chinese_word_number[i] + len(part)

                #
                elif self.is_all_letter(part):
                    self.english_word_number[i] = self.english_word_number[i] + 1
                    if self.is_link(part):
                        self.link_number[i] = self.link_number[i] + 1

                #
                elif self.is_all_digit(part):
                    self.digit_number[i] = self.digit_number[i] + len(part)

                #
                elif self.is_question_mark(part):
                    self.question_mark_number[i] = self.question_mark_number[i] + 1

                #
                elif self.is_exclamation_mark(part):
                    self.exclamation_mark_number[i] = self.exclamation_mark_number[i] + 1

                # quotation
                elif self.is_quotation_mark(part):
                    self.quotation_mark_number[i] = self.quotation_mark_number[i] + 1

                # bracket
                elif self.is_bracket_mark(part):
                    self.bracket_mark_number[i] = self.bracket_mark_number[i] + 1

                # at
                elif self.is_at_mark(part):
                    self.at_mark_number[i] = self.at_mark_number[i] + 1

                # numbersign
                elif self.is_numbersign_mark(part):
                    self.numbersign_mark_number[i] = self.numbersign_mark_number[i] + 1


    def is_all_chinese(self, part):
        for uchar in part:
            if (uchar >= u'\u4e00' and uchar <= u'\u9fa5') is False:
                return False
        return True
    def is_all_letter(self, part):
        for uchar in part:
            if ((uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a')) is False:
                return False
        return True
    def is_all_digit(self, part):
        for uchar in part:
            if (uchar >= u'\u0030' and uchar <= u'\u0039') is False:
                return False
        return True
    def is_question_mark(self, part):
        if part == u'\uff1f':
            return True
        else:
            return False
    def is_exclamation_mark(self, part):
        if part == u'\uff01':
            return True
        else:
            return False
    def is_quotation_mark(self, part):
        if part == u'\u201c':
            return True
        else:
            return False
    def is_bracket_mark(self, part):
        if part == u'\uff08':
            return True
        else:
            return False
    def is_at_mark(self, part):
        if part == u'\u0040':
            return True
        else:
            return False
    def is_numbersign_mark(self, part):
        if part == u'\u0023':
            return True
        else:
            return False
    def is_link(self, part):
        if part == u'http':
            return True
        else:
            return False


    def save(self):
        self.feature_data['chinese-word-number'] = self.chinese_word_number
        self.feature_data['english-word-number'] = self.english_word_number
        self.feature_data['digit-number'] = self.digit_number
        self.feature_data['question-mark-number'] = self.question_mark_number
        self.feature_data['exclamation-mark-number'] = self.exclamation_mark_number

        self.feature_data['quotation-mark-number'] = self.quotation_mark_number
        self.feature_data['bracket-mark-number'] = self.bracket_mark_number
        self.feature_data['at-mark-number'] = self.at_mark_number
        self.feature_data['numbersign-mark-number'] = self.numbersign_mark_number
        self.feature_data['link-number'] = self.link_number

        with open("./mid-data/feature_data.json", 'w') as f:
            json.dump(self.feature_data, f)

if __name__ == "__main__":
    feature_extractor = FeatureExtractor("./mid-data/data.json")
    feature_extractor.counter()
    feature_extractor.save()



