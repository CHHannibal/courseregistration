import os
import sys
from django.core.wsgi import get_wsgi_application

# Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
#sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), '..'))
#sys.path.append('/var/www/html/ffcs/')
#sys.path.append('/var/www/html/ffcs/ffcs')

os.environ['DJANGO_SETTINGS_MODULE'] = 'courseregistration.settings'

sys.stdout = sys.stderr

DEBUG = True

application = get_wsgi_application()
