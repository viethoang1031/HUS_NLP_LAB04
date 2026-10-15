"""Tiền xử lý và chia dữ liệu cho LAB 04 - Text Classification.

Dataset: NLTK movie_reviews (2000 review phim, nhãn pos/neg), dùng cho sentiment classification.
"""

import re
import random

import numpy as np

LABEL2ID = {"neg": 0, "pos": 1}
ID2LABEL = {0: "neg", 1: "pos"}

_TOKEN_RE = re.compile(r"[a-z']+")


def clean_text(text):
    """Lowercase, giữ chữ cái và apostrophe, bỏ số và ký tự đặc biệt."""
    return " ".join(_TOKEN_RE.findall(text.lower()))


def tokenize(text):
    return _TOKEN_RE.findall(text.lower())


def load_movie_reviews():
    """Trả về (texts, labels) từ NLTK movie_reviews corpus."""
    import nltk

    try:
        from nltk.corpus import movie_reviews
        movie_reviews.fileids()
    except LookupError:
        nltk.download("movie_reviews")
        from nltk.corpus import movie_reviews

    texts, labels = [], []
    for fileid in movie_reviews.fileids():
        category = movie_reviews.categories(fileid)[0]
        texts.append(movie_reviews.raw(fileid))
        labels.append(LABEL2ID[category])
    return texts, labels


def stratified_split(texts, labels, val_size=0.15, test_size=0.15, seed=42):
    """Chia train/validation/test theo tỷ lệ cho trước, giữ nguyên tỷ lệ class.

    Chỉ chia dữ liệu, chưa fit vectorizer nào, để TF-IDF/Word2Vec chỉ fit trên train (tránh data leakage).
    """
    rng = random.Random(seed)
    texts = np.array(texts, dtype=object)
    labels = np.array(labels)

    train_idx, val_idx, test_idx = [], [], []
    for label in np.unique(labels):
        idx = np.where(labels == label)[0].tolist()
        rng.shuffle(idx)
        n = len(idx)
        n_val = int(round(n * val_size))
        n_test = int(round(n * test_size))
        val_idx.extend(idx[:n_val])
        test_idx.extend(idx[n_val:n_val + n_test])
        train_idx.extend(idx[n_val + n_test:])

    rng.shuffle(train_idx)
    rng.shuffle(val_idx)
    rng.shuffle(test_idx)

    def _subset(idx):
        return [texts[i] for i in idx], [int(labels[i]) for i in idx]

    return _subset(train_idx), _subset(val_idx), _subset(test_idx)
