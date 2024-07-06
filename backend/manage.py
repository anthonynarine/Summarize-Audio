#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_core.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
        
    # ensure the midai directory exists
    media_path = Path(__file__).resolve().parent / "meida"
    media_path.mkdir(parents=True, exist_ok=True)
    
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
