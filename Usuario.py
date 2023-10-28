# Clase Usuario
class Usuario:
    def _init_(self, nombre, email, password, tipo_usuario):
        self.nombre = nombre
        self.email = email
        self.__password = password  # Encapsulación
        self.tipo_usuario = tipo_usuario

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def login(self, input_password):
        return self.__password == input_password


class Administrador(Usuario):
    def _init_(self, nombre, email, password):
        super()._init_(nombre, email, password, "Administrador")

    def _str_(self):
        return f"Administrador: {self.__nombre}"


class Empleado(Usuario):
    def _init_(self, nombre, email, password):
        super()._init_(nombre, email, password, "Empleado")


class Aplicacion:
    def _init_(self):
        self.usuarios = []

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

    def menu(self):
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("3. Salir")

    def iniciar_sesion(self):
        email = input("Email: ")
        password = input("Contraseña: ")

        usuario = self.buscar_usuario(email)
        if usuario is not None and usuario.login(password):
            print(f"Bienvenido, {usuario.nombre}! Tipo de usuario: {usuario.tipo_usuario}")
            return usuario
        else:
            print("Inicio de sesión fallido. El usuario no está registrado. Por favor, regístrese.")
            return None

    def registrar_nuevo_usuario(self):
        nombre = input("Nombre: ")
        email = input("Email: ")
        password = input("Contraseña: ")
        tipo_usuario = input("Tipo de usuario (Administrador/Empleado): ").capitalize()
        if tipo_usuario not in ["Administrador", "Empleado"]:
            print("Tipo de usuario inválido.")
            return None
        if self.buscar_usuario(email) is not None:
            print("El usuario ya está registrado.")
            return None

        if tipo_usuario == "Administrador":
            usuario = Administrador(nombre, email, password)
        else:
            usuario = Empleado(nombre, email, password)
        self.registrar_usuario(usuario)
        print(f"{tipo_usuario} registrado exitosamente.")
        return usuario

    def mostrar_usuarios_registrados(self):
        print("Usuarios Registrados:")
        for usuario in self.usuarios:
            print(f"Nombre: {usuario.nombre}, Tipo de usuario: {usuario.tipo_usuario}")

    def menu_administrador(self, usuario):
        while True:
            print("Menú de Administrador:")
            print("1. Ver usuarios registrados")
            print("2. Cerrar sesión")
            opcion_admin = input("Seleccione una opción (Admin): ")
            if opcion_admin == "1":
                self.mostrar_usuarios_registrados()
            elif opcion_admin == "2":
                return None


if __name__ == "_main_":
    app = Aplicacion()
    usuario_actual = None

    while True:
        if usuario_actual is None:
            app.menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                usuario_actual = app.iniciar_sesion()
            elif opcion == "2":
                usuario_actual = app.registrar_nuevo_usuario()
            elif opcion == "3":
                break

        elif isinstance(usuario_actual, Administrador):
            usuario_actual = app.menu_administrador(usuario_actual)

            if usuario_actual is None:
                usuario_actual = None
        else:
            print("No tienes permiso de administrador")
            usuario_actual
