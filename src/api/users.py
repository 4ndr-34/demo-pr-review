# -*- coding: utf-8 -*-
"""
User API Module

Handles user-related operations.
Contains intentional issues for testing.
"""

import sqlite3
from typing import List, Optional


class ConnectionPool:
    """Simple connection pool for database"""
    def __init__(self, db_path: str, pool_size: int = 5):
        self.db_path = db_path
        self.pool = [sqlite3.connect(db_path) for _ in range(pool_size)]
        self.available = list(self.pool)
    
    def get_connection(self):
        if self.available:
            return self.available.pop()
        return sqlite3.connect(self.db_path)
    
    def return_connection(self, conn):
        if len(self.available) < len(self.pool):
            self.available.append(conn)


class UserAPI:
    """User API with connection pooling"""
    
    def __init__(self, db_path: str):
        self.pool = ConnectionPool(db_path)
        self.connection = self.pool.get_connection()
    
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
