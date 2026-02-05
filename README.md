# IT 360 Final Project  
## Digital Forensics File Metadata & Hash Verification Tool

## Team Members
- Member 1  
- Member 2  

## Project Overview
This project is a Python-based digital forensics tool designed to automate the process of file metadata extraction and file integrity verification. The tool scans a directory containing digital evidence and collects key forensic attributes such as file timestamps, file size, and cryptographic hash values.

The goal of this project is to apply concepts learned throughout the course and in the *Lab Access for Digital Forensics, Investigation, and Response (Fourth Edition)* textbook to a practical, hands-on forensic task. This tool replicates common evidence examination techniques used in real-world digital forensic investigations.

---

## Problem Statement
Manually collecting file metadata and verifying file integrity during a digital forensic investigation can be time-consuming and prone to human error. Investigators must ensure accuracy while maintaining evidence integrity.

This project addresses that problem by providing an automated and repeatable method for gathering forensic file metadata and generating cryptographic hashes to support evidence analysis and documentation.

---

## Features
- Recursively scans a directory of evidence files
- Extracts file metadata:
  - File name
  - File size
  - Created, modified, and accessed timestamps
- Generates SHA-256 hash values for file integrity verification
- Outputs results to a structured CSV forensic report
- Displays a summary of results in the terminal after execution

---

## Technologies Used
- Python 3
- Built-in Python libraries:
  - os
  - hashlib
  - csv
  - datetime

No external dependencies are required.

---

## Repository Structure
