# -*- coding: utf-8 -*-
"""
User Model

Contains intentional architecture issues.
"""

from datetime import datetime
from typing import Optional


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
        """
        Validate password strength
        
        SECURITY ISSUE: Weak password validation
        """
        # SECURITY ISSUE: Very weak password validation
        return len(password) >= 6  # Should be much stronger!
    
    def send_welcome_email(self):
        """
        Send welcome email
        
        ARCHITECTURE ISSUE: Model should not handle email sending
        """
        # ARCHITECTURE ISSUE: Business logic in model
        print(f"Sending welcome email to {self.email}")
    
    def log_login(self):
        """
        Log user login
        
        ARCHITECTURE ISSUE: Model handling logging
        """
        # ARCHITECTURE ISSUE: Model should not handle logging
        print(f"User {self.username} logged in at {datetime.now()}")
    
    def calculate_reputation(self) -> int:
        """
        Calculate user reputation
        
        ARCHITECTURE ISSUE: Complex business logic in model
        """
        # ARCHITECTURE ISSUE: Business logic should be in service layer
        days_since_creation = (datetime.now() - self.created_at).days
        return days_since_creation * 10
    
    def to_dict(self) -> dict:
        """Convert user to dictionary"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }
