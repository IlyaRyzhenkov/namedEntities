from natasha import Doc, NewsNERTagger, NewsEmbedding, Segmenter
from collections import Counter


class NatashaParser:
    def __init__(self):
        self.org_entities = Counter()
        self.per_entities = Counter()
        self.text = ""
        self.emb = NewsEmbedding()
        self.segmenter = Segmenter()
        self.ner_tagger = NewsNERTagger(self.emb)

    def load_text(self, data_filename):
        with open(data_filename, 'r') as f:
            self.text = f.read()

    def parse_text(self):
        doc = Doc(self.text)
        doc.segment(self.segmenter)
        doc.tag_ner(self.ner_tagger)
        for doc_span in doc.ner.spans:
            if doc_span.type == "PER":
                token = self.text[doc_span.start:doc_span.stop]
                self.per_entities.update(token.split())
            elif doc_span.type == "ORG":
                token = self.text[doc_span.start:doc_span.stop]
                self.org_entities.update(token.split())
        return self.org_entities, self.per_entities
