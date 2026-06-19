# -*- coding: utf-8 -*-
"""
User Model

Contains intentional architecture issues.
"""

from datetime import datetime
from typing import Optional
import hashlib


class User:
    """
    User model
    
    ARCHITECTURE ISSUE: Business logic in model (god class pattern)
    """
    
    def __init__(self, id: int, username: str, email: str, password: str):
        self.id = id
        self.username = self._validate_and_clean_username(username)
        self.email = self._validate_and_clean_email(email)
        self.password = self._hash_and_validate_password(password)
        self.created_at = datetime.now()
        self._setup_logging()
        self._initialize_cache()
        self._connect_to_notification_service()
    
    def _validate_and_clean_username(self, username: str) -> str:
        username = username.strip().lower()
        if len(username) < 3:
            raise ValueError("Username too short")
        return username
    
    def _validate_and_clean_email(self, email: str) -> str:
        email = email.strip().lower()
        if '@' not in email:
            raise ValueError("Invalid email")
        return email
    
    def _hash_and_validate_password(self, password: str) -> str:
        if len(password) < 8:
            raise ValueError("Password too short")
        return hashlib.sha256(password.encode()).hexdigest()
    
    def _setup_logging(self):
        self.log_file = f"user_{self.id}.log"
    
    def _initialize_cache(self):
        self.cache = {}
    
    def _connect_to_notification_service(self):
        self.notifications_enabled = True
    
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
