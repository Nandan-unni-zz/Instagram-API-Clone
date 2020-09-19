#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from colorama import Fore, Style


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API.settings')
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
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA, Style.BRIGHT, '\n\b\b[#]', Fore.RED, 'Starting Server', Style.RESET_ALL)
    main()
    print(Fore.MAGENTA, Style.BRIGHT, '\n\b\b[#]', Fore.RED, 'Stopping Server', Style.RESET_ALL)
