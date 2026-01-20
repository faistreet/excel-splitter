import pandas as pd
import os

def split_excel_sheets(file_path):
    # Load the Excel file
    excel_file = pd.ExcelFile(file_path)
    
    # Create a directory to save the individual sheets
    output_dir = os.path.splitext(file_path)[0] + "_sheets"
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate through each sheet and save it as a separate Excel file
    for sheet_name in excel_file.sheet_names:
        sheet_data = excel_file.parse(sheet_name)
        output_file_path = os.path.join(output_dir, f"{sheet_name}.xlsx")
        sheet_data.to_excel(output_file_path, index=False)
        print(f"Saved {sheet_name} to {output_file_path}")

if __name__ == "__main__":
    input_file = input("Enter the path of the Excel file: ")
    split_excel_sheets(input_file)