def verificar_acceso_entorno(funcion):
  def wrapper(*args, **kwargs):
    entorno = obtener_entorno()
    if entorno == 'produccion':
      print("Acceso permitido en el entorno de produccion")
      return (funcion(*args,*kwargs))
    else:
      print("Acceso restringido a entornos de desarrollo")
  return wrapper

@verificar_acceso_entorno
def subir_documento(documento):
  print(f"Subiendo documento: {documento}")

@verificar_acceso_entorno
def eliminar_documento(documento):
  print(f"Eliminando documento: {documento}")

#///////////Entorno de produccion
print("/////////////Entorno de produccion")
def obtener_entorno():
  return "produccion"
subir_documento('Documento A')
eliminar_documento('Documento B')

#///////////Entorno de desarrollo
print("/////////////Entorno de desarrollo")
def obtener_entorno():  # noqa: F811
  return "desarrollo"
subir_documento('Documento A')
eliminar_documento('Documento B')
