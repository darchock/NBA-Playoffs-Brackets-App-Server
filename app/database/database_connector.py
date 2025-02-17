import mysql.connector
from mysql.connector import Error
from typing import Optional, List, Dict, Any
import logging
from contextlib import contextmanager

class DatabaseConnector:
    def __init__(self, host: str, database: str, user: str, password: str):
        """Initialize database connection parameters."""
        self.config = {
            'host': host,
            'database': database,
            'user': user,
            'password': password
        }
        self.setup_logging()

    def setup_logging(self):
        """Configure logging for database operations."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('DatabaseConnector')

    @contextmanager
    def get_connection(self):
        """Context manager for database connections."""
        conn = None
        try:
            conn = mysql.connector.connect(**self.config)
            self.logger.info("Database connection established successfully")
            yield conn
        except Error as e:
            self.logger.error(f"Error connecting to database: {e}")
            raise
        finally:
            if conn and conn.is_connected():
                conn.close()
                self.logger.info("Database connection closed")

    def execute_query(self, query: str, params: tuple = None) -> Optional[List[Dict[str, Any]]]:
        """Execute a query and return results."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor(dictionary=True)
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                if query.strip().upper().startswith('SELECT'):
                    results = cursor.fetchall()
                    return results
                else:
                    conn.commit()
                    return None

        except Error as e:
            self.logger.error(f"Error executing query: {e}")
            raise