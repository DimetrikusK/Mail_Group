"""
module
"""
import argparse


class InvertedIndex:
    """
    class
    """
    service_bits = "6shhh"
    format_strings = []

    def __init__(self, invert_index=None):
        self.invert_index = invert_index or {}

    def query(self, words: list):
        """Return the list of relevant documents for the given query"""
        if not words:
            return None
        ids_set = set(self.invert_index.get(words[0], []))
        if len(words) == 1:
            return list(ids_set)
        for word in words[1:]:
            ids_set &= set(self.invert_index.get(word, []))
        return list(ids_set)

    def dump(self, filepath: str):
        with open(filepath, "wb", 1) as file:
            for word, id in self.invert_index.items():
                format_string = "{}s".format(len(word.encode("utf-8"))) + "H" * len(id)
                InvertedIndex.format_strings.append(format_string)
                line_to_write = [word.encode("utf-8")] + [i for i in id]
                len_line = len(word.encode("utf-8")) + \
                           sum([len(str(i)) for i in id]) + \
                           len([i for i in id])
                file.write(struct.pack(InvertedIndex.service_bits + format_string,
                                "\t\0\t\t\0\t".encode("utf-8"),
                                len(word.encode("utf-8")),
                                len(id),
                                len_line, *line_to_write))

    @classmethod
    def load(cls, filepath: str):
        article_dict = {}
        with open(filepath, "rb") as file:
            lines = file.read()
        for i in lines.split(b'\t\x00\t\t\x00\t'):
            if i == b'':
                continue
            struct_info = struct.unpack("hhh", i[:6])
            len_word, num_ids = struct_info[0], struct_info[1]
            tup = struct.unpack("{}s".format(len_word) + "H" * num_ids, i[6:])
            key = tup[0].decode("utf-8")
            article_dict[key] = article_dict.get(key, []) + list(tup[1:])
        return InvertedIndex(article_dict)


def load_documents(filepath: str):
    documents = []
    with open(filepath, "r") as file:
        for line in file.readlines():
            documents.append(line)
    return documents


def build_inverted_index(documents):
    article_dict = {}
    with open("stop_words_en.txt", "r") as file:
        stop_words = file.read().split("\n")
    for doc in documents:
        tokens = nltk.word_tokenize(doc)
        tokens = {word.lower() for word in tokens
                  if not word.isdigit()
                  and word not in stop_words
                  and word.isalnum()}
        id = int(doc.split("\t", 1)[0])
        for token in tokens:
            article_dict[token] = article_dict.get(token, []) + [id]
    return InvertedIndex(article_dict)


def main():
    # documents = load_documents("wikipedia_sample")
    # inverted_index = build_inverted_index(documents)
    # inverted_index.dump("inverted.index")
    inverted_index = InvertedIndex.load("inverted.index")

    document_ids = inverted_index.query(["two", "words", "german", "war"])
    document_ids = inverted_index.query((["long", "query", "sex"]))
    # print(inverted_index.invert_index)
    print(document_ids)


# parser = argparse.ArgumentParser(description='inverted index parser')
# parser.add_argument('query', action="store", dest="quer")

if __name__ == "__main__":
    # import nltk
    # import struct

    import argparse
    parser = argparse.ArgumentParser(description='inverted index parser')
    parser = argparse.ArgumentParser(description='inverted index parser')
    parser.add_argument('query', action="store_true")
    parser.add_argument('build', action="store_true")
    parser.add_argument('--dataset', action='store', type=str, dest="dataset_path")
    parser.add_argument('--output', action='store', type=str, dest="output_path")
    args = parser.parse_args()
    # print(args.query)
    if args.build:
        pass
    # if args.query:
    #     main()