<p align="center">INFORMACIÓN</p>

ESP:


Imagina que estás trabajando en el desarrollo de un sistema para una aplicación de gestión de documentos en un entorno empresarial. Deseas implementar un decorador llamado verificar_acceso_entorno que permita controlar el acceso a funciones según el entorno de ejecución.

El decorador realiza las siguientes acciones:

Antes de ejecutar la función, verificar si el entorno de ejecución es "producción".

Si el entorno es "producción", permitir la ejecución de la función y mostrar un mensaje indicando que el acceso fue permitido en el entorno de producción.

Si el entorno no es "producción", evitar la ejecución de la función y mostrar un mensaje indicando que el acceso está restringido a entornos de producción.

Luego, aplica este decorador a dos funciones, subir_documento y eliminar_documento. Intenta ejecutar estas funciones con diferentes entornos y observa el comportamiento del decorador.



---

ENG:

Imagine you are working on developing a system for a document management application in a business environment. You want to implement a decorator called check_environment_access that controls access to functions based on the execution environment.

The decorator performs the following actions:

Before executing the function, it checks if the execution environment is "production".

If the environment is "production", it allows the function to execute and shows a message indicating that access was granted in the production environment.

If the environment is not "production", it prevents the function from executing and shows a message indicating that access is restricted to production environments.

Then, apply this decorator to two functions, upload_document and delete_document. Try executing these functions with different environments and observe the behavior of the decorator.

