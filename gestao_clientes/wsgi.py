"""
WSGI config for gestao_clientes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Inderido na Secao 5, video 29 - 10:55
from dj_static import Cling


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gestao_clientes.settings")

# Comentado na Secao 5, video 29 -  11:20
# application = get_wsgi_application()
application = Cling(get_wsgi_application())
