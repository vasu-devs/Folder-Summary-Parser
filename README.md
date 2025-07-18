# Folder Summary Parser

A simple Python GUI application that analyzes folder contents and provides detailed statistics about files, folders, sizes, and file types.

## Features

- **Folder Analysis**: Recursively scans selected folders and subfolders
- **File Statistics**: Counts total files and folders
- **Size Calculation**: Shows total size in human-readable format (B, KB, MB, GB, TB)
- **File Type Breakdown**: Groups files by extension and shows counts
- **User-Friendly GUI**: Simple Tkinter interface for easy folder selection
- **Error Handling**: Gracefully handles inaccessible files

## Screenshots

The application displays:
- 📁 Total number of folders
- 📄 Total number of files  
- 💾 Total size (formatted and in bytes)
- 📦 File types breakdown with counts

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)
- No additional external dependencies required

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Run the application:

```bash
python main.py
```

## Usage

1. Launch the application by running `main.py`
2. Click the "Select Folder" button
3. Choose the folder you want to analyze
4. View the summary statistics displayed in the GUI

## Project Structure

```
Folder Summary Parser/
├── main.py          # Entry point - launches the GUI
├── gui.py           # GUI implementation using tkinter
├── parser.py        # Core folder parsing logic
├── utils.py         # Utility functions (size formatting)
├── test.py          # Test script for manual testing
└── README.md        # This file
```

## How It Works

1. **Folder Selection**: Users select a folder through a file dialog
2. **Recursive Scanning**: The `parse_folder()` function uses `os.walk()` to traverse all subdirectories
3. **Statistics Collection**: Counts files, folders, calculates sizes, and groups by file extensions
4. **Display**: Results are formatted and displayed in the GUI with emoji indicators

## Example Output

```
📁 Folders: 15
📄 Files: 127
💾 Total Size: 2.45 MB (2567890 bytes)

📦 File Types:
 .py: 8
 .txt: 15
 .md: 3
 .json: 2
 [no ext]: 1
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the [MIT License](LICENSE).