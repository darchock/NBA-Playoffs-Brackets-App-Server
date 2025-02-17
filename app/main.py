from flask import Flask, jsonify
from flask_cors import CORS
from database.db_config import db
import logging

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.route('/api/data', methods=['GET'])
def get_users_data():
    try:
        # Execute query using the database connector
        users = db.execute_query("SELECT * FROM User")
        logger.info(f"Successfully retrieved {len(users)} users from database")
        print(users[0])
        return jsonify(users[0])
    except Exception as e:
        logger.error(f"Error retrieving users: {str(e)}")
        return jsonify({"error": "Failed to retrieve users"}), 500

if __name__ == "__main__":
    app.run(debug=True)
