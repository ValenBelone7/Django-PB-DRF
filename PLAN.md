# Plan de trabajo — Entrega 3 (ViewSets, Routers, Permisos, JWT)

**Consigna:**

> - ViewSets en reemplazo a las vistas Concrete Generics (al menos 1 `ModelViewSet` y 1
>   `ReadOnlyModelViewSet`).
> - Enrutamiento en `routers.py` para los viewsets.
> - Implementación de seguridad con `permission_classes` en los viewsets.
> - Autenticación con `restframework-simplejwt` (y opcional, SessionAuth de DRF).

Además: **una sola forma de escribir vistas en todo el proyecto.** Se elimina `@api_view` (usado
hoy en `herederos`) y las Concrete Generic APIView (usadas hoy en `bienes`). Todo queda como
ViewSets.

**Material de referencia:**

1. **Repo del profe (`drf-2026`), commit `143d5a9 clase 16/09 viewsets`**: su código real con
   ViewSets + router + JWT. Es la referencia principal para la estructura.
2. **`viewsets.md`** que pasó el profe en la última clase (ViewSets, `DefaultRouter`, `@action`).
   Referencia conceptual; donde difiere del código del profe, seguimos el código.

Lo que tomamos del commit del profe:

- `ModelViewSet` con `queryset` + `get_serializer_class()` (o `serializer_class`) +
  `permission_classes`, sin métodos propios salvo que haga falta.
- `get_serializer_class()` mira **`self.request.method == "GET"`**, igual que en su
  `ArticuloViewSet` (no `self.action`, que es lo que sugiere el `.md`).
- **Un solo router para todo el proyecto**, en un `routers.py` dentro del paquete de settings
  (él lo tiene en `src/settings/routers.py`, nosotros en `src/nucleo/routers.py`), y el `urls.py`
  raíz lo incluye con `path("api/", include(router.urls))`. Los `urls.py` de las apps dejan de
  usarse.
- `@action` para endpoints fuera del CRUD (él hizo `borrado_logico` en `ProveedorViewSet`). Para
  nosotros es **opcional** (ver 5.5).
- JWT: `settings.py` y rutas de token calcadas del commit `868d520 9/9 auth & jwt` (no cambiaron
  en el commit de viewsets).

