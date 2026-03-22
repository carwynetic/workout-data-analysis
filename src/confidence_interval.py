import pandas as pd
import numpy as np
import scipy.stats as st

def calculate_confidence_intervals(file_path, column_name='Calories_Burned', alpha=0.05):
    # 1. Đọc dữ liệu
    df = pd.read_csv(file_path)
    data = df[column_name].dropna() # Bỏ qua giá trị rỗng nếu có
    
    # 2. Tính toán các tham số thống kê mẫu
    n = len(data)
    x_bar = data.mean()
    s = data.std() # pandas mặc định tính std mẫu (ddof=1)
    df_degrees = n - 1
    
    print(f"--- THÔNG TIN MẪU ({column_name}) ---")
    print(f"Số lượng (n): {n}")
    print(f"Trung bình (x_bar): {x_bar:.3f}")
    print(f"Độ lệch chuẩn (s): {s:.3f}\n")

    # 3. Tính Khoảng tin cậy hai phía (Two-sided CI)
    t_two_sided = st.t.ppf(1 - alpha/2, df_degrees)
    margin_error_2 = t_two_sided * (s / np.sqrt(n))
    ci_lower_2 = x_bar - margin_error_2
    ci_upper_2 = x_bar + margin_error_2
    
    print(f"--- KHOẢNG TIN CẬY {(1-alpha)*100}% HAI PHÍA ---")
    print(f"Giá trị tới hạn t: {t_two_sided:.3f}")
    print(f"Khoảng tin cậy: ({ci_lower_2:.3f}, {ci_upper_2:.3f})\n")

    # 4. Tính Khoảng tin cậy một phía - Cận dưới (One-sided Lower Bound)
    t_one_sided = st.t.ppf(1 - alpha, df_degrees)
    margin_error_1 = t_one_sided * (s / np.sqrt(n))
    ci_lower_1 = x_bar - margin_error_1
    
    print(f"--- KHOẢNG TIN CẬY {(1-alpha)*100}% MỘT PHÍA (CẬN DƯỚI) ---")
    print(f"Giá trị tới hạn t: {t_one_sided:.3f}")
    print(f"Cận dưới: {ci_lower_1:.3f}")

if __name__ == "__main__":
    # Đường dẫn file data (chạy từ thư mục gốc của project)
    DATA_FILE = 'data/processed/Filtered_Cardio_Data.csv'
    
    # Gọi hàm tính toán cho biến Calories_Burned
    calculate_confidence_intervals(DATA_FILE, column_name='Calories_Burned')