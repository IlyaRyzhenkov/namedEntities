from collections import Counter


class TextParser:
    def __init__(self):
        self.org_entities = Counter()
        self.per_entities = Counter()
        self.data_lines = []
        self.mark_lines = []

    def parse_files(self, data_filename, mark_filename):
        self.load_text(data_filename, mark_filename)
        self.parse_lines()
        return self.org_entities, self.per_entities

    def load_text(self, data_filename, mark_filename):
        with open(data_filename, 'r') as data_f:
            with open(mark_filename, 'r') as res_f:
                self.data_lines = data_f.readlines()
                self.mark_lines = res_f.readlines()

    def parse_lines(self):
        parsed = 0
        for i in range(min(len(self.data_lines), len(self.mark_lines))):
            self.parse_line(self.data_lines[i], self.mark_lines[i])
            parsed += 1
        print(f"Parsed {parsed} lines")

    def parse_line(self, data_line, mark_line):
        tokens = mark_line.split()
        token_id = 0
        while token_id < len(tokens):
            if tokens[token_id] == "EOL":
                break

            token_start = int(tokens[token_id])
            token_length = int(tokens[token_id+1])
            token_type = tokens[token_id+2]
            token_id += 3
            token = data_line[token_start:token_start+token_length]
            if token_type == "PERSON":
                self.per_entities[token] += 1
            elif token_type == "ORG":
                self.org_entities[token] += 1