**Entrega anterior (Entrega 2):** ya mergeada a `main` (fases 0 a 3, PRs #1 a #6). No se repite
acá — lo que hace falta de esa entrega ya está en el código y en el README.

## Estado y responsables

| Fase | Estado | Responsable |
|---|---|---|
| 4 — ViewSets de `users` | ✅ **Hecha** (rama `fase-4/viewsets-users`) | Valen |
| 5 — ViewSets de `bienes` | ✅ **Hecha** (rama `fase-5/viewsets-bienes`) | Valen |
| 6 — JWT | Pendiente | Tiago |
| 7 — Pruebas, README y merge | Pendiente | Tiago |

**Tiago:** arrancá desde `develop` actualizado, **con las Fases 4 y 5 ya mergeadas**
(`git checkout develop && git pull`). Los 4 ViewSets ya existen, `src/nucleo/routers.py` ya
tiene los 4 registrados y `nucleo/urls.py` ya incluye `router.urls` (los `urls.py` de las apps
ya no existen). Te quedan la Fase 6 (JWT) y después la Fase 7 (pruebas, README y merge).
Antes de JWT, pegarle a la API sin autenticarse da **403**; después de tu Fase 6 tiene que
dar **401**.

**Rama base:** `develop`. Los nombres de rama siguen la numeración que ya veníamos usando
(`fase-0` a `fase-3` en la Entrega 2), así que esta entrega arranca en `fase-4`.

---

## Decisiones tomadas antes de arrancar

| Tema | Decisión |
|---|---|
| `ReadOnlyModelViewSet` | **`UserViewSet`** (nuevo). Tiene sentido de negocio real: los usuarios no se crean ni se editan por esta API (eso es admin, o a futuro `/api/auth/register/`), solo se consultan para ver quién es el `propietario` de un bien o el `usuario` de un heredero. `list` + `retrieve` nada más. (El profe no tiene `ReadOnlyModelViewSet` en su código, solo en el `.md`; la consigna lo pide.) |
| `ModelViewSet` (CRUD completo) | `HerederoViewSet`, `BienViewSet`, `AsignacionViewSet`. Los tres necesitan alta/baja/modificación real por API. |
| `get_serializer_class()` | **Como el profe:** `if self.request.method == "GET"` → `*PublicSerializer`, si no → serializer plano. En un ViewSet eso cubre `list` y `retrieve` (los dos son `GET`) y también cualquier `@action` con `GET`. |
| Router | **Uno solo, en `src/nucleo/routers.py`**, como el `settings/routers.py` del profe. Además de copiar su estructura, evita un problema real: dos `DefaultRouter` incluidos en `api/` generan dos vistas raíz `api-root` y la segunda queda tapada (el índice navegable de `/api/` mostraría solo la mitad de los recursos). |
| `permission_classes` | **Solo clases built-in de DRF**, igual que el profe (nada de permisos custom todavía). Él usa `IsAuthenticatedOrReadOnly` en `Articulo` (catálogo público) e `IsAuthenticated` en `Proveedor`. Acá todo es información privada de herencia (bienes, quién hereda qué), así que usamos **`IsAuthenticated`** en los 4 ViewSets — ni el `GET` queda abierto a anónimos. |
| Autenticación | JWT con `djangorestframework-simplejwt`, settings calcados de los del profe (`SIMPLE_JWT`, `DEFAULT_AUTHENTICATION_CLASSES`), + `SessionAuthentication` de DRF como opcional (la consigna lo pide opcional, el profe la deja puesta igual, la dejamos). Sin endpoint de registro — los usuarios se siguen creando por `/admin/` o `createsuperuser`, como hace el profe. |
| Código viejo (`@api_view`, Concrete Generic) | **Se borra, no se comenta.** El profe en su commit lo dejó comentado (tiene sentido en un repo de clase), pero acá el objetivo explícito es que quede una sola forma de escribir vistas en todo el proyecto. Lo mismo para `users/urls.py` y `bienes/urls.py`: el profe dejó `productos/urls.py` comentado, nosotros los borramos. |
| `permissions.py` | Se agrega un `bienes/permissions.py` con una clase custom **comentada**, sin usar (igual que el placeholder que dejó el profe en su propio `productos/permissions.py`). Es más fácil activarla el día que la cátedra pida permisos a nivel de objeto (dueño del bien), y deja documentado que sabemos que existe esa opción sin meternos en el alcance de esta entrega. |
| Estructura de las rutas | El prefijo de cada recurso no cambia (`bienes/`, `asignaciones/`, `herederos/`) porque el router lo genera igual que antes. Se suma `usuarios/` nuevo. El `basename` de cada uno es singular (`bien`, `asignacion`, `heredero`, `usuario`), como en el ejemplo del `.md` (`basename='articulo'`). El profe en su código usó `"articulos_vs"`; es solo un nombre, nos quedamos con el singular. |
| `@action` | **Opcional**, no lo pide la consigna. Si sobra tiempo, `GET /api/bienes/mios/` (ver 5.5). |

---

## Convenciones de código (siguen valiendo, Entrega 2 + código del profe)

- Comillas dobles en strings nuevos.
- `# noqa: RUF012` en atributos de clase mutables (el profe lo sacó de `permission_classes`,
  nosotros lo mantenemos porque ruff lo marca igual).
- FK con `related_name` (ya está en todos los modelos).
- Comentario en castellano arriba de cada ViewSet explicando qué es (`# ModelViewSet: CRUD completo`, `# ReadOnlyModelViewSet: solo lectura, sin alta/baja/modificación por API`), como el `# Concrete generic` que usaba el profe.
- `router.register()` con el mismo prefijo que ya usa cada recurso en las URLs actuales.
- JWT: variables de `SIMPLE_JWT` y `DEFAULT_AUTHENTICATION_CLASSES` calcadas del `settings.py` del profe.

---

## Contrato de nombres

**`src/users/views.py`**

| Clase | Tipo | Ruta (via router) |
|---|---|---|
| `UserViewSet` | `ReadOnlyModelViewSet` | `GET /api/usuarios/`, `GET /api/usuarios/<pk>/` |
| `HerederoViewSet` | `ModelViewSet` | `GET/POST /api/herederos/`, `GET/PUT/PATCH/DELETE /api/herederos/<pk>/` |

**`src/bienes/views.py`**

| Clase | Tipo | Ruta (via router) |
|---|---|---|
| `BienViewSet` | `ModelViewSet` | `GET/POST /api/bienes/`, `GET/PUT/PATCH/DELETE /api/bienes/<pk>/` |
| `AsignacionViewSet` | `ModelViewSet` | `GET/POST /api/asignaciones/`, `GET/PUT/PATCH/DELETE /api/asignaciones/<pk>/` |

**`src/nucleo/routers.py`** (estado final, después de Fases 4 y 5)

```python
from rest_framework.routers import DefaultRouter

from bienes.views import AsignacionViewSet, BienViewSet
from users.views import HerederoViewSet, UserViewSet

router = DefaultRouter()

router.register("usuarios", UserViewSet, basename="usuario")
router.register("herederos", HerederoViewSet, basename="heredero")
router.register("bienes", BienViewSet, basename="bien")
router.register("asignaciones", AsignacionViewSet, basename="asignacion")
```

**`src/nucleo/urls.py`** (estado final, después de Fases 4, 5 y 6)

```python
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .routers import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

> **Coordinación entre Fases 4, 5 y 6:** las tres tocan `nucleo/urls.py` y las dos primeras
> `nucleo/routers.py`. Como la Fase 4 ya está hecha y las 5 y 6 van en orden, cada fase agrega
> sus líneas sobre lo que dejó la anterior. Si igual aparece un conflicto en esas líneas, se
> resuelve **quedándose con las dos partes** hasta llegar al estado final de arriba.

---

# Fase 4 — ViewSets de `users`

**Rama:** `fase-4/viewsets-users`
**Responsable:** Valen
**Estado:** ✅ Hecha. Criterios verificados con el test client (con la salvedad del 401, que
llega con Fase 6: hoy sin sesión da 403). `manage.py check` y `ruff` limpios.

### 4.1 — Reescribir `src/users/views.py`

Borrar `herederos` y `heredero_detail` (las `@api_view`). Reemplazar por:

```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Heredero, User
from .serializers import HerederoPublicSerializer, HerederoSerializer, UserSerializer


# ReadOnlyModelViewSet: solo lectura, sin alta/baja/modificación por API
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # noqa: RUF012


# ModelViewSet: CRUD completo
class HerederoViewSet(viewsets.ModelViewSet):
    queryset = Heredero.objects.all().select_related("usuario")
    permission_classes = [IsAuthenticated]  # noqa: RUF012

    def get_serializer_class(self):
        if self.request.method == "GET":
            return HerederoPublicSerializer
        return HerederoSerializer
```

> `select_related("usuario")` es nuevo: antes no hacía falta (el `@api_view` no traía el usuario
> anidado), ahora con `HerederoPublicSerializer` en los `GET` sí, para no disparar una query
> extra por fila. `main` no se anida en el serializer, así que no hace falta traerlo.

### 4.2 — Crear `src/nucleo/routers.py` con los ViewSets de `users`

```python
from rest_framework.routers import DefaultRouter

from users.views import HerederoViewSet, UserViewSet

router = DefaultRouter()

router.register("usuarios", UserViewSet, basename="usuario")
router.register("herederos", HerederoViewSet, basename="heredero")
```

(Fase 5 suma las líneas de `bienes`, ver contrato de nombres.)

### 4.3 — `src/nucleo/urls.py`

Reemplazar `path("api/", include("users.urls"))` por el router. Mientras Fase 5 no esté
mergeada, `bienes.urls` sigue incluido:

```python
from .routers import router

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/", include("bienes.urls")),  # lo saca Fase 5
]
```

### 4.4 — Borrar `src/users/urls.py`

Ya no lo incluye nadie; las rutas las genera el router.

### ✅ Criterio de aceptación

- `uv run manage.py check` sin errores.
- `GET /api/` → índice navegable del router con `usuarios` y `herederos`.
- `GET /api/usuarios/` → 401 sin token, 200 con token (lista de usuarios, sin anidados raros).
- `POST /api/usuarios/` → 405 (el `ReadOnlyModelViewSet` no lo permite), incluso autenticado.
- `GET /api/herederos/` y `GET /api/herederos/<pk>/` → 200 con token, traen `usuario` anidado.
- `POST /api/herederos/` → 201 con token, `usuario` se manda como id.
- `PUT`/`DELETE /api/herederos/<pk>/` → funcionan con token.
- Todo lo anterior sin token → 401 (no 403 — con `JWTAuthentication` primera en la lista, DRF
  devuelve 401 con `WWW-Authenticate: Bearer`). Esto requiere Fase 6; antes de Fase 6 la
  autenticación por defecto de DRF devuelve 403.

---

# Fase 5 — ViewSets de `bienes`

**Rama:** `fase-5/viewsets-bienes`
**Responsable:** Valen
**Estado:** ✅ Hecha (rama `fase-5/viewsets-bienes`, sale de `fase-4/viewsets-users`). Las 8
operaciones verificadas con el test client; sin sesión da 403 hasta Fase 6. `manage.py check` y
`ruff` limpios en los archivos tocados. **No se hizo el opcional 5.5 (`@action`).**

### 5.1 — Reescribir `src/bienes/views.py`

Borrar las 4 Concrete Generic (`BienesListCreateAPIView`, `BienDetailAPIView`,
`AsignacionesListCreateAPIView`, `AsignacionDetailAPIView`). Reemplazar por:

```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Asignacion, Bien
from .serializers import (
    AsignacionPublicSerializer,
    AsignacionSerializer,
    BienPublicSerializer,
    BienSerializer,
)


