# Safe Legacy

## Herencia Digital Segura

Aplicación web desarrollada con **Django REST Framework** como Trabajo Práctico. El proyecto propone una plataforma para gestionar una **herencia digital**, permitiendo que una persona pueda registrar, organizar y asignar bienes digitales a diferentes herederos para que sean entregados automáticamente bajo determinadas condiciones.

---

## 📌 Descripción del proyecto

**Safe Legacy** es una aplicación de herencia digital en la que un usuario principal, denominado **Main**, puede preparar su patrimonio digital para que, en caso de dejar de reportar actividad durante un período determinado, los bienes previamente asignados sean transferidos a sus herederos.

El sistema busca representar de manera simulada qué ocurriría con los bienes digitales de una persona cuando esta ya no puede administrarlos.

El usuario **Main** podrá:

- Registrar herederos.
- Administrar un saldo de dinero virtual.
- Distribuir dinero entre sus herederos.
- Subir y almacenar archivos.
- Registrar imágenes y documentos.
- Guardar credenciales y contraseñas.
- Registrar otros bienes de valor digital.
- Simular la herencia de una cuenta de Bitcoin.
- Definir qué heredero recibirá cada bien.
- Establecer un período máximo de días sin reportar actividad.
- Confirmar periódicamente que continúa con vida y utilizando la plataforma.

Mientras el usuario Main continúe reportando actividad, la herencia permanecerá **bloqueada**.

Si el período establecido finaliza sin que el usuario confirme su actividad, el sistema activará el proceso de herencia y los bienes serán entregados a los herederos según la distribución previamente configurada.

---

## 🎯 Objetivos

### Objetivo general

Desarrollar una API REST utilizando **Django REST Framework** que permita gestionar de forma simulada una plataforma de herencia digital, aplicando conceptos de autenticación, autorización, relaciones entre modelos, almacenamiento de información y lógica de negocio.

### Objetivos específicos

- Implementar un sistema de usuarios y autenticación.
- Diferenciar al usuario principal de sus herederos.
- Permitir registrar y administrar herederos.
- Gestionar bienes digitales pertenecientes al usuario Main.
- Permitir asignar bienes a diferentes herederos.
- Implementar un sistema de dinero virtual.
- Simular la transferencia de criptomonedas.
- Implementar un mecanismo de comprobación periódica de actividad.
- Detectar cuándo el usuario Main deja de reportar actividad.
- Activar automáticamente la herencia cuando se cumplan las condiciones.
- Aplicar permisos para proteger la información privada.
- Exponer la funcionalidad mediante una API REST.
- Documentar y probar los endpoints de la aplicación.

---

## 👤 Roles del sistema

### Main

Es el usuario que posee los bienes digitales y configura su herencia.

Puede:

- Administrar su perfil.
- Agregar y eliminar herederos.
- Crear bienes digitales.
- Asignar bienes a herederos.
- Administrar su dinero virtual.
- Establecer el período de comprobación.
- Reportar que continúa activo.
- Consultar el estado de su herencia.

### Heredero

Es un usuario que fue designado por un Main para recibir determinados bienes.

Puede:

- Consultar las herencias que tiene asignadas.
- Acceder a los bienes que le fueron transferidos.
- Recibir dinero virtual.
- Recibir archivos y otros bienes digitales.
- Recibir activos digitales simulados.

Los bienes permanecen ocultos o bloqueados para el heredero hasta que la herencia sea activada.

---

## 💰 Bienes digitales

La aplicación permitirá manejar diferentes tipos de bienes.

Algunos ejemplos son:

| Tipo         | Ejemplo                  |
| ------------ | ------------------------ |
| Dinero       | $50.000 de saldo virtual |
| Archivo      | Documento PDF            |
| Imagen       | Fotografía               |
| Contraseña   | Credencial de una cuenta |
| Documento    | Documento personal       |
| Criptomoneda | 0.05 BTC                 |
| Otro         | Cualquier activo digital |

Cada bien podrá tener información como:

- Nombre.
- Descripción.
- Tipo.
- Valor.
- Propietario.
- Heredero asignado.
- Fecha de creación.
- Estado.
- Fecha de transferencia.

---

## ₿ Criptomonedas

Como parte del alcance académico, se podrá simular la existencia de criptomonedas.

Por ejemplo:

```text
Activo: Bitcoin
Cantidad: 0.05 BTC
Propietario: Usuario Main
Heredero: Juan Pérez
Estado: Bloqueado
```

No se realizará una transferencia real en la blockchain.

La aplicación solamente representará el activo y su posterior transferencia dentro del sistema.

---

## ⏱️ Sistema de comprobación de vida

Una de las funcionalidades principales será el sistema de **Check-in**.

El usuario Main deberá reportar periódicamente que continúa activo.

Por ejemplo:

```text
Período configurado: 30 días

Último check-in:
25/08/2026

Próximo vencimiento:
24/09/2026
```

Cada vez que el usuario presione el botón **"Estoy activo"**, se actualizará la fecha de su último reporte.

