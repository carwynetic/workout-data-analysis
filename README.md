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

## ⚙️ Hướng dẫn cài đặt và chạy (Installation & Usage)

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
* Trần Thiện Anh Khoa
