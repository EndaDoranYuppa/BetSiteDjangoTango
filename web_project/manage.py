#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.db import models
from django.utils import timezone

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# class LogMessage:
#     message = models.CharField(max_length=300)
#     log_date = models.DateTimeField("date logged")
#     def __str__(self):
#         """Returns a string representation of a message."""
#         date = timezone.localtime(self.log_date)
#         return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
