import pandas as pd
import sqlite3
import unittest
import json
import zipfile
import numpy as np

class TestDataBackup(unittest.TestCase):
    def setUp(self):
        # Extract files from zip
        with zipfile.ZipFile("data_backup.zip", 'r') as zip_ref:
            zip_ref.extractall("temp_data")

        # Load CSV into DataFrame
        self.original_df = pd.read_csv("main.csv")

        # Load JSON into DataFrame
        with open("temp_data/main.json", "r") as file:
            # Read lines individually and parse each one as JSON
            json_data = [json.loads(line) for line in file]

        self.json_df = pd.json_normalize(json_data)

        # SQLite setup
        self.conn = sqlite3.connect("temp_data/main.db")

        self.sqlite_df = pd.read_sql_query("SELECT * FROM data", self.conn)
        print(self.original_df.head())
        print(self.json_df.head())


    def test_full_data_integrity_json(self):
        diffs = {}
        for column in ['sentiment_score', 'emotion_score']:
            if not np.allclose(self.original_df[column], self.json_df[column], atol=1e-8):
                diffs[column] = self.original_df[column] - self.json_df[column]

        if diffs:
            for col, diff in diffs.items():
                print(f"Differences in {col}:")
                print(diff[diff != 0])  # Print only non-zero differences
            self.fail("Significant differences were found between CSV and JSON DataFrames")
        else:
            print("No significant differences found.")

    def test_full_data_integrity_sqlite(self):
        """Test each row from the CSV data for full data integrity in SQLite."""
    # Compare the two DataFrames
        differences = self.original_df.compare(self.sqlite_df)
        # Check if there are any differences
        if not differences.empty:
            print("Differences found between CSV and SQLite DataFrames:")
            print(differences)
            self.fail("Data integrity test failed: Differences found between CSV and SQLite DataFrames")
        else:
            print("No differences found: Data integrity test passed")

    def tearDown(self):
        """Close the database connections and clean up temporary files."""
        self.conn.close()
        import shutil
        shutil.rmtree('temp_data')  # Clean up the directory

if __name__ == '__main__':
    unittest.main()

