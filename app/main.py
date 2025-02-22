from flask import Flask, jsonify
from flask_cors import CORS
# from database.db_config import db
from database.database_alchemy import get_db, engine
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, declarative_base
from models.models import User
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

@app.route('/api/users/<string:user_id>', methods=['GET'])
def get_user_email(user_id):
    try:
        print(f"Given user_id from client: {user_id}")
        db = next(get_db())
        user = db.query(User).filter(User.user_id == user_id).first()
        print(f"Returned email from querry: {user.email}")
        if user is None:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify({"email": user.email}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

if __name__ == "__main__":
    app.run(debug=True)
