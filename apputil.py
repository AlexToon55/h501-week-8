''' Markov text generator module '''
from collections import defaultdict
import numpy as np


class MarkovText(object):
    ''' Markov text generator class '''
    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    ''' Build term dictionary from corpus '''
    def get_term_dict(self):

        corpus = self.corpus if isinstance(self.corpus, str) else ""
        # white space tokenization
        tokens = corpus.split()

        # Build token and list next tokens
        d = defaultdict(list)
        for i in range(len(tokens) - 1):
            d[tokens[i]].append(tokens[i + 1])

        if tokens:
            _ = d[tokens[-1]]  # ensure last token is in dictionary

        self.term_dict = dict(d)

        return self.term_dict

    ''' Generate text from corpus '''
    def generate(self, seed_term=None, term_count=15):
        
        # build the term dictionary if not already built
        if self.term_dict is None:
            self.get_term_dict()

    
        # term_count must be validated - raise ValueError if not positive
        if term_count <= 0:
            raise ValueError("term_count must be a positive integer")
        
        # validating the dictionary and parameters
        if not self.term_dict:
            raise ValueError("Term dictionary is not built.")

        # seed_term must be validated - raise ValueError if not in dictionary
        if seed_term is not None:
            if not isinstance(seed_term, str):
                raise ValueError("seed_term must be a string or nothing")
            if seed_term not in self.term_dict:
                raise ValueError("seed_term not found in term dictionary")
            
         # if seed_term is None, randomly select one from the term_dict keys
        if seed_term is None:
            seed_term = np.random.choice(list(self.term_dict.keys()))

        out = [seed_term]
        cur = seed_term

        for _ in range(term_count - 1):
            followers = self.term_dict.get(cur, [])
            if not followers:
                
                cur = np.random.choice(list(self.term_dict.keys()))
                out.append(cur)
                continue
            nxt = np.random.choice(followers)
            out.append(nxt)
            cur = nxt

        return " ".join(out)