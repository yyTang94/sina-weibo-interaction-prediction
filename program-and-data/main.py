from segmentation import Segment
from feature import FeatureExtractor
from topic import TopicExtractor

if __name__ == "__main__":
    segment = Segment("./mid-data/part-raw-data.txt")
    segment.preprocess()
    segment.segment()

    feature_extractor = FeatureExtractor("./mid-data/data.json")
    feature_extractor.counter()
    feature_extractor.save()

    topic_extractor = TopicExtractor("./mid-data/feature_data.json", "./mid-data/feature_data.txt")
    topic_extractor.extract()
    topic_extractor.save()