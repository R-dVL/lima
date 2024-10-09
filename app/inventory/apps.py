from django.apps import AppConfig

class InventoryConfig(AppConfig):
    """
    Configuration for the 'inventory' app in Django.

    This class inherits from AppConfig and defines the default settings
    for the 'inventory' application. Django uses this class to initialize
    the app and set some key properties.

    Attributes:
        default_auto_field (str): Specifies the default field type for
                                  primary keys in this application's models.
        name (str): The name of the application, used in the code and configuration.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'
