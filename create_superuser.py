import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto_illis.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "iker")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "avilesiker71@gmail.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "12345678")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"✅ Superusuario '{username}' creado correctamente.")
else:
    print(f"⚠️ El superusuario '{username}' ya existe.")

print("Usuarios existentes:", list(User.objects.values_list("username", flat=True)))