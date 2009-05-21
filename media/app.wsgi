import os, sys
# Use packages?  Anyhoo, altering path at runtime...
sys.path.append('/path/to/projects/')
sys.path.append('/path/to/projects/thisProjectDir/')
# might have to be app.settings, nope
os.environ['DJANGO_SETTINGS_MODULE'] = 'thisProjectDir.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
