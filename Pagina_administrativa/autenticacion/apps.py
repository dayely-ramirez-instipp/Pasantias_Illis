from django.apps import AppConfig
class AutenticacionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Pagina_administrativa.autenticacion'

    def ready(self):
        import Pagina_administrativa.autenticacion.signals