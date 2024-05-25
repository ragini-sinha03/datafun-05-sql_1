import sqlite3
import csv

# Define the database file name and location
db_file = "project.db"
new_author_id = "12"
new_first_name = "Mark"
new_last_name = 'Twain'

def insert_author(author_id):

    conn = sqlite3.connect(db_file)

    try:
        # Connect to the database
        cursor = conn.cursor()
        print ("Hi")
        # Insert a new author into the authors table
        insert_command = """
        INSERT INTO authors (author_id, first_name)
        VALUES (?,?)
        """

        cursor.execute(insert_command, (author_id))
        
        # Commit the transaction
        conn.commit()
        print("New author added successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting new author: {e}")
    finally:
        # Close the connection
        conn.close()


def main():
    insert_author(author_id, first_name )



if __name__ == "__main__":
    db_name = 'project.db'
    main()
    
    