# ModelViewSet: CRUD completo
class BienViewSet(viewsets.ModelViewSet):
    queryset = Bien.objects.all().select_related("propietario")
    permission_classes = [IsAuthenticated]  # noqa: RUF012

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BienPublicSerializer
        return BienSerializer


# ModelViewSet: CRUD completo
class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all().select_related(
        "bien", "heredero", "bien__propietario", "heredero__usuario"
    )
    permission_classes = [IsAuthenticated]  # noqa: RUF012

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AsignacionPublicSerializer
        return AsignacionSerializer
```

> `get_serializer_class` queda igual que en la Entrega 2 (`self.request.method == "GET"`), que es
> como lo sigue haciendo el profe en su `ArticuloViewSet`. La diferencia es que antes el detalle
> era otra vista (`RetrieveUpdateDestroyAPIView` con `serializer_class` plano); ahora es el mismo
> ViewSet, así que el `GET /<id>/` también pasa por `get_serializer_class` y devuelve el
> `*PublicSerializer`.

### 5.2 — Registrar en `src/nucleo/routers.py`

```python
from bienes.views import AsignacionViewSet, BienViewSet

router.register("bienes", BienViewSet, basename="bien")
router.register("asignaciones", AsignacionViewSet, basename="asignacion")
```

El import va arriba junto al de `users.views` y los dos `register` abajo de los de `usuarios`/
`herederos`. El archivo tiene que quedar igual al del contrato de nombres.

### 5.3 — `src/nucleo/urls.py`

Sacar la línea `path("api/", include("bienes.urls")),  # lo saca Fase 5`. El
`path("api/", include(router.urls))` ya está (lo dejó Fase 4).

