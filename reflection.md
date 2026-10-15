# LAB 04 - Reflection

## So sánh các representation

| Representation | Đặc tính | Điểm mạnh | Điểm yếu |
|---|---|---|---|
| TF-IDF | sparse, lexical | Giữ thông tin từng term, phù hợp với từ đặc trưng cho sentiment (bad, boring), dễ diễn giải qua trọng số | Không hiểu từ đồng nghĩa, không biết thứ tự từ |
| Average Word2Vec | dense, semantic | Nắm quan hệ ngữ nghĩa giữa các từ, số chiều cố định | Mất word order, một từ một vector, averaging làm loãng tín hiệu trên document dài. Trong lab: F1 0.6997 so với 0.8105 của TF-IDF |
| TF-IDF + bigram | sparse, có ngữ cảnh cục bộ | Bắt được cụm như "not good" | Vocabulary tăng từ 33734 lên 408277, F1 không cải thiện (0.8073) |

## Câu hỏi về bank

Từ "bank" có hai nghĩa: ngân hàng và bờ sông. Với TF-IDF, "bank" chỉ là một cột duy nhất trong ma trận nên không phân biệt được nghĩa. Với Word2Vec, "bank" chỉ có một vector chung cho mọi ngữ cảnh. Vì vậy cả hai đều không có khả năng contextual understanding.

## Từ representation đến neural NLP

TF-IDF khác semantic understanding vì chỉ đếm tần suất term. Word2Vec khác contextual understanding vì mỗi từ có đúng một vector bất kể ngữ cảnh.
Ví dụ "I like this movie" và "I do not like this movie": với average embedding, "not" chỉ được cộng vào trung bình như mọi từ khác nên hai câu có vector rất gần nhau (cosine 0.9490 trong Experiment 4).

Đây là động lực để chuyển sang Sequence Models (RNN, LSTM, GRU) ở LAB 05, nơi thứ tự và ngữ cảnh của từ được mô hình hóa trực tiếp, rồi tiếp đến attention và Transformer.
