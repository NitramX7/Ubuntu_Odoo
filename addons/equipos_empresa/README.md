# Equipos de la Empresa

Módulo Odoo para gestionar ordenadores, componentes, incidencias y usuarios.

## Modelos

- `equipos_empresa.componente`
  - `name` (Char): Nombre técnico.
  - `especificaciones` (Text): Especificaciones del componente.
  - `price` (Monetary), `currency_id` (Many2one): Precio y moneda.

- `equipos_empresa.so_tag`
  - `name` (Char): Nombre del S.O.
  - `color` (Integer): Color opcional para etiquetas.

- `equipos_empresa.ordenador`
  - `numero_equipo` (Char, requerido): Identificador del equipo.
  - `user_id` (Many2one a `res.users`, requerido): Usuario asignado (relación Many2one; un usuario puede tener muchos ordenadores, pero cada ordenador tiene un único usuario).
  - `componente_ids` (Many2many a `equipos_empresa.componente`): Lista de piezas (relación Many2many; las piezas no son únicas y pueden repetirse en varios ordenadores).
  - `os_tag_ids` (Many2many a `equipos_empresa.so_tag`): Tags de sistemas operativos (widget de tags en la vista).
  - `incidencias` (Text): Registro de incidencias.
  - `ultima_modificacion` (Date, compute+store, readonly): Última modificación basada en `write_date`/`create_date`.
  - `currency_id` (Many2one a `res.currency`): Moneda del ordenador.
  - `precio_total` (Monetary, compute+store, readonly): Suma de precios de los componentes, con conversión automática de moneda.

## Lógica y restricciones

- `_compute_ultima_modificacion`: Toma la fecha de `write_date` (o `create_date`).
- `_comprobar_fecha` (constraint): Impide que `ultima_modificacion` esté en el futuro.
- `_compute_precio_total`: Suma `price` de cada componente; si la moneda del componente difiere, convierte usando la moneda de la compañía y la fecha actual.

## Vistas

- Listas y formularios para `Componentes` y `Ordenadores`.
- En `Ordenador` se usa el widget `many2many_tags` para `componente_ids` y `os_tag_ids`.
- Campos calculados en solo lectura (`ultima_modificacion`, `precio_total`).

## Seguridad

Grupos:
- `Equipos - Usuario` (`equipos_empresa.group_equipos_user`): Acceso de solo lectura.
- `Equipos - Manager` (`equipos_empresa.group_equipos_manager`): Lectura/creación/escritura/borrado.

Se definen en `security/security.xml` y sus permisos en `security/ir.model.access.csv`.

## Instalación

1. Copia `ubuntu_odoo/equipos_empresa` a tu ruta de addons de Odoo (o añade `ubuntu_odoo` a `addons_path`).
2. Actualiza la lista de aplicaciones e instala "Equipos de la Empresa".
3. Asigna a los usuarios los grupos "Equipos - Usuario" o "Equipos - Manager" desde Ajustes → Usuarios.

## Notas

- `numero_equipo` no tiene restricción de unicidad por defecto; si la necesitas, se puede añadir un `_sql_constraints`.
- Si quieres que el ordenador tenga `company_id`, se puede añadir para multiempresa y conversiones por compañía.
