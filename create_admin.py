import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto_illis.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Datos del admin (usa variables de entorno por seguridad)
username = os.getenv('ADMIN_USERNAME', 'admin')
email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
password = os.getenv('ADMIN_PASSWORD', '12345678')

if not User.objects.filter(username=username).exists():
    print(f"Creando superusuario: {username}...")
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superusuario creado con éxito.")
else:
    print(f"El usuario {username} ya existe.")