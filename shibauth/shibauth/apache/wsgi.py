
import os, sys
#
 # Calculate the path based on the location of the WSGI script.
apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)

# # Add the path to 3rd party django application and to django itself.
sys.path.append('/home/ubuntu/pathf-shib-auth/shibauth')
os.environ['DJANGO_SETTINGS_MODULE'] = 'shibauth.apache.override'

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shibauth.apache.override")

application = get_wsgi_application()
