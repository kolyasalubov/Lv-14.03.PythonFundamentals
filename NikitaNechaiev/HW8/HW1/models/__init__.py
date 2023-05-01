# Файл __init__.py для пакету user
from .user import create_user
# Файл __init__.py для пакету admin
from .admin import create_admin
__all__ = ['create_admin','create_user']

