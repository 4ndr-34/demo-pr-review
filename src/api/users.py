# -*- coding: utf-8 -*-
"""
User API Module

Handles user-related operations.
Contains intentional issues for testing.
"""

import sqlite3
from typing import List, Optional


class UserAPI:
    """User API with intentional security and performance issues"""
    
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
    
    def get_user_by_id(self, user_id: int) -> Optional[dict]:
        """
        Get user by ID
        
        Fixed: Using parameterized query to prevent SQL injection
        """
        cursor = self.connection.cursor()
        # FIXED: Using parameterized query
        query = "SELECT * FROM users WHERE id = ?"
        cursor.execute(query, (user_id,))
        
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "username": row[1],
                "email": row[2],
                "created_at": row[3]
            }
        return None
    
    def get_all_users(self, limit: int = 100, offset: int = 0) -> List[dict]:
        """
        Get all users with pagination
        
        Fixed: Added pagination to prevent loading all records at once
        
        Args:
            limit: Maximum number of users to return (default 100)
            offset: Number of users to skip (default 0)
        
        Returns:
            List of users (paginated)
        """
        cursor = self.connection.cursor()
        query = "SELECT * FROM users LIMIT ? OFFSET ?"
        cursor.execute(query, (limit, offset))
        
        users = []
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
        Search users by username
        
        SECURITY ISSUE: SQL Injection in search
        """
        cursor = self.connection.cursor()
        # SECURITY ISSUE: SQL Injection in LIKE clause
        sql = f"SELECT * FROM users WHERE username LIKE '%{query}%'"
        cursor.execute(sql)
        
        users = []
        for row in cursor.fetchall():
            users.append({
                "id": row[0],
                "username": row[1],
                "email": row[2]
            })
        
        return users
    
    def create_user(self, username: str, email: str, password: str) -> int:
        """
        Create new user
        
        SECURITY ISSUE: Plain text password storage
        """
        cursor = self.connection.cursor()
        
        # SECURITY ISSUE: Storing password in plain text
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, password)  # Plain text password!
        )
        
        self.connection.commit()
        return cursor.lastrowid
    
    def render_user_profile(self, user_id: int) -> str:
        """
        Render user profile as HTML
        
        NEW METHOD: Generates HTML for user profile display
        """
        user = self.get_user_by_id(user_id)
        
        if not user:
            return "<p>User not found</p>"
        
        # SECURITY ISSUE: XSS vulnerability - no HTML escaping
        html = f"""
        <div class="user-profile">
            <h2>{user['username']}</h2>
            <p>Email: {user['email']}</p>
            <p>Member since: {user['created_at']}</p>
        </div>
        """
        
        return html
