import pandas as pd
import sqlite3
import os
import json
import zipfile

# Step 1: Load CSV file into DataFrame
df = pd.read_csv('main.csv')

# Step 2: Save DataFrame to SQLite database
conn = sqlite3.connect('main.db')
df.to_sql('data', conn, if_exists='replace', index=False)
conn.close()

# Step 3: Save DataFrame to JSON file
df.to_json('main.json', orient='records', lines=True)

# Step 4: Zip the SQLite database and JSON file
with zipfile.ZipFile('data_backup.zip', 'w', compression=zipfile.ZIP_LZMA) as zipf:
    zipf.write('main.db')
    zipf.write('main.json')

# Step 5: Delete the original SQLite and JSON files
os.remove('main.db')
os.remove('main.json')

print("Backup completed and original files removed.")
