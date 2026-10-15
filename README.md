# LAB 04 - Text Classification

Bài làm mẫu (đáp án tham chiếu) cho LAB 04.

## Nội dung

- calculations.md: Bài 1 đến Bài 4.
- prediction.md: 5 prediction trước experiment (Prediction, Reason, Confidence) và đối chiếu sau khi chạy.
- preprocessing.py: clean_text, tokenize, load_movie_reviews, stratified_split.
- classification.ipynb: Experiment 1 đến 5, data leakage, evaluation, error analysis, model interpretation. Output đã chạy sẵn.
- results.csv: kết quả số của các thí nghiệm (cột experiment, setting, item, metric, value).
- confusion_matrix.png: confusion matrix của TF-IDF + Logistic Regression trên test set.
- error_analysis.md: 3 mẫu đúng và 3 mẫu sai.
- reflection.md: so sánh representation, câu hỏi về bank, định hướng sang neural NLP.

## Cài đặt và chạy

```powershell
pip install numpy pandas scikit-learn gensim nltk matplotlib jupyter jupytext
cd LAB04
python -m jupyter nbconvert --to notebook --execute --inplace classification.ipynb
```

Dataset NLTK movie_reviews sẽ tự tải về lần chạy đầu tiên.

## Quy ước

- Dataset: NLTK movie_reviews (2000 review phim, 1000 pos / 1000 neg, cùng nguồn với IMDb), bài toán sentiment (Option A).
- Chia stratified 70/15/15 (1400 / 300 / 300), seed 42. TF-IDF và Word2Vec chỉ fit trên train để tránh data leakage.
- Tiền xử lý: lowercase, giữ chữ cái và apostrophe, bỏ số và ký tự đặc biệt, không bỏ stopword.
- Word2Vec (gensim): CBOW, vector_size 100, window 5, min_count 2, epochs 10, seed 42, huấn luyện trên tập train. Document vector là trung bình vector các từ.
- Classifier: LogisticRegression (max_iter 1000), LinearSVC mặc định.

## Kết quả chính (test set)

| Representation | Classifier | Accuracy | Precision | Recall | F1 |
|---|---|---|---|---|---|
| TF-IDF | Logistic Regression | 0.8067 | 0.7949 | 0.8267 | 0.8105 |
| Avg Word2Vec | Logistic Regression | 0.6967 | 0.6928 | 0.7067 | 0.6997 |
| TF-IDF | Linear SVM | 0.8300 | 0.8113 | 0.8600 | 0.8350 |

| Features | Vocabulary | F1 |
|---|---|---|
| Unigram | 33734 | 0.8105 |
| Unigram + Bigram | 408277 | 0.8073 |

Ghi chú cho người chấm: số liệu có thể lệch nhẹ nếu đổi phiên bản thư viện hoặc seed. Cần kiểm tra các kết luận định tính: TF-IDF tốt hơn Average Word2Vec trên dataset này, bigram làm vocabulary tăng mạnh nhưng không chắc cải thiện F1, average embedding không phân biệt rõ "good" và "not good", không báo cáo chỉ accuracy, không có data leakage.
