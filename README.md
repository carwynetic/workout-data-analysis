# 🏃‍♂️ Workout Data Analysis - Linear Regression Project

Đây là dự án phân tích thống kê và hồi quy tuyến tính (Computer Project) cho môn học **MAS291** tại Đại học FPT.
Dự án tập trung nghiên cứu mối quan hệ giữa **thời gian tập Cardio** (*Session_Duration*) và **lượng calo đốt được** (*Calories_Burned*) ở nam giới trong độ tuổi 18–25.

---

## 🎯 Mục tiêu dự án

* Tiền xử lý dữ liệu và lọc tệp dữ liệu *Life Style Data*
* Thực hiện thống kê mô tả và trực quan hóa dữ liệu (*Histogram, Boxplot, Scatter Plot*)
* Tính toán khoảng tin cậy 95% cho trung bình
* Thực hiện kiểm định giả thuyết hai mẫu độc lập (*T-test*)
* Xây dựng mô hình hồi quy tuyến tính đơn (*Simple Linear Regression*) và đánh giá hệ số

---

## 📂 Cấu trúc thư mục (Folder Structure)

```text
workout-data-analysis/
├── data/
│   ├── raw/                      # Dữ liệu thô (Final_data.csv)
│   └── processed/                # Dữ liệu sau khi lọc (Filtered_Cardio_Data.csv)
├── images/                       # Biểu đồ xuất từ code
│   ├── boxplot_calories.png
│   ├── histogram_calories.png
│   ├── scatter_plot.png
│   └── regression_line_plot.png
├── notebooks/                    # Notebook phân tích
│   └── 01_exploratory_data_analysis.ipynb
├── src/                          # Source code chính
│   ├── confidence_interval.py
│   ├── data_pipeline.py
│   ├── descriptive_stats.py
│   ├── hypothesis_testing.py
│   ├── simple_linear_regression.py
│   └── visualize_data.py
├── README.md
└── requirements.txt
```

---

## &#x20;

````
# 🏃‍♂️ Workout Data Analysis - Linear Regression Project

Đây là dự án phân tích thống kê và hồi quy tuyến tính (Computer Project) cho môn học **MAS291** tại Đại học FPT. 
Dự án tập trung nghiên cứu mối quan hệ giữa **thời gian tập Cardio** (Session_Duration) và **lượng calo đốt được** (Calories_Burned) ở nam giới trong độ tuổi 18-25.

## 🎯 Mục tiêu dự án
* Tiền xử lý dữ liệu và lọc tệp dữ liệu Life Style Data.
* Thực hiện Thống kê mô tả và Trực quan hóa dữ liệu (Histogram, Boxplot, Scatter Plot).
* Tính toán ước lượng khoảng tin cậy 95% cho trung bình.
* Thực hiện kiểm định giả thuyết 2 mẫu độc lập (T-test).
* Xây dựng mô hình Hồi quy tuyến tính đơn (Simple Linear Regression) và đánh giá các hệ số.

## 📂 Cấu trúc thư mục (Folder Structure)

Dự án được tổ chức theo cấu trúc chuẩn dành cho Khoa học dữ liệu (Data Science):

```text
workout-data-analysis/
├── data/
│   ├── raw/                      # Chứa dữ liệu thô (Final_data.csv)
│   └── processed/                # Chứa dữ liệu sau khi lọc (Filtered_Cardio_Data.csv)
├── images/                       # Chứa các biểu đồ xuất ra từ code
│   ├── boxplot_calories.png
│   ├── histogram_calories.png
│   ├── scatter_plot.png
│   └── regression_line_plot.png
├── notebooks/                    # Môi trường chạy và báo cáo tương tác
│   └── 01_exploratory_data_analysis.ipynb
├── src/                          # Chứa mã nguồn Python chính
│   ├── confidence_interval.py    # Code tính khoảng tin cậy
│   ├── data_pipeline.py          # Code tiền xử lý và lọc data
│   ├── descriptive_stats.py      # Code tính các đại lượng thống kê
│   ├── hypothesis_testing.py     # Code kiểm định giả thuyết T-test
│   ├── simple_linear_regression.py # Code hồi quy tuyến tính
│   └── visualize_data.py         # Code xuất biểu đồ tự động
├── README.md                     # Tài liệu hướng dẫn (File này)
└── requirements.txt              # Danh sách các thư viện cần cài đặt

````

## ⚙️ Hướng dẫn cài đặt và chạy (Installation & Usage)

### Bước 1: Thiết lập môi trường

Đảm bảo bạn đã cài đặt Python (phiên bản 3.8 trở lên). Cài đặt các thư viện cần thiết bằng lệnh:

Bash

```
pip install -r requirements.txt

