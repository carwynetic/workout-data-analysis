import pandas as pd

def process_workout_data(input_path, output_path):
    # read the raw data
    df = pd.read_csv(input_path)

    #filter the data based on the specified criteria
    filtered_df = df.loc[
        (df['Age'].between(18, 25)) & 
        (df['Gender'] == 'Male') & 
        (df['Workout_Type'] == 'Cardio'),
        ['Age', 'Gender', 'Session_Duration (hours)', 'Calories_Burned', 'Workout_Type']
    ]

    # Save the filtered data to a new CSV file
    filtered_df.to_csv(output_path, index=False)
    print(f"Đã xử lý xong. Dữ liệu mới có {len(filtered_df)} dòng.")
    print(filtered_df.head())

if __name__ == "__main__":
    process_workout_data('data/raw/Final_data.csv', 'data/processed/Filtered_Cardio_Data.csv')