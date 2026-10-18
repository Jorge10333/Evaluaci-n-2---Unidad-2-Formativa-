from models.administrador import Administrador

admin = Administrador(1, "jlagos", "1234", "admin",
                      "Jorge", "Santiago", "123456789", "j@mail.com",
                      "2026-10-17", 1000000, 101)

admin.imprimir_Empleado()
print(admin.autenticar("1234"))
print(admin.verificarPermiso("cualquiera"))
print(admin.registrarHoras("2026-10-17", 8, "Prueba"))