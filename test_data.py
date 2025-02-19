import unittest
import pandas as pd

class TestMainCsvData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load the data once before all tests
        cls.df = pd.read_csv("main.csv")

    def test_file_not_empty(self):
        # Check that the dataframe is not empty
        self.assertFalse(self.df.empty, "The CSV file is empty.")

    def test_columns_existence(self):
        # Verify all expected columns are in the dataframe
        expected_columns = [
            'Unnamed: 0','DATE', 'AUTHOR', 'TITLE', 'cleaned', 'sentiment',
            'sentiment_score', 'emotion', 'emotion_score', 'ARTICLE'
        ]
        self.assertListEqual(list(self.df.columns), expected_columns, "Not all expected columns are present.")

    def test_no_missing_values(self):
        # Check for missing values in crucial columns
        crucial_columns = ['DATE', 'AUTHOR', 'sentiment', 'emotion', 'sentiment_score', 'emotion_score']
        for column in crucial_columns:
            self.assertFalse(self.df[column].isnull().any(), f"Missing values found in {column}.")

    def test_date_format(self):
        # Check if 'DATE' column is in the correct format
        try:
            pd.to_datetime(self.df['DATE'], format='%Y-%m-%d')  # Adjust format as per your date format in CSV
            date_format_issue = False
        except ValueError:
            date_format_issue = True
        self.assertFalse(date_format_issue, "Date format is incorrect.")

    def test_data_types(self):
        # Ensure that specific columns have the correct data type
        self.assertTrue(pd.api.types.is_float_dtype(self.df['sentiment_score']), "Sentiment Score column is not a float.")
        self.assertTrue(pd.api.types.is_float_dtype(self.df['emotion_score']), "Emotion Score column is not a float.")

    def test_score_ranges(self):
        # Check if sentiment and emotion scores fall within expected ranges
        self.assertTrue(self.df['sentiment_score'].between(0, 1).all(), "Sentiment scores are out of the expected range (0-1).")
        self.assertTrue(self.df['emotion_score'].between(0, 1).all(), "Emotion scores are out of the expected range (0-1).")

if __name__ == '__main__':
    unittest.main()
