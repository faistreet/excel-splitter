def split_excel_sheets(file_path):
    import pandas as pd
    import os

    # Load the Excel file
    xls = pd.ExcelFile(file_path)

    # Create a directory to save the sheets if it doesn't exist
    output_dir = os.path.splitext(file_path)[0] + "_sheets"
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through each sheet and save it as a separate Excel file
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        output_file = os.path.join(output_dir, f"{sheet_name}.xlsx")
        df.to_excel(output_file, index=False)

    return output_dir

def handle_file_path(file_path):
    import os

    # Ensure the file path is valid
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    return os.path.abspath(file_path)