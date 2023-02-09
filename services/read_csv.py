from flask import request
import pandas as pd

#COMPARE BOTH CSV FILES BY ROW
def read_by_row_csv_logic(**kwargs):

    file1 = str(request.args.get('file1'))
    file2 = str(request.args.get('file2'))
    column_name1 = str(request.args.get('column_name1'))
    column_name2 = str(request.args.get('column_name2'))

    # Read the CSV files into pandas DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    print(df1.iterrows())
    # # Sort both DataFrames by column_name1
    # sorted_df1 = df1.sort_values(by=[column_name1])
    # sorted_df2 = df2.sort_values(by=[column_name1])

    # Compare the specified columns
    for index, row in df1.iterrows():
        value1 = (row[column_name1], row[column_name2])
        value2 = (df2.loc[index, column_name1], df2.loc[index, column_name2])
        if value2 != value1:
            print(f"Mismatch: {value2} != {value1} and Not Located in {file1}")
        if value2 in value1:
            print(f"Match: {value2} == {value1} and Located in {file1}")    

    return{'Message':'Success'}

#COMPARE BOTH CSV FILES BY VALUES IN COLUMN
def read_csv_logic(**kwargs):

    file1 = str(request.args.get('file1'))
    file2 = str(request.args.get('file2'))
    column_name1 = str(request.args.get('column_name1'))
    column_name2 = str(request.args.get('column_name2'))

    # Read the CSV files into pandas DataFrames
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Select the columns to be compared
    column1 = df1[column_name1]
    column2 = df2[column_name2]

    # Convert the selected columns to sets and compare them
    set1 = set(column1)
    set2 = set(column2)

    # Check if the sets are equal
    if set1 == set2:
        print("The values in both columns are equal.")
    else:
        print("The values in both columns are not equal.")
  
    return{'Message':'Success'}

