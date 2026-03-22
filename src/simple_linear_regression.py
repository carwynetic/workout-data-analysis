import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_linear_regression(file_path, output_image_dir='images/'):
    # 1. Đọc dữ liệu
    df = pd.read_csv(file_path)
    x = df['Session_Duration (hours)']
    y = df['Calories_Burned']
    
    # 2. Tính toán các thành phần công thức
    n = len(df)
    sum_x, sum_y = x.sum(), y.sum()
    sum_x2, sum_y2, sum_xy = (x**2).sum(), (y**2).sum(), (x*y).sum()
    
    Sxx = sum_x2 - (sum_x**2) / n
    Syy = sum_y2 - (sum_y**2) / n
    Sxy = sum_xy - (sum_x * sum_y) / n
    
    # 3. Tính hệ số hồi quy
    beta1 = Sxy / Sxx
    beta0 = y.mean() - beta1 * x.mean()
    
    # 4. Tính hệ số tương quan (r) và hệ số xác định (R^2)
    r = Sxy / np.sqrt(Sxx * Syy)
    r_squared = r**2
    
    print("--- KẾT QUẢ HỒI QUY TUYẾN TÍNH ---")
    print(f"Hệ số chặn (beta_0): {beta0:.3f}")
    print(f"Hệ số góc (beta_1): {beta1:.3f}")
    print(f"Hệ số tương quan (r): {r:.3f}")
    print(f"Hệ số xác định (R^2): {r_squared:.3f}")
    print(f"\nPhương trình: Calories = {beta0:.3f} + {beta1:.3f} * Duration")

    # 5. Vẽ đồ thị Scatter Plot kèm đường hồi quy
    os.makedirs(output_image_dir, exist_ok=True)
    plt.figure(figsize=(8, 6))
    
    # Vẽ bằng seaborn (có dải tin cậy 95% mờ mờ xung quanh đường thẳng)
    sns.regplot(x=x, y=y, 
                scatter_kws={'alpha':0.5, 'color':'blue'}, 
                line_kws={'color':'red', 'linewidth':2})
    
    plt.title('Hồi quy tuyến tính: Thời gian tập và Calo đốt được', fontsize=14)
    plt.xlabel('Session Duration (hours)')
    plt.ylabel('Calories Burned')
    plt.tight_layout()
    
    img_path = os.path.join(output_image_dir, 'regression_line_plot.png')
    plt.savefig(img_path, dpi=300)
    plt.close()
    print(f"\nĐã lưu biểu đồ tại: {img_path}")

if __name__ == "__main__":
    DATA_FILE = 'data/processed/Filtered_Cardio_Data.csv'
    run_linear_regression(DATA_FILE)