### 5.4 — Borrar `src/bienes/urls.py`

Ya no lo incluye nadie.

### 5.5 — (Opcional) `@action` en `BienViewSet`

Solo si sobra tiempo, siguiendo el Paso 4 del `viewsets.md` y el `borrado_logico` del profe.
Un endpoint de colección (`detail=False`) que devuelve los bienes del usuario logueado:

```python
from rest_framework.decorators import action
from rest_framework.response import Response


class BienViewSet(viewsets.ModelViewSet):
    ...

    # detail=False: aplica a la colección → GET /api/bienes/mios/
    @action(detail=False, methods=["get"])
    def mios(self, request):
        bienes = self.get_queryset().filter(propietario=request.user)
        serializer = self.get_serializer(bienes, many=True)
        return Response(serializer.data)
```

Como es `GET`, `get_serializer_class` devuelve `BienPublicSerializer` sin tocar nada más.

### 5.6 — `src/bienes/permissions.py` (placeholder, sin usar)

```python
"""
from rest_framework import permissions


class EsPropietarioOSoloLectura(permissions.BasePermission):
    # Permiso a nivel de objeto: cualquier autenticado puede leer,
    # pero solo el propietario del bien puede editarlo o borrarlo.
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.propietario == request.user
"""
```

Igual que el `productos/permissions.py` del profe: queda documentado y listo para activar,
pero no se usa en esta entrega.

