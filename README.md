# IT 360 Final Project Proposal

## Digital Forensics File Metadata & Hash Verification Tool

## Team Members
- Denvour  
- Chris
- Justin

---

## Project Overview
This project proposes the development of a Python-based digital forensics tool designed to automate the process of file metadata extraction and file integrity verification. The tool will scan a directory containing digital evidence and collect key forensic attributes such as file timestamps, file size, and cryptographic hash values.

The goal of this project is to apply concepts learned throughout the course and in the *Lab Access for Digital Forensics, Investigation, and Response (Fourth Edition)* textbook to a practical, hands-on forensic task. The proposed tool reflects common evidence examination techniques used in real-world digital forensic investigations.

---

## Problem Statement
Manually collecting file metadata and verifying file integrity during a digital forensic investigation can be time-consuming and prone to human error. Investigators must ensure accuracy while maintaining evidence integrity throughout the investigation process.

This project addresses that problem by proposing an automated and repeatable method for gathering forensic file metadata and generating cryptographic hash values to support evidence analysis and documentation.

---

## Proposed Features
- Recursively scan a directory of evidence files  
- Extract forensic file metadata, including:
  - File name  
  - File size  
  - Created, modified, and accessed timestamps  
- Generate SHA-256 hash values for file integrity verification  
- Output results to a structured CSV forensic report  
- Display a summary of results in the terminal after execution  

---

## Technologies Used
- Python 3  
- Built-in Python libraries:
  - `os`
  - `hashlib`
  - `csv`
  - `datetime`  

No external dependencies will be required.

---

## Expected Output
The final tool will generate a CSV-based forensic report containing file metadata and cryptographic hash values for each analyzed file. The tool will also display a terminal summary confirming the number of files analyzed and the successful completion of the forensic process.

---

## Project Scope and Timeline
This project is to be achievable by a 3-person team within the course timeframe. Development will focus on implementing core forensic functionality aligned with weekly lab exercises, followed by documentation and a recorded video demonstration.
---

# Planned Repository Structure

```text
IT_360_FINAL_Project/
│
├── src/
│   └── main.py
│
├── data/
│   └── sample_evidence/
│
├── output/
│
├── docs/
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

# Planned Installation and Setup

## Prerequisites
- Python 3.x
- Git (optional)

Verify Python installation:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Cloning the Repository

```bash
git clone https://github.com/denvour04/IT_360_FINAL_Project.git
```

Navigate into the project directory:

```bash
cd IT_360_FINAL_Project
```

---

# Planned Usage

1. Place evidence files inside:

```text
data/sample_evidence/
```

2. Run the tool:

```bash
python src/main.py
```

or:

```bash
python3 src/main.py
```

3. View the generated report inside:

```text
output/forensic_report.csv
```

---

## How to Use the Tool

Place evidence files inside:

```text

data/sample_evidence/

```

Example evidence files may include:

```text

.txt

.pdf

.jpg

.png

.docx

```

Run the tool:

```bash

python src/main.py

```

or:

```bash

python3 src/main.py

```

---

## Output

After the tool runs, it creates a CSV report at:

```text

output/forensic_report.csv

```

The report includes:

- File path

- File name

- File size

- Created/changed time

- Modified time

- Accessed time

- SHA-256 hash

---

## Example Terminal Output

```text

Scan Complete

----------------------------

Files analyzed: 1

Total size: 103 bytes

Hash algorithm: SHA-256

Report saved to: output/forensic_report.csv

```

---


---


# Forensic Relevance

This project demonstrates several core digital forensics concepts covered throughout IT 360 and the *Lab Access for Digital Forensics, Investigation, and Response (Fourth Edition)* textbook, including:

- File metadata analysis
- Evidence documentation
- File integrity verification
- Cryptographic hashing
- Automated forensic reporting

The tool will perform read-only analysis and will not modify original evidence files.

---

# Future Improvements

Possible future improvements include:
- Graphical user interface (GUI)
- Additional hash algorithms
- Support for forensic disk image analysis
- Log analysis integration
- PDF report generation

---

## Limitations

On Windows, the created/changed timestamp usually represents file creation time. On macOS and Linux, this timestamp may represent metadata change time instead of original file creation time.

This tool is designed for basic file metadata and hash verification. It does not analyze full disk images or recover deleted files.

---

## Final Report

The written report will be located in:

```text

docs/final_report.pdf

```

---

## Video Presentation

Video Link: To be added


---

# License

This project will use the MIT License.
