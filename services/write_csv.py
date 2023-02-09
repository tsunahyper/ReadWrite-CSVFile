from flask import request
import pandas as pd

def write_csv_logic(**kwargs):
    # Read the CSV files into pandas DataFrames
    old_file = str(request.args.get('old_file'))
    new_file = str(request.args.get('old_file'))
    df2 = pd.read_csv(old_file)

    df2['Specialisation'] = df2['Specialisation'].astype(str)
    df2.dropna(subset=['Specialisation'], inplace=True)

    # Compare the specified columns
    for index, row in df2.iterrows():
        if df2.loc[index, 'Specialisation'] == "Current Value":
            # Replace the specified columns value
            df2.at[index, 'Programme'] = "New Value"

        if df2.loc[index, 'Specialisation'] == "Current Value":
            # Replace the specified columns value
            df2.at[index, 'Programme'] = "New Value"

        if df2.loc[index, 'Specialisation'] == "Current Value":
            # Replace the specified columns value
            df2.at[index, 'Programme'] = "New Value"
    df2.to_csv(new_file, index=False)        

    return{'Message':'Success'}