### ✅ Criterio de aceptación

Las 8 operaciones de siempre, ahora todas exigiendo token (401 sin token requiere Fase 6):

| Método | Ruta | Sin token | Con token |
|---|---|---|---|
| GET | `/api/bienes/` | 401 | 200, `propietario` anidado |
| POST | `/api/bienes/` | 401 | 201 |
| GET | `/api/bienes/<id>/` | 401 | 200, `propietario` anidado (ahora list y retrieve usan el mismo serializer público) |
| PUT | `/api/bienes/<id>/` | 401 | 200 |
| DELETE | `/api/bienes/<id>/` | 401 | 204 |
| GET | `/api/asignaciones/` | 401 | 200, `bien` y `heredero` anidados |
| POST | `/api/asignaciones/` | 401 | 201 |
| DELETE | `/api/asignaciones/<id>/` | 401 | 204 |

Si se hizo 5.5: `GET /api/bienes/mios/` → 401 sin token, 200 con token (solo los bienes del
usuario del token).

> Cambia el comportamiento del `GET /<id>/` respecto a la Entrega 2: antes usaba el serializer
> plano (propietario como id). Ahora el detalle también trae el anidado. Es más consistente y es
> el comportamiento estándar de un ViewSet — documentar el cambio en el README (Fase 7).

---

# Fase 6 — Autenticación JWT

**Rama:** `fase-6/auth-jwt`
**Responsable:** Tiago (es chica — solo toca `pyproject.toml`, `settings.py` y el `urls.py`
raíz).
**Depende de:** Fases 4 y 5 mergeadas a `develop`. En `nucleo/urls.py` solo se suman el import
y las dos rutas de token; el resto ya está en su estado final.

### 6.1 — Agregar la dependencia

```shell
uv add djangorestframework-simplejwt
```

(Mismo paquete y misma familia de versión que usa el profe: `>=5.5.1`.)

### 6.2 — `src/nucleo/settings.py`

Agregar, calcado del `settings.py` del profe:

```python
from datetime import timedelta
```

```python
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ]
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=2),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=10),
    "AUTH_HEADER_TYPES": ("Bearer",),
}
```

No se toca `DEFAULT_PERMISSION_CLASSES` a nivel global — igual que el profe, el permiso se
declara en cada ViewSet (Fase 4 y 5), no de forma global.

### 6.3 — `src/nucleo/urls.py`

Agregar las dos rutas de token (como en el `urls.py` del profe), sin tocar las líneas del
router/includes que manejan Fases 4 y 5:

```python
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    ...
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
```

### ✅ Criterio de aceptación

- `POST /api/token/` con `{"username": "...", "password": "..."}` de un superusuario existente
  → 200, devuelve `access` y `refresh`.
