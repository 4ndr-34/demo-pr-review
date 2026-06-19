import unittest
from src.api.users import UserAPI
import sqlite3


class TestUserAPI(unittest.TestCase):
    """Test suite for UserAPI class"""
    
    def setUp(self):
        """Set up test database"""
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute(
            'CREATE TABLE users (id INTEGER, username TEXT, email TEXT, password TEXT, created_at TEXT)'
        )
        self.conn.commit()
    
    def tearDown(self):
        """Clean up test database"""
        self.conn.close()
    
    def test_get_user_by_id_returns_none_for_missing_user(self):
        """Test that get_user_by_id returns None for non-existent users"""
        api = UserAPI(':memory:')
        result = api.get_user_by_id(999)
        self.assertIsNone(result)
    
    def test_create_user_with_valid_data(self):
        """Test creating user with valid inputs"""
        api = UserAPI(':memory:')
        user_id = api.create_user('testuser', 'test@example.com', 'password123')
        self.assertIsInstance(user_id, int)
        self.assertGreater(user_id, 0)
    
    def test_search_users_returns_empty_for_no_match(self):
        """Test that search returns empty list when no users match"""
        api = UserAPI(':memory:')
        results = api.search_users('nonexistent')
        self.assertEqual(len(results), 0)
    
    def test_get_all_users_returns_list(self):
        """Test that get_all_users returns a list"""
        api = UserAPI(':memory:')
        users = api.get_all_users()
        self.assertIsInstance(users, list)


if __name__ == '__main__':
    unittest.main()
