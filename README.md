IT 360 Final Project
Digital Forensics File Metadata & Hash Verification Tool
Team Members

Denver (denvour04)

Chris Nkwo (CINKWO)

Justin Ray

Project Overview

This project is a Python-based digital forensics tool designed to automate the process of file metadata extraction and file integrity verification. The tool scans a directory containing digital evidence and collects key forensic attributes such as file timestamps, file size, and cryptographic hash values.
The goal of this project is to apply concepts learned throughout the course and in the Lab Access for Digital Forensics, Investigation, and Response (Fourth Edition) textbook to a practical, hands-on forensic task. This tool replicates common evidence examination techniques used in real-world digital forensic investigations.

Problem Statement

Manually collecting file metadata and verifying file integrity during a digital forensic investigation is time-consuming and prone to human error. Investigators must ensure accuracy while maintaining evidence integrity.
This project addresses that problem by providing an automated and repeatable method for gathering forensic file metadata and generating cryptographic hashes to support evidence analysis and documentation.

Features

Recursively scans a directory of evidence files
Extracts file metadata: file name, file size, created/modified/accessed timestamps
Generates SHA-256 hash values for file integrity verification
Outputs results to a structured CSV forensic report
Displays a summary in the terminal after execution


Technologies Used

Python 3
Built-in libraries: os, hashlib, csv, datetime
No external dependencies required


How to Run


Make sure Python 3 is installed

Clone the repository: git clone https://github.com/denvour04/IT_360_FINAL_Project.git

Navigate into the folder: cd IT_360_FINAL_Project

Run the tool: python src/main.py

View the report at output/forensic_report.csv


Course
IT 360 — Digital Forensics
Illinois State University
