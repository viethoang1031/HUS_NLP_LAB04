# LAB 04 - Bài tập tính toán

## Bài 1 - Binary classification

Cho $x = [1, 2, 0]$, $w = [0.5, -0.2, 0.4]$, $b = 0.1$.

$$z = w^\top x + b = 0.5 \cdot 1 + (-0.2) \cdot 2 + 0.4 \cdot 0 + 0.1 = 0.5 - 0.4 + 0 + 0.1 = 0.2$$

$$\sigma(z) = \frac{1}{1 + e^{-z}} = \frac{1}{1 + e^{-0.2}} = \frac{1}{1 + 0.8187} = \frac{1}{1.8187} \approx 0.5498$$

$$P(y = 1 \mid x) = \sigma(z) \approx 0.5498$$

## Bài 2 - Prediction threshold

Cho $P(y = 1 \mid x) = 0.72$.

Với $\tau = 0.5$: $0.72 \geq 0.5 \Rightarrow \hat{y} = 1$ (positive).

Với $\tau = 0.8$: $0.72 < 0.8 \Rightarrow \hat{y} = 0$ (negative).

Tăng threshold ($\tau \uparrow$) thì model dự đoán positive ít hơn:
- FP giảm nên Precision $= \frac{TP}{TP + FP}$ thường tăng.
- Một số mẫu positive thật có xác suất vừa phải bị chuyển thành negative nên FN tăng, Recall $= \frac{TP}{TP + FN}$ giảm.

Giảm threshold ($\tau \downarrow$) thì ngược lại: Recall tăng, Precision giảm.

## Bài 3 - Confusion matrix

$TP = 80,\ FN = 20,\ FP = 10,\ TN = 90$

$$Precision = \frac{TP}{TP + FP} = \frac{80}{80 + 10} = \frac{80}{90} \approx 0.8889$$

$$Recall = \frac{TP}{TP + FN} = \frac{80}{80 + 20} = \frac{80}{100} = 0.8$$

$$F1 = \frac{2PR}{P + R} = \frac{2 \cdot 0.8889 \cdot 0.8}{0.8889 + 0.8} = \frac{1.4222}{1.6889} \approx 0.8421$$

Ý nghĩa trong bài toán phát hiện spam:
- False positive: email bình thường bị gán nhầm là spam. Email quan trọng có thể bị chuyển vào thư mục spam và người dùng không đọc được.
- False negative: email spam bị bỏ lọt, vẫn nằm trong hộp thư đến. Gây phiền toái nhưng thường ít nghiêm trọng hơn false positive.

Vì vậy trong spam detection thường ưu tiên precision cao cho class spam.

## Bài 4 - Accuracy trap

Dataset: 950 negative, 50 positive. Model dự đoán mọi sample là negative.

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN} = \frac{0 + 950}{1000} = 95\%$$

Với class positive: $TP = 0,\ FN = 50,\ FP = 0$.

$$Recall = \frac{0}{0 + 50} = 0$$

$$Precision = \frac{0}{0 + 0} \ \text{(không xác định)}$$

$$F1 = 0$$

Model này không thực sự tốt: accuracy cao chỉ vì dữ liệu mất cân bằng, chỉ cần đoán theo class đa số là đạt 95% mà không phát hiện được mẫu positive nào.

Cần xem thêm precision, recall, F1 của class thiểu số (positive), hoặc macro-F1 và balanced accuracy.
