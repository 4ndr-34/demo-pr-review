# -*- coding: utf-8 -*-
"""
User Model

Contains intentional architecture issues.
"""

from datetime import datetime
from typing import Optional


class UserService:
    """Service layer for user business logic"""
    
    @staticmethod
    def validate_password_strength(password: str) -> bool:
        """Validate password meets security requirements"""
        return len(password) >= 8
    
    @staticmethod
    def calculate_reputation(created_at: datetime) -> int:
        """Calculate user reputation score"""
        days_active = (datetime.now() - created_at).days
        return days_active * 10
    
    @staticmethod
    def send_welcome_email(email: str):
        """Send welcome email to new user"""
        print(f"Sending welcome email to {email}")
    
    @staticmethod
    def log_user_activity(username: str, action: str):
        """Log user activity"""
        print(f"User {username} performed: {action} at {datetime.now()}")


class User:
    """
    User model
    
    ARCHITECTURE ISSUE: Business logic in model (god class pattern)
    """
    
    def __init__(self, id: int, username: str, email: str, password: str):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = datetime.now()
    
    def validate_password(self, password: str) -> bool:
        """Validate password using service layer"""
        return UserService.validate_password_strength(password)
    
    def send_welcome_email(self):
        """Delegate to service layer"""
        UserService.send_welcome_email(self.email)
    
    def log_login(self):
        """Delegate to service layer"""
        UserService.log_user_activity(self.username, 'login')
    
    def calculate_reputation(self) -> int:
        """Delegate to service layer"""
        return UserService.calculate_reputation(self.created_at)
    
    def to_dict(self) -> dict:
        """Convert user to dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }
