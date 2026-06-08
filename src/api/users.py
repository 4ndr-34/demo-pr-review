"""
User API endpoints

This module handles user-related API operations.
"""

from typing import List, Optional
import sqlite3


class UserAPI:
    """User management API"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = None
    
    def connect(self):
        """Connect to database"""
        self.connection = sqlite3.connect(self.db_path)
    
    def get_user_by_id(self, user_id: str) -> Optional[dict]:
        """
        Get user by ID
        
        Args:
            user_id: User ID to fetch
            
        Returns:
            User data or None
        """
        cursor = self.connection.cursor()
        
        # SECURITY ISSUE: SQL Injection vulnerability
        query = f"SELECT * FROM users WHERE id = {user_id}"
        cursor.execute(query)
        
        result = cursor.fetchone()
        if result:
            return {
                "id": result[0],
                "username": result[1],
                "email": result[2],
                "created_at": result[3]
            }
        return None
    
    def get_all_users(self) -> List[dict]:
        """
        Get all users
        
        Returns:
            List of all users
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        
        users = []
        # PERFORMANCE ISSUE: Loading all users without pagination
        for row in cursor.fetchall():
            users.append({
                "id": row[0],
                "username": row[1],
                "email": row[2],
                "created_at": row[3]
            })
        
        return users
    
    def search_users(self, query: str) -> List[dict]:
        """
        Search users by username or email
        
        Args:
            query: Search query
            
        Returns:
            Matching users
        """
        cursor = self.connection.cursor()
        
        # SECURITY ISSUE: SQL Injection vulnerability
        sql = f"SELECT * FROM users WHERE username LIKE '%{query}%' OR email LIKE '%{query}%'"
        cursor.execute(sql)
        
        results = []
        for row in cursor.fetchall():
            results.append({
                "id": row[0],
                "username": row[1],
                "email": row[2],
                "created_at": row[3]
            })
        
        return results
    
    def create_user(self, username: str, email: str, password: str) -> int:
        """
        Create new user
        
        Args:
            username: Username
            email: Email address
            password: Password (plain text)
            
        Returns:
            New user ID
        """
        cursor = self.connection.cursor()
        
        # SECURITY ISSUE: Storing password in plain text
        # SECURITY ISSUE: No input validation
        query = f"INSERT INTO users (username, email, password) VALUES ('{username}', '{email}', '{password}')"
        cursor.execute(query)
        
        self.connection.commit()
        return cursor.lastrowid
    
    def get_user_posts(self, user_id: int) -> List[dict]:
        """
        Get all posts for a user
        
        Args:
            user_id: User ID
            
        Returns:
            List of user posts
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM posts WHERE user_id = ?", (user_id,))
        
        posts = []
        for row in cursor.fetchall():
            # PERFORMANCE ISSUE: N+1 query problem
            # Fetching comments for each post individually
            cursor2 = self.connection.cursor()
            cursor2.execute("SELECT * FROM comments WHERE post_id = ?", (row[0],))
            comments = cursor2.fetchall()
            
            posts.append({
                "id": row[0],
                "title": row[1],
                "content": row[2],
                "user_id": row[3],
                "comments": len(comments)
            })
        
        return posts
