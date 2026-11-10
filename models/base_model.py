#!/usr/bin/python3
"""Defines the BaseModel class, the parent of all AirBnB clone classes."""
import uuid
from datetime import datetime


class BaseModel:
    """Represents the base model that all other classes inherit from."""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance with a unique id and timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary of all instance attributes plus __class__."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
EOF
