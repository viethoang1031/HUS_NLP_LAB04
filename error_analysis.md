# LAB 04 - Error analysis

Model: TF-IDF (unigram) + Logistic Regression, đánh giá trên test set (300 review, 150 pos / 150 neg). Confusion matrix: TP = 124, FN = 26, FP = 32, TN = 118.

## Ví dụ phân loại đúng

| Text (rút gọn) | True | Predicted | Analysis |
|---|---|---|---|
| nosferatu the vampyre ( germany 1979 ) a film review by mike watson ... this extraordinary re-telling of bram stoker's " dracula " by german filmmaker werner herzog deserves ... | pos | pos | Ngôn ngữ khen nhất quán ("extraordinary", "deserves"), không có phủ định hay tương phản nên dễ phân loại |
| a friend invites you to a movie . this film would evade the explosions and special effects of standard summer fare , and be grounded in reality ... | neg | neg | Phần sau của review chứa nhiều từ chê rõ ràng, đủ tín hiệu từ vựng cho class negative |
| an astonishingly difficult movie to watch , the last temptation of christ may be scorsese's most important film ... | pos | pos | Các từ "astonishingly", "most important" tạo tín hiệu tích cực mạnh |

## Ví dụ phân loại sai

| Text (rút gọn) | True | Predicted | Analysis |
|---|---|---|---|
| when a someone journeys to the theater to see a comedy , he always risks having to sit through inanity such as ... it really is too bad that comedies are so hit- and-miss ... | pos | neg | Contrastive structure (gần với negation): đoạn mở đầu chê thể loại phim nói chung rồi mới khen phim đang review. Bag-of-words không phân biệt được bối cảnh với đánh giá trực tiếp |
| " marie couldn't talk , " paulie , the parrot star of his own movie , tells us about the daughter in his original family . " dad couldn't listen ... | neg | pos | Văn phong kể chuyện, đoạn đầu không có từ chê rõ ràng nên model chỉ thấy từ vựng bề mặt. Có thể xem là lexical ambiguity (nhiều từ trung tính hoặc mang sắc thái tích cực nhẹ) |
| wong kar-wei's " fallen angels " is , on a purely visceral level , one of the most exciting films i've seen in a long while . unfortunately , wong seems more interested in experimenting with his camera ... | pos | neg | Mixed sentiment: câu đầu khen, sau "unfortunately" là chê. Review hỗn hợp, các từ tiêu cực kéo dự đoán về negative |

Nhận xét chung: cả ba lỗi đều không do rare word, domain-specific term hay data noise, mà chủ yếu do cấu trúc tương phản hoặc sentiment hỗn hợp. TF-IDF + Logistic Regression cộng dồn đóng góp của từng từ độc lập nên không nắm được thứ tự câu và vai trò của các từ chuyển hướng như but, however, unfortunately. Đây là giới hạn của bag-of-words đã thấy ở Experiment 4.

Về metric: số FP (32) hơi nhiều hơn FN (26), precision (0.7949) thấp hơn recall (0.8267), nghĩa là model hơi thiên về dự đoán pos. Chênh lệch nhỏ nên không có class nào bị bỏ sót rõ rệt.
