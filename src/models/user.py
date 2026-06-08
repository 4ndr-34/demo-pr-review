"""
User data model

Represents a user in the system.
"""

from datetime import datetime
from typing import Optional


class User:
    """User model"""
    
    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email
        self.created_at = datetime.now()
        self.password = None  # Should not be stored here
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": str(self.created_at)
        }
    
    def from_dict(self, data: dict):
        """Load from dictionary"""
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.created_at = datetime.fromisoformat(data['created_at'])
    
    # ARCHITECTURE ISSUE: Business logic in model
    def send_welcome_email(self):
        """Send welcome email to user"""
        # This should be in a service layer
        print(f"Sending welcome email to {self.email}")
    
    def validate_password(self, password: str) -> bool:
        """Validate password"""
        # SECURITY ISSUE: Weak password validation
        return len(password) >= 6
