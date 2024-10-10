from django.apps import AppConfig

class UsersConfig(AppConfig):
    """
    Configuration for the 'users' app.

    This class is responsible for configuring the 'users' application
    and its settings within the Django project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
