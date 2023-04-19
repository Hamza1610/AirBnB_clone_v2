#!/usr/bin/python3
"""Module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
