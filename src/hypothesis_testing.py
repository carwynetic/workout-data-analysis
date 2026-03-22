import pandas as pd
import numpy as np
import scipy.stats as st

def two_sample_t_test(file_path):
    df = pd.read_csv(file_path)
    
    # Lấy trung vị của thời gian tập để chia 2 nhóm
    median_duration = df['Session_Duration (hours)'].median()
    
    # Chia 2 nhóm dữ liệu Calo đốt được
    group1 = df[df['Session_Duration (hours)'] <= median_duration]['Calories_Burned']
    group2 = df[df['Session_Duration (hours)'] > median_duration]['Calories_Burned']
    
    n1, n2 = len(group1), len(group2)
    mean1, std1 = group1.mean(), group1.std(ddof=1)
    mean2, std2 = group2.mean(), group2.std(ddof=1)
    
    print("--- THÔNG TIN 2 MẪU ---")
    print(f"Nhóm 1 (Tập <= {median_duration}h): n1={n1}, mean1={mean1:.3f}, std1={std1:.3f}")
    print(f"Nhóm 2 (Tập > {median_duration}h): n2={n2}, mean2={mean2:.3f}, std2={std2:.3f}\n")
    
    # Tính Pooled Standard Deviation
    df_deg = n1 + n2 - 2
    sp_sq = ((n1 - 1) * std1**2 + (n2 - 1) * std2**2) / df_deg
    sp = np.sqrt(sp_sq)
    
    # Tính T-statistic
    t_stat = (mean1 - mean2) / (sp * np.sqrt(1/n1 + 1/n2))
    
    # Tính P-value (2-sided & 1-sided lower)
    p_two_sided = 2 * (1 - st.t.cdf(abs(t_stat), df_deg))
    p_one_sided = st.t.cdf(t_stat, df_deg) # P(T <= t_stat) vì t_stat âm
    
    print("--- KẾT QUẢ KIỂM ĐỊNH (T-TEST) ---")
    print(f"Phương sai gộp (Sp): {sp:.3f}")
    print(f"Giá trị kiểm định T0: {t_stat:.3f}, Bậc tự do df: {df_deg}")
    print(f"P-value (Two-sided): {p_two_sided:.3e}")
    print(f"P-value (One-sided Lower): {p_one_sided:.3e}")

if __name__ == "__main__":
    DATA_FILE = 'data/processed/Filtered_Cardio_Data.csv'
    two_sample_t_test(DATA_FILE)