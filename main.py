import pandas as pd

# Read the Excel file
october_output_file_path = 'october_transfers.xls'
november_output_file_path = 'november_transfers.xls'
december_output_file_path = 'december_transfers.xls'
january_output_file_path = 'january_transfers.xls'
df = pd.read_excel('mank_transfers.xls')

# Initialize month DataFrames as global variables
october_df = pd.DataFrame()
november_df = pd.DataFrame()
december_df = pd.DataFrame()
january_df = pd.DataFrame()

# Display the first few rows of the DataFrame
#print(df.head())

# Ensure the first column is in datetime format
# Assuming the first column is named 'Date', replace it with the actual column name
#df['Date'] = pd.to_datetime(df['Date'])

#  Filter and store data for each month in separate variables
def separate_data():
    global october_df, november_df, december_df, january_df
    october_df = df[df['Data waluty'].dt.month == 10]
    november_df = df[df['Data waluty'].dt.month == 11]
    december_df = df[df['Data waluty'].dt.month == 12]
    january_df = df[df['Data waluty'].dt.month == 1]

# Write the filtered data to a new Excel file
def separate_xls():
    global october_df, november_df, december_df, january_df
    december_df.to_excel(december_output_file_path, index=False)

def print_all_records():
    global october_df, november_df, december_df, january_df
    for index, row in df.iterrows():
        print(row)

def print_data_for_each_month():
    global october_df, november_df, december_df, january_df
    print("January records:", len(january_df))
    print(january_df)
    #print("February records:", len(february_data))
    #print("March records:", len(march_data))

separate_data()
print_data_for_each_month()