import sqlite3  
import pandas as pd  
import csv
from pathlib import Path

# Define the database file name and location
db_file = "project.db"

# Function to create a new SQLite database
def create_database():
    try:
        # Connect to the database (or create it if it doesn't exist)
        conn = sqlite3.connect(db_file)
        # Close the connection
        conn.close()
        # Print a success message
        print("Database created successfully.")
    except sqlite3.Error as e:
        # Print error message if there's an issue creating the database
        print("Error creating the database:", e)

# Function to create tables in the database

def create_table_from_csv(conn, csv_file):
    try:
        # Create a cursor object to execute SQL commands
        cursor = conn.cursor()
        
        # Extract table name from CSV filename
        table_name = Path(csv_file).stem
        
        # Read the first row of the CSV file to get column names
        with open(csv_file, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            
            headers = next(csvreader)
            # Generate CREATE TABLE command dynamically
            create_table_command = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'\"{header}\" TEXT' for header in headers])})"
            cursor.execute(create_table_command)
        
        # Read values from the CSV file and insert them into the table
        with open(csv_file, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip header row
            for row in csvreader:
                insert_command = f"INSERT INTO {table_name} VALUES ({', '.join(['?' for _ in row])})"
                cursor.execute(insert_command, tuple(row))
        
        print(f"Table '{table_name}' created and data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table from CSV: {e}")

def main():
    # Directory containing CSV files
    csv_directory = Path("data")
    print (csv_directory)
    
    # Path to the SQLite database file
    db_name = 'project.db'
    
    # Connect to the database
    try:
        conn = sqlite3.connect(db_name)
        for file in csv_directory.glob("*.csv"):
            print (file)
            create_table_from_csv(conn, file)
        # Commit the transaction
        conn.commit()
        print("All tables created and data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error connecting to SQLite database: {e}")
    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    main()


    
           