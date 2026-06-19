# -*- coding: utf-8 -*-
"""
User API Module

Handles user-related operations.
Contains intentional issues for testing.
"""

import sqlite3
import hashlib
from typing import List, Optional


class UserAPI:
    """User API with intentional security and performance issues"""
    
    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
    
    def get_user_by_id(self, user_id: int) -> Optional[dict]:
        """
        Get user by ID
        
        SECURITY ISSUE: SQL Injection vulnerability
        """
        cursor = self.connection.cursor()
        # SECURITY ISSUE: SQL Injection vulnerability
        query = f"SELECT * FROM users WHERE id = {user_id}"
        cursor.execute(query)
        
        row = cursor.fetchone()
        if row:
            return {
                "id": row[0],
                "username": row[1],
                "email": row[2],
                "created_at": row[3]
            }
        return None
    
    def get_all_users(self) -> List[dict]:
        """
        Get all users
        
        PERFORMANCE ISSUE: No pagination
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
    
    def create_users_batch(self, users: List[tuple]) -> int:
        """Create multiple users efficiently using batch insert"""
        cursor = self.connection.cursor()
        
        hashed_users = []
        for username, email, password in users:
            if len(password) < 8:
                continue
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            hashed_users.append((username, email, password_hash))
        
        cursor.executemany(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            hashed_users
        )
        
        self.connection.commit()
        return cursor.rowcount
