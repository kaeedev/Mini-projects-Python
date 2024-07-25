usuarios_registrados = {
    "usuario1": {"contrasena": "contrasena123", "nombre_completo": "Juan Pérez", "correo_electronico": "juan@example.com"},
    "usuario2": {"contrasena": "password456", "nombre_completo": "María Gómez", "correo_electronico": "maria@example.com"},
    "usuario3": {"contrasena": "qwerty789", "nombre_completo": "Carlos Rodríguez", "correo_electronico": "carlos@example.com"}
}


def verificar_inicio_sesion(funcion):
  def wrapper(nombre_usuario,contrasena):
    if nombre_usuario in usuarios_registrados and usuarios_registrados[nombre_usuario]['contrasena']==contrasena:
      print(f" Inicio de sesion exitoso para el usuario {nombre_usuario}")
      usuario_info=usuarios_registrados[nombre_usuario]
      return(funcion(usuario_info))
    else:
      print("Inicio de sesion fallido, Verifica tu nombre de usuario y contrasena")
  return wrapper


@verificar_inicio_sesion
def informacion_usuario(usuario_info):
  print("Informacion personal del usuario:")
  print("Nombre completo: ",usuario_info["nombre_completo"])
  print("Correo electronico: ",usuario_info["correo_electronico"])

#Usos
informacion_usuario('usuario1','contrasena123')
informacion_usuario('usuario2','password456')
