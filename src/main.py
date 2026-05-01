#!/usr/bin/env python3
"""
IT 360 - Digital Forensics File Metadata & Hash Verification Tool
Course: IT 360 - Digital Forensics | Illinois State University
Team: Denvour, Chris, Justin
"""

import os
import hashlib
import csv
from datetime import datetime


def calculate_sha256(file_path):
    """
    Calculate the SHA-256 hash of a file.
    Reads in 4096-byte chunks to handle large files without memory issues.
    Returns the hex digest string, or an error message if the file is unreadable.
    """
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            for block in iter(lambda: file.read(4096), b""):
                sha256_hash.update(block)
        return sha256_hash.hexdigest()
    except Exception as error:
        return f"ERROR: {error}"


def format_timestamp(timestamp):
    """
    Convert a raw OS timestamp into a readable date/time string.
    Example output: 2026-05-01 14:32:05
    """
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


def scan_directory(evidence_directory, output_file):
    """
    Recursively scan all files in evidence_directory.
    Extracts metadata and SHA-256 hash for each file.
    Writes results to a CSV report at output_file.
    Prints a summary to the terminal when complete.
    """
    total_files = 0
    total_size = 0

    with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # Write CSV header row
        writer.writerow([
            "File Path",
            "File Name",
            "File Size (Bytes)",
            "Created/Changed Time",
            "Modified Time",
            "Accessed Time",
            "SHA-256 Hash"
        ])

        # Walk through every file in the evidence directory recursively
        for root, folders, files in os.walk(evidence_directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                try:
                    file_stats = os.stat(file_path)
                    file_size    = file_stats.st_size
                    created_time = format_timestamp(file_stats.st_ctime)
                    modified_time = format_timestamp(file_stats.st_mtime)
                    accessed_time = format_timestamp(file_stats.st_atime)
                    file_hash    = calculate_sha256(file_path)

                    writer.writerow([
                        file_path,
                        file_name,
                        file_size,
                        created_time,
                        modified_time,
                        accessed_time,
                        file_hash
                    ])

                    total_files += 1
                    total_size  += file_size

                except Exception as error:
                    # Log files that could not be read instead of crashing
                    writer.writerow([
                        file_path,
                        file_name,
                        "ERROR", "ERROR", "ERROR", "ERROR",
                        f"ERROR: {error}"
                    ])

    # Terminal summary
    print("\nScan Complete")
    print("----------------------------")
    print(f"Files analyzed:  {total_files}")
    print(f"Total size:      {total_size} bytes")
    print("Hash algorithm:  SHA-256")
    print(f"Report saved to: {output_file}")


if __name__ == "__main__":
    evidence_directory = "data/sample_evidence"
    output_directory   = "output"
    output_file        = "output/forensic_report.csv"

    # Create output folder if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Check evidence directory exists before scanning
    if not os.path.exists(evidence_directory):
        print(f"Evidence directory not found: {evidence_directory}")
        print("Please create the folder and add sample evidence files.")
    else:
        scan_directory(evidence_directory, output_file)
