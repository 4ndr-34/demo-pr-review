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
    
    def get_all_users(self, limit: int = 100, offset: int = 0) -> List[dict]:
        """Get all users with pagination and null safety"""
        if limit is None or limit <= 0:
            limit = 100
        if offset is None or offset < 0:
            offset = 0
        
        cursor = self.connection.cursor()
        query = "SELECT * FROM users LIMIT ? OFFSET ?"
        cursor.execute(query, (limit, offset))
        
        users = []
        for row in cursor.fetchall():
            if row and len(row) >= 4:
                for field in row:
                    if field is None:
                        continue
                users.append({
                    "id": row[0] if row[0] is not None else 0,
                    "username": row[1] if row[1] is not None else "",
                    "email": row[2] if row[2] is not None else "",
                    "created_at": row[3] if row[3] is not None else ""
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
