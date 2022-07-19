from rolepermissions.roles import AbstractUserRole

class Docente(AbstractUserRole):
    available_permissions = {'cadastrar_lab': True,'ver_lab': True}

class Discente(AbstractUserRole):
    available_permissions = {'ver_lab': True}