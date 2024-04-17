# Remitly_Internship_2024

## Description
The application is designed to check to check correctness of AWS::IAM::Role Policy JSON file. It raises error when file's syntax is incorrect.

## Features
* checking for correctness of AWS::IAM::Role Policy JSON file format
* informs about '*' sign existance in "Resource" field

## Requirements
* Python 3.x: The program is written in Python and requires an installed Python interpreter version 3.x.

## External sources
* [JSONschema](https://json-schema.org/) - library for checking correctness of AWS IAM Policy JSON grammar
* [AWS IAM Policy JSON Schema](https://gist.github.com/jstewmon/ee5d4b7ec0d8d60cbc303cb515272f8a?permalink_comment_id=3884576) - configured shcema for JSONschema library

## Structure
* JsonReader.py - program checking correctness of AWS IAM Policy JSON grammar.
* test_JsonReader.py - tests for JsonReader.py.
* test_wrong_syntax_data - directory containing input files with AWS IAM Policy JSON that have wrong syntax.
* test_true_data - directory containing input files with AWS IAM Policy JSON that "Resource" field is defferent than "*".
* test_false_data - directory containing input files with AWS IAM Policy JSON that "Resource" field is "*".

## Instalation
1. Clone the repository to your device:
   ```bash
   git clone https://github.com/Sitaarz/Remitly_Internship_2024.git
   ```
2. Install the required Python libraries using a package manager like pip:
   ```bash
   cd Remitly_Internship_2024
   pip install -r requirements.txt
   ```
   
## Usage
1. Enter project directory.
2. Type:
   ```bash
   python RemitlyIsTheBest.py pathToTestedJSONFile
   ```

## Tests running
1. Enter project directory.
2. Type:
   ```bash
   python test_JsonReader.py
   ```
