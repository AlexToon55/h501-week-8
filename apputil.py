from collections import defaultdict


class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):

        # white space tokenization
        tokens = self.corpus.split()

        # Build token and list next tokens
        d = defaultdict(list)
        for i in range(len(tokens) - 1):
            cut_term = tokens[i]
            next_term = tokens[i + 1]
            d[cut_term].append(next_term)

        if tokens:
            _ = d[tokens[-1]]  # ensure last token is in dictionary

        self.term_dict = dict(d)

        return self.term_dict


    def generate(self, seed_term=None, term_count=15):

        # your code here ...

        return None