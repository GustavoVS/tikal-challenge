# Routers to external app classes


class RecortesRouter:
    """
    A router to control all database operations on models in
    this app
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'recortes':
            return 'recortes_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'recortes':
            return 'recortes_db'
        return None
