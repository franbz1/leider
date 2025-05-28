| Identificador               | HU0010                                                    |
|-----------------------------|-----------------------------------------------------------|
| **Título**                  | Inicio de sesión                                           |
| **Narrativa**               | Como usuario (paciente, recepción, doctor o administrador) deseo iniciar sesión con mi correo y contraseña para acceder a mis funcionalidades. |
| **Criterios de aceptación** | <ol><li>El usuario ingresa correo electrónico y contraseña en el formulario de inicio de sesión.</li><li>El sistema valida las credenciales contra la base de datos de Django.</li><li>Si las credenciales son válidas, se crea la sesión de usuario y se redirige a la página de inicio según el rol.</li><li>Si las credenciales son inválidas, se muestra un mensaje de error “Correo o contraseña incorrectos”.</li><li>El formulario incluye protección CSRF y límite de intentos para evitar ataques de fuerza bruta.</li></ol> |


| Identificador               | HU0009                                                    |
|-----------------------------|-----------------------------------------------------------|
| **Título**                  | Registro de cuenta de paciente                              |
| **Narrativa**               | Como paciente deseo crear una cuenta con mi nombre, correo y contraseña para poder agendar citas y recibir recordatorios. |
| **Criterios de aceptación** | <ol><li>El paciente debe ingresar nombre completo, correo electrónico y contraseña.</li><li>La contraseña debe cumplir con criterios de longitud y complejidad (mínimo 8 caracteres, incluir letra y número).</li><li>El sistema verifica que el correo no esté registrado previamente.</li><li>Al registrarse correctamente, se envía un correo de verificación y la cuenta queda activa tras confirmar el enlace.</li><li>Si hay campos inválidos o correo duplicado, el sistema muestra mensajes de error adecuados.</li></ol> |