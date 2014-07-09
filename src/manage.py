#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    # From <app>/bin to <app>/src
    # This should be used only by elastic-beanstalk, 
    # Why manage.py requires?
    # If you need to run syncdb or any other management commands
    # on the servers and you are using elasticbeanstalk
    # then we need manage.py
    
    PROJECT_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
    sys.path.append(PROJECT_DIR)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assignment6.settings")
  
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
