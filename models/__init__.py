#!/usr/bin/python3
"""
    creating unique FileStorage instance for this application
"""
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