```

### Bước 2: Chạy mã nguồn Python

Mở Terminal tại thư mục gốc của dự án, bạn có thể chạy tuần tự các tệp trong thư mục `src/` để tự động hóa quá trình phân tích:

1. Lọc dữ liệu thô:

Bash

```
python src/data_pipeline.py

```

2. Tính thống kê mô tả:

Bash

```
python src/descriptive_stats.py

```

3. Xuất biểu đồ ra thư mục `images/`:

Bash

```
python src/visualize_data.py

```

4. Tính khoảng tin cậy:

Bash

```
python src/confidence_interval.py

```

5. Chạy kiểm định giả thuyết (T-test):

Bash

```
python src/hypothesis_testing.py

```

6. Chạy mô hình hồi quy tuyến tính:

Bash

```
python src/simple_linear_regression.py

```

### Bước 3: Xem Báo cáo tương tác

Mở Jupyter Notebook để xem toàn bộ quá trình phân tích và báo cáo:

Bash

```
jupyter notebook notebooks/01_exploratory_data_analysis.ipynb

```

## 📊 Kết luận chính (Key Findings)

* Có sự khác biệt rất lớn về lượng calo đốt được giữa nhóm tập thời gian ngắn (<= 1.28 giờ) và nhóm tập thời gian dài.
* Mô hình Hồi quy tuyến tính cho thấy mối tương quan **cực kỳ mạnh mẽ ($r = 0.990$)** giữa Thời gian tập và Calo tiêu hao.
* Biến "Thời gian tập" có khả năng giải thích xuất sắc tới **98.0% ($R^2 = 0.980$)** sự biến thiên của lượng calo, là cơ sở vững chắc để lập kế hoạch tập luyện thực tế.

---

*Dự án được thực hiện bởi Nguyễn Đoàn Bảo Phúc và Trần Thiên Anh Khoa.*

  

### Bước 1: Cài đặt môi trường

Yêu cầu Python >= 3.8

```bash
pip install -r requirements.txt
```

---

### Bước 2: Chạy các module phân tích

```bash
# Lọc dữ liệu
python src/data_pipeline.py

# Thống kê mô tả
python src/descriptive_stats.py

# Vẽ biểu đồ
python src/visualize_data.py

# Khoảng tin cậy
python src/confidence_interval.py

# Kiểm định giả thuyết
python src/hypothesis_testing.py

# Hồi quy tuyến tính
python src/simple_linear_regression.py
```

---

### Bước 3: Xem báo cáo tương tác

```bash
jupyter notebook notebooks/01_exploratory_data_analysis.ipynb
```

---

## 📊 Kết luận chính (Key Findings)

* Có sự khác biệt lớn về lượng calo đốt được giữa nhóm tập thời gian ngắn (≤ 1.28 giờ) và nhóm tập thời gian dài
* Mô hình hồi quy tuyến tính cho thấy tương quan rất mạnh: **r = 0.990**
* Biến *Session_Duration* giải thích khoảng **98.0% (R² = 0.980)** biến thiên của *Calories_Burned*

---

## 📚 Dataset

* Lifestyle dataset (Kaggle):
  https://www.kaggle.com/datasets/jockeroika/life-style-data/data

---

## 👨‍💻 Tác giả

* Nguyễn Đoàn Bảo Phúc
