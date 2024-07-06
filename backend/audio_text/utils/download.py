import os
import re
from pytube import YouTube

def sanitize_filename(filename):
    """
    Sanitizes the filename by replacing spaces with underscores and removing special characters.

    Args:
        filename (str): The original filename.
        
    Returns:
        str: The sanitized filename.
    """
    # Replace spaces with underscores
    filename = filename.replace(" ", "_")
    # Remove any characters that are not alphanumeric, underscores, hyphens, or dots
    filename = re.sub(r'[^a-zA-Z0-9._-]', '', filename)
    return filename
