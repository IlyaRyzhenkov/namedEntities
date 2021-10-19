import TextParser
import NatashaParser
import StatMaker


DATA_FILENAME = "data/train_sentences.txt"
MARK_FILENAME = "data/train_nes.txt"

if __name__ == '__main__':

    text_parser = TextParser.TextParser()
    mark_data = text_parser.parse_files(DATA_FILENAME, MARK_FILENAME)

    natasha_parser = NatashaParser.NatashaParser()
    natasha_parser.load_text(DATA_FILENAME)
    natasha_data = natasha_parser.parse_text()

    sm = StatMaker.StatMaker()
    sm.compare_stat(natasha_data, mark_data)
