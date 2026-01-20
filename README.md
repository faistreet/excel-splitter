# Excel Splitter

This project is a Python application that reads an Excel file containing multiple sheets and separates each sheet into individual Excel files.

## Installation

To get started, clone the repository and install the required dependencies. You can do this by running:

```bash
pip install -r requirements.txt
```

## Usage

To use the Excel Splitter, run the main script with the path to the Excel file you want to split. For example:

```bash
python src/main.py path/to/your/excel_file.xlsx
```

This will create separate Excel files for each sheet in the specified directory.

## Example

Given an Excel file named `data.xlsx` with sheets named `Sheet1`, `Sheet2`, and `Sheet3`, running the command will generate:

- `Sheet1.xlsx`
- `Sheet2.xlsx`
- `Sheet3.xlsx`

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. 

## License

This project is licensed under the MIT License.