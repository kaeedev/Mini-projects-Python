<p align="center">INFORMACIÓN</p>

ESP:



Sistema de autenticación para una aplicación web que implementa un sistema de inicio de sesión que verifica si las credenciales proporcionadas por el usuario son válidas antes de permitir el acceso a ciertas funciones. Además, una vez que el usuario haya iniciado sesión correctamente, se le proporciona información personal.

El programa realiza lo siguiente:

Un registro de usuarios que contenga información adicional, como el nombre completo y el correo electrónico.

Un decorador llamado verificar_inicio_sesion que acepta el nombre de usuario y la contraseña como argumentos. Este decorador verificará si las credenciales proporcionadas son válidas comparándolas con el registro de usuarios. Si las credenciales son válidas, la función decorada se ejecutará y se le pasará como argumento la información personal del usuario.

Una función llamada informacion_usuario que imprime la información personal del usuario después de que haya iniciado sesión correctamente.




---

ENG:

Authentication System for a Web Application

The system implements a login system that verifies if the credentials provided by the user are valid before granting access to certain functions. Additionally, once the user has logged in successfully, personal information is provided.

The program performs the following tasks:

User Registration: Contains additional information, such as full name and email address.

Decorator Named check_login: This decorator accepts the username and password as arguments. It will check if the provided credentials are valid by comparing them with the user registration records. If the credentials are valid, the decorated function will execute and the user's personal information will be passed as an argument.

Function Named user_info: Prints the user's personal information after they have logged in successfully.