- `POST /api/token/refresh/` con el `refresh` → 200, devuelve `access` nuevo.
- Pegarle a cualquier endpoint de Fase 4/5 sin header → 401.
- Con header `Authorization: Bearer <access>` → funciona igual que antes de JWT.
- `uv run manage.py check` sin errores.

---

# Fase 7 — Pruebas, README y merge

**Rama:** `fase-7/documentacion`
**Responsable:** Tiago
**Depende de:** Fases 4, 5 y 6 mergeadas a `develop`.

### 7.1 — Prueba de humo end-to-end

1. Confirmar que `nucleo/routers.py` y `nucleo/urls.py` quedaron como el estado final del
   contrato de nombres, y que no quedan `users/urls.py` ni `bienes/urls.py`.
2. `GET /api/` → el índice del router lista los 4 recursos (`usuarios`, `herederos`, `bienes`,
   `asignaciones`).
3. `POST /api/token/` con un superusuario → guardar `access`.
4. Con ese token: `GET /api/usuarios/` → 200, lista de usuarios (sin poder hacer `POST`).
5. `POST /api/herederos/` → crear a Ana y Juan.
6. `POST /api/bienes/` → crear el bien de 0.05 BTC.
7. `POST /api/asignaciones/` → repartir 50/50.
8. `GET /api/asignaciones/` → confirmar que trae `bien` y `heredero` anidados, y que sin token
   da 401.

### 7.2 — Actualizar `README.md`

En la sección `🌐 API REST`:

- Sumar `GET /api/usuarios/` y `GET /api/usuarios/{id}/` a los "Implementados", aclarando que
  es de solo lectura.
- Si se hizo 5.5, sumar `GET /api/bienes/mios/`.
- Aclarar que **todos los endpoints ahora requieren JWT** (`Authorization: Bearer <token>`),
  salvo `POST /api/token/` y `POST /api/token/refresh/`.
- Sacar la nota vieja de "en el listado viaja anidado, en el detalle viaja como id" para
  `bienes` — ya no es así (Fase 5 lo unificó, ver nota en el criterio de aceptación de esa
  fase).
- Mover `POST /api/auth/register/`, `login`, `logout` a "pendientes" si no existen (siguen sin
  existir — JWT no incluye registro, los usuarios se crean por `/admin/`).
- Marcar el checklist de la consigna:
  - [x] ViewSets (`ModelViewSet` x3, `ReadOnlyModelViewSet` x1)
  - [x] Router en `routers.py`
  - [x] `permission_classes`
  - [x] JWT (+ SessionAuth opcional)

### 7.3 — Merge final

```shell
git checkout develop && git pull
git checkout main && git pull
git merge develop
git push origin main
```

O por Pull Request desde GitHub, como en la Entrega 2.

---

## Resumen de ramas

| Fase | Rama | Quién | Orden |
|---|---|---|---|
| 4 | `fase-4/viewsets-users` | Valen | ✅ hecha |
| 5 | `fase-5/viewsets-bienes` | Valen | ✅ hecha |
| 6 | `fase-6/auth-jwt` | Tiago | después de Fase 5 |
| 7 | `fase-7/documentacion` | Tiago | no, va última |

## Checklist de la consigna

- [ ] **ViewSets en reemplazo de Concrete Generics** → `BienViewSet`, `AsignacionViewSet`,
  `HerederoViewSet` (`ModelViewSet`) + `UserViewSet` (`ReadOnlyModelViewSet`) (Fases 4 y 5).
- [ ] **Enrutamiento en `routers.py`** → un solo `nucleo/routers.py` con `DefaultRouter` y los 4
  ViewSets, como el `settings/routers.py` del profe (Fases 4 y 5).
- [ ] **`permission_classes` en los viewsets** → `IsAuthenticated` en los 4 (Fases 4 y 5).
- [ ] **JWT con `djangorestframework-simplejwt`** (+ `SessionAuthentication` opcional) →
  Fase 6.
- [ ] **Una sola forma de escribir vistas** → se borran `@api_view` (`users`), Concrete Generic
  (`bienes`) y los `urls.py` de las apps, no quedan comentados (Fases 4 y 5).
