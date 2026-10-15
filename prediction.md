# LAB 04 - Prediction trước experiment

## Prediction 1

Câu hỏi: TF-IDF + Logistic Regression có khả năng hoạt động tốt không?

Prediction: Có, F1 khoảng 0.75 đến 0.85.
Reason: Dataset cân bằng 50/50, review phim chứa nhiều từ mang sentiment rõ ràng (bad, great, boring) mà TF-IDF giữ lại thành feature riêng, và Logistic Regression thường hoạt động tốt với dữ liệu text sparse nhiều chiều.
Confidence: Cao.

Đối chiếu sau khi chạy: accuracy 0.8067, precision 0.7949, recall 0.8267, F1 0.8105. Đúng dự đoán.

## Prediction 2

Câu hỏi: Average Word2Vec có chắc chắn tốt hơn TF-IDF không?

Prediction: Không chắc chắn, có thể kém hơn.
Reason: Mỗi document dài trung bình hơn 600 token bị nén thành một vector 100 chiều nên tín hiệu của vài từ sentiment bị loãng. Word2Vec chỉ được train trên 1400 document nên chất lượng embedding hạn chế.
Confidence: Trung bình.

Đối chiếu sau khi chạy: Average Word2Vec + LR đạt accuracy 0.6967, F1 0.6997, thấp hơn rõ rệt so với TF-IDF + LR (F1 0.8105). Đúng dự đoán.

## Prediction 3

Câu hỏi: Nếu tăng vocabulary size thì accuracy chắc chắn tăng không?

Prediction: Không chắc chắn, có thể giữ nguyên hoặc giảm nhẹ.
Reason: Vocabulary lớn thêm nhiều feature hiếm và nhiễu, mô hình tuyến tính học trọng số không ổn định cho các feature xuất hiện rất ít lần trong tập train nhỏ.
Confidence: Trung bình.

Đối chiếu sau khi chạy (Experiment 5): từ unigram (33734 feature) sang unigram + bigram (408277 feature), F1 giảm nhẹ từ 0.8105 xuống 0.8073. Đúng dự đoán.

## Prediction 4

Câu hỏi: Nếu bỏ stopwords thì performance chắc chắn tăng không?

Prediction: Không chắc chắn.
Reason: Một số stopword như not, no, very mang thông tin phủ định hoặc nhấn mạnh quan trọng cho sentiment, bỏ đi có thể mất tín hiệu. Hiệu quả phụ thuộc dataset và mô hình.
Confidence: Trung bình.

Đối chiếu sau khi chạy: lab này không chạy riêng thí nghiệm bỏ stopword. Phần model interpretation cho thấy nhiều stopword vô nghĩa (and, is, as, his, the) có trọng số lớn, nên bỏ stopword có thể giảm nhiễu, nhưng cũng có rủi ro mất các từ phủ định. Kết luận: không thể khẳng định chắc chắn tăng.

## Prediction 5

Câu hỏi: Accuracy và F1 có thể cho kết luận khác nhau không?

Prediction: Có, đặc biệt khi dataset imbalance.
Reason: Như Bài 4, model đoán toàn bộ class đa số vẫn đạt accuracy 95% nhưng F1 của class thiểu số bằng 0.
Confidence: Cao.

Đối chiếu sau khi chạy: dataset movie_reviews cân bằng nên accuracy và F1 gần nhau (TF-IDF + LR: 0.8067 và 0.8105). Hai metric chỉ lệch đáng kể khi dataset imbalance.
