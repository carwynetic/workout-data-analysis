import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_charts(input_path, output_dir):
    # Tạo thư mục lưu ảnh nếu chưa tồn tại
    os.makedirs(output_dir, exist_ok=True)
    
    # Thiết lập giao diện
    sns.set_theme(style="whitegrid")
    df = pd.read_csv(input_path)

    # 1. Vẽ Histogram
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Calories_Burned'], bins=20, kde=True, color='skyblue')
    plt.title('Phân bố Lượng Calo đốt được (Histogram)', fontsize=14)
    plt.xlabel('Calories Burned')
    plt.ylabel('Tần số (Frequency)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'histogram_calories.png'), dpi=300)
    plt.close() # Đóng plot để giải phóng bộ nhớ

    # 2. Vẽ Box Plot
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df['Calories_Burned'], color='lightgreen')
    plt.title('Biểu đồ hộp Lượng Calo đốt được (Box Plot)', fontsize=14)
    plt.xlabel('Calories Burned')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'boxplot_calories.png'), dpi=300)
    plt.close()

    # 3. Vẽ Scatter Plot (Không có đường hồi quy)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Session_Duration (hours)', y='Calories_Burned', data=df, alpha=0.6, color='blue')
    plt.title('Mối liên hệ giữa Thời gian tập và Lượng Calo (Scatter Plot)', fontsize=14)
    plt.xlabel('Session Duration (hours)')
    plt.ylabel('Calories Burned')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'scatter_plot.png'), dpi=300)
    plt.close()

    print(f"Đã xuất thành công 3 biểu đồ vào thư mục: {output_dir}")

if __name__ == "__main__":
    # Đường dẫn file data (chạy từ thư mục gốc của project)
    DATA_FILE = 'data/processed/Filtered_Cardio_Data.csv'
    
    # Nơi lưu ảnh (có thể trỏ thẳng vào thư mục chứa file LaTeX của bạn)
    SAVE_FOLDER = 'images/' 
    
    generate_charts(DATA_FILE, SAVE_FOLDER)