Mientras el usuario realice el check-in dentro del período establecido, la herencia continuará bloqueada.

### Activación de la herencia

Si el usuario no realiza el check-in y supera el período configurado:

```text
Último check-in: 25/08/2026
Período: 30 días
Fecha límite: 24/09/2026

Estado → HERENCIA ACTIVADA
```

El sistema deberá procesar la distribución de los bienes según las asignaciones previamente realizadas.

---

## 🔐 Seguridad

Debido a que el sistema manejará información potencialmente sensible, la seguridad será una parte importante del proyecto.

Se deberán implementar mecanismos como:

- Autenticación de usuarios.
- Autorización mediante permisos.
- Protección de endpoints.
- Separación de información entre usuarios.
- Validación de datos.
- Contraseñas almacenadas mediante mecanismos seguros.
- Protección de archivos.
- Restricción de acceso a bienes heredados.
- Control de acceso según el estado de la herencia.

> **Nota:** En una aplicación real, almacenar contraseñas, claves privadas de criptomonedas u otros secretos requeriría medidas de seguridad mucho más avanzadas. Para este Trabajo Práctico se trabajará con información simulada y se priorizará la demostración de la arquitectura y la lógica de negocio.

---

## 🏗️ Tecnologías

### Backend

- **Python**
- **Django**
- **Django REST Framework**

### Base de datos

Se podrá utilizar:

- MySQL / MariaDB
- SQLite para desarrollo y pruebas

### Herramientas complementarias

- Git
- GitHub
- Postman
- Docker _(opcional)_
- Swagger / OpenAPI _(opcional)_

---

## 🧩 Arquitectura propuesta

La aplicación estará desarrollada siguiendo una arquitectura basada en Django y Django REST Framework.

```text
Cliente
   │
   ▼
API REST
   │
   ▼
Django REST Framework
   │
   ├── Autenticación
   ├── Usuarios
   ├── Herederos
   ├── Bienes
   ├── Herencias
   ├── Dinero virtual
   └── Check-in
   │
   ▼
Base de datos
```

---

## 🗄️ Modelos principales

Una posible estructura inicial de modelos sería:

### User

Representa a los usuarios de la aplicación.

```text
User
├── id
├── username
├── email
├── password
├── first_name
├── last_name
└── role
```

El campo `role` podría diferenciar entre:

```text
MAIN
HEREDERO
```

---

### Heredero

Representa la relación entre un Main y una persona designada como heredero.

```text
Heredero
├── id
├── main
├── usuario
├── nombre
├── porcentaje
└── fecha_creacion
```

Un Main podrá tener múltiples herederos.

---

### Bien

Representa cualquier activo digital que pueda formar parte de la herencia.

```text
Bien
├── id
├── propietario
├── nombre
├── descripcion
├── tipo
├── valor
├── archivo
├── estado
└── fecha_creacion
```

Ejemplos de `tipo`:

```text
DINERO
ARCHIVO
IMAGEN
CONTRASEÑA
DOCUMENTO
BITCOIN
OTRO
```

---

### Asignación

Permite determinar qué heredero recibe cada bien.

```text
Asignacion
├── id
├── bien
├── heredero
├── porcentaje
└── fecha_asignacion
```

Esto permite representar situaciones como:

```text
Bitcoin → Heredero A → 50%
Bitcoin → Heredero B → 50%
```

o:

```text
Archivo "Fotos Familiares"
        ↓
Heredero A → 100%
```

---

### Billetera

Representa el dinero virtual disponible del usuario.

```text
Billetera
├── id
├── usuario
└── saldo
```

El dinero podrá utilizarse como otro tipo de bien heredable.

---

### Transacción

Registra los movimientos de dinero dentro de la aplicación.

```text
Transaccion
├── id
├── origen
├── destino
├── monto
├── tipo
└── fecha
```

---

### CheckIn

Registra la actividad del usuario Main.

```text
CheckIn
├── id
├── usuario
├── ultima_confirmacion
├── periodo_dias
├── fecha_vencimiento
└── estado
```

Estados posibles:

```text
ACTIVO
ADVERTENCIA
VENCIDO
HERENCIA_ACTIVADA
```

---

### Herencia

Representa el proceso de activación y transferencia.

```text
Herencia
├── id
├── main
├── fecha_activacion
├── estado
└── fecha_finalizacion
```

Estados posibles:

```text
PENDIENTE
ACTIVA
PROCESADA
```

---

## 🔄 Flujo principal de la aplicación

```text
                 ┌─────────────────────┐
                 │   Usuario se registra│
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Se convierte en   │
                 │        MAIN         │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Agrega herederos    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Registra sus bienes │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Asigna bienes a los │
                 │      herederos      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Configura período   │
                 │     de check-in     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Realiza Check-in │◄──────┐
                 └──────────┬──────────┘       │
                            │                  │
                     ¿Venció el período?       │
                       │             │         │
                      NO            SÍ         │
                       │             │         │
                       └─────────────┘         │
                             │                 │
                             ▼                 │
                    ┌────────────────┐         │
                    │ Activar herencia│         │
                    └───────┬────────┘         │
                            │                  │
                            ▼                  │
                    ┌────────────────┐         │
                    │ Transferir los │         │
                    │     bienes     │         │
                    └───────┬────────┘         │
                            │                  │
                            ▼                  │
                    ┌────────────────┐         │
                    │    Herederos   │         │
                    │ reciben bienes │         │
                    └────────────────┘         │
                                              │
                                              └── Check-in
```

---

## 🌐 API REST

Algunos endpoints posibles:

### Autenticación

```http
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/logout/
```

### Usuarios

```http
GET    /api/users/me/
PUT    /api/users/me/
```

### Herederos

```http
GET    /api/herederos/
POST   /api/herederos/
GET    /api/herederos/{id}/
PUT    /api/herederos/{id}/
DELETE /api/herederos/{id}/
```

### Bienes

```http
GET    /api/bienes/
POST   /api/bienes/
GET    /api/bienes/{id}/
PUT    /api/bienes/{id}/
DELETE /api/bienes/{id}/
```

### Asignaciones

```http
GET    /api/asignaciones/
POST   /api/asignaciones/
PUT    /api/asignaciones/{id}/
DELETE /api/asignaciones/{id}/
```

### Check-in

```http
GET  /api/checkin/
POST /api/checkin/
```

### Herencia

```http
GET /api/herencia/
POST /api/herencia/procesar/
```

### Billetera

```http
GET  /api/wallet/
POST /api/wallet/depositar/
POST /api/wallet/transferir/
```

---

## 🧪 Ejemplo de uso

Un usuario llamado **Carlos** crea una cuenta y configura su herencia.

### 1. Agrega herederos

```text
Ana
Juan
```

### 2. Registra sus bienes

```text
$100.000 de dinero virtual
Notebook
Fotos familiares
Contraseña de una cuenta
0.05 BTC
```

### 3. Distribuye los bienes

```text
$100.000
├── Ana → $60.000
└── Juan → $40.000

Notebook
└── Juan → 100%

Fotos familiares
└── Ana → 100%

0.05 BTC
├── Ana → 50%
└── Juan → 50%
```

### 4. Configura el check-in

```text
Período: 30 días
```

Carlos deberá ingresar periódicamente y confirmar:

> "Estoy activo"

### 5. Carlos deja de realizar check-in

Una vez superados los 30 días, el sistema detecta el vencimiento.

### 6. Se activa la herencia

El sistema procesa automáticamente las asignaciones:

```text
Ana
├── $60.000
├── Fotos familiares
└── 0.025 BTC

Juan
├── $40.000
├── Notebook
└── 0.025 BTC
```

---

## 📋 Alcance del Trabajo Práctico

El proyecto tendrá como objetivo demostrar conocimientos de:

- Django.
- Django REST Framework.
- Modelado de bases de datos.
- Relaciones entre modelos.
- CRUD.
- APIs REST.
- Serializers.
- Views / ViewSets.
- Routers.
- Autenticación.
- Permisos.
- Validaciones.
- Manejo de archivos.
- Lógica de negocio.
- Manejo de estados.
- Pruebas de API.

El sistema será una **simulación académica** y no realizará transferencias monetarias reales ni operaciones reales de criptomonedas.

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/usuario/safe-legacy.git
cd safe-legacy
```

### 2. Crear entorno virtual

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear un archivo `.env`:

```env
SECRET_KEY=tu_secret_key
DEBUG=True

DB_NAME=safe_legacy
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
```

### 5. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario

```bash
python manage.py createsuperuser
```

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

La API estará disponible en:

```text
http://127.0.0.1:8000/
```

---

## 📁 Estructura propuesta

```text
safe-legacy/
│
├── manage.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── permissions.py
│
├── inheritance/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── services.py
│
├── assets/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── wallet/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
└── media/
    └── ...
```

---

## 🔮 Posibles mejoras futuras

Si el proyecto continúa desarrollándose, podrían incorporarse:

- Notificaciones por correo electrónico.
- Avisos antes del vencimiento del check-in.
- Autenticación mediante JWT.
- Autenticación de dos factores (2FA).
- Cifrado adicional de bienes sensibles.
- Sistema de contactos de confianza.
- Historial completo de movimientos.
- Registro de auditoría.
- Panel administrativo.
- Frontend independiente con React.
- Integración con una blockchain de prueba.
- Sistema de testamento digital con múltiples niveles de autorización.
- Recuperación ante intentos de acceso no autorizados.

---

## 👨‍💻 Estado del proyecto

**Estado:** 🚧 En desarrollo

**Tipo:** Trabajo Práctico

**Backend:** Django + Django REST Framework

**Base de datos:** MySQL / MariaDB

**Objetivo:** Desarrollo de una API REST para la gestión simulada de herencia digital.

---

## 📄 Licencia

Proyecto desarrollado con fines **educativos y académicos**. No debe utilizarse para gestionar dinero real, credenciales reales, claves privadas de criptomonedas ni otros datos sensibles sin implementar previamente mecanismos de seguridad adecuados.
