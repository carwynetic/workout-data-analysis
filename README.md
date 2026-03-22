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

