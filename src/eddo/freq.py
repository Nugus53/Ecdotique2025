import spacy
import re
from collections import Counter
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def get_frequence(texts, feature="text", model: str = None, regex: str = None, ignore_punctuation: bool = True, use_tfidf=False):
    """
    Calcule la fréquence des mots en fonction de l'option choisie. Option pour normaliser avec TF-IDF.

    feature peut être :
    - "text" : mots tels qu'ils apparaissent dans le texte
    - "lemma" : lemmes des mots
    - "pos" : catégories grammaticales (part-of-speech)
    - "msd" : détails morphosyntaxiques

    Params :
    - texts : dict {clé: texte} contenant les textes à analyser
    - model : modèle spaCy à utiliser (None si regex ou tokenisation par espace)
    - regex : regex pour la tokenisation (prioritaire si présente)
    - ignore_punctuation : bool, True pour ignorer la ponctuation
    - use_tfidf : bool, True pour normaliser les fréquences avec TF-IDF
    """
    nlp = spacy.load(model) if model else None
    all_features = set()
    tokenized_texts = {}

    for key, value in texts.items():
        if regex:
            tokens = re.findall(regex, value)
            if ignore_punctuation:
                tokens = [token for token in tokens if token.isalnum()]
        elif model:
            doc = nlp(value)
            if feature == "text":
                tokens = [token.text.lower() for token in doc if not (ignore_punctuation and token.is_punct)]
            elif feature == "lemma":
                tokens = [token.lemma_.lower() for token in doc if not (ignore_punctuation and token.is_punct)]
            elif feature == "pos":
                tokens = [token.pos_ for token in doc]
            elif feature == "msd":
                tokens = [token.morph for token in doc]
            else:
                raise ValueError("Feature non valide. Choisissez entre 'text', 'lemma', 'pos' ou 'msd'.")
        else:
            tokens = value.split()
            if ignore_punctuation:
                tokens = [token for token in tokens if token.isalnum()]

        tokenized_texts[key] = tokens
        all_features.update(tokens)

    all_features = list(all_features)
    freq_df = pd.DataFrame(index=texts.keys(), columns=all_features).fillna(0)

    for key, tokens in tokenized_texts.items():
        word_freq = Counter(tokens)
        for token, freq in word_freq.items():
            freq_df.loc[key, token] = freq

    if use_tfidf:
        tfidf_vectorizer = TfidfVectorizer(vocabulary=all_features)
        tfidf_matrix = tfidf_vectorizer.fit_transform(texts.values())
        tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), index=texts.keys(), columns=all_features)
        freq_df = tfidf_df

    return freq_df.transpose()


