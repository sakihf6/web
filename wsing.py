import sys
import os

# Agregar el directorio de tu proyecto al path
path = '/home/tu-usuario/tu-proyecto'
if path not in sys.path:
    sys.path.append(path)

from app import app as application

# Configuración de variables de entorno para producción
os.environ['FLASK_ENV'] = 'production'
os.environ['SECRET_KEY'] = 'tu-clave-secreta'