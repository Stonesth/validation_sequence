# Sequence Modifier

This project is designed to modify sequences in a specified file located in the `files` directory. The main functionality includes reading the content of the file, adjusting the sequence values starting from line 1682, and writing the corrected content back to the file.

## Project Structure

```
sequence-modifier
├── files
│   └── sample_file.txt
├── src
│   ├── main.py
│   └── utils.py
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository or download the project files.
2. Navigate to the project directory.

## Installation
To create the local env
py -m venv venv

<!-- Activate the local envrionment -->
# In Unix/Linux/macOS
source venv/bin/activate 
 # In Windows
venv\Scripts\activate

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

This will read the `sample_file.txt`, modify the sequences starting from line 1682, and save the changes back to the file.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.