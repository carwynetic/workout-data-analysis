import pandas as pd

def calculate_descriptive_stats(file_path):
    # 1. Đọc dữ liệu đã lọc
    df = pd.read_csv(file_path)
    
    # 2. Chọn biến cần thống kê
    target_cols = ['Session_Duration (hours)', 'Calories_Burned']
    
    # 3. Dùng .agg() để tính các chỉ số: Số lượng, Trung bình, Phương sai, Độ lệch chuẩn, Tứ phân vị, Max
    stats = df[target_cols].agg([
        'count', 
        'mean', 
        'var', 
        'std', 
        lambda x: x.quantile(0.25), 
        'median', 
        lambda x: x.quantile(0.75), 
        'max'
    ]).T  # Dùng .T (Transpose) để đảo dòng/cột hiển thị cho đẹp
    
    # 4. Đổi tên cột cho khớp với LaTeX
    stats.columns = ['Count', 'Mean', 'Variance', 'Std. Dev.', 'Q1', 'Median', 'Q3', 'Max']
    
    # 5. Làm tròn 3 chữ số thập phân
    stats = stats.round(3)
    
    print("BẢNG THỐNG KÊ MÔ TẢ:")
    print(stats)
    return stats

if __name__ == "__main__":
    # Đường dẫn trỏ tới file csv bạn đã tạo ở bước xử lý data
    calculate_descriptive_stats('data/processed/Filtered_Cardio_Data.csv')