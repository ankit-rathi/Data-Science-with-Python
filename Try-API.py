from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Define your SQLite database file
DB_FILE = 'your_database.db'

# API route to select records from SQLite
@app.route('/select', methods=['POST'])
def select_records():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Extract data from the request
        data = request.json

        # Extract input parameters from the request JSON
        table_name = data.get('table_name')
        filter_conditions = data.get('filter_conditions')

        # Construct the SQL query
        sql_query = f"SELECT * FROM {table_name} WHERE {' AND '.join(filter_conditions)}"

        # Execute the SQL query
        cursor.execute(sql_query)

        # Fetch selected records
        records = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Return the selected records as JSON response
        return jsonify({'records': records}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
