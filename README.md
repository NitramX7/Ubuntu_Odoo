# Ubuntu_Odoo – Gestión de equipos y componentes

Módulo Odoo para inventariar ordenadores, sus componentes y los sistemas operativos instalados, calculando el coste total por equipo y evitando fechas futuras de modificación.

## Modelos principales

### Componentes (`ubuntu_odoo.componente`)
- `name`: Nombre técnico (requerido).
- `especificaciones`: Detalles libres.
- `currency_id`: Moneda del precio.
- `price`: Importe del componente (Monetary).

### Sistemas Operativos (`ubuntu_odoo.sistema_operativo`)
- `name`: Nombre del S.O. (requerido).

### Ordenadores (`ubuntu_odoo.ordenador`)
- `name`: Nombre técnico del equipo (requerido).
- `user_id`: Usuario asignado.
- `components_ids`: Many2many de componentes.
- `sistema_operativo_ids`: Many2many de sistemas operativos (widget tags).
- `ultima_modificacion` (compute): Toma `write_date` o `create_date`.
- `currency_id`: Moneda del equipo (por defecto, la de la compañía).
- `precio` (compute): Suma de los precios de los componentes.

## Lógica y validaciones

- `_compute_total`: Suma los `price` de `components_ids` y los muestra en `precio`.
- `_compute_ultima_modificacion`: Refleja la última fecha de cambio o creación.
- `_comprobar_fecha`: Evita que `ultima_modificacion` quede en el futuro (lanza `ValidationError`).

## Vistas y menús

- Componentes: lista y formulario (`views/pc_componentes.xml`).
- Ordenadores: lista y formulario con componentes y S.O. (`views/pc_computer.xml`).
- Menú raíz “Equipos” con accesos a Ordenadores y Componentes (`views/menu.xml`).

## Seguridad

- Grupos de respaldo: `group_martin_modulo_user` y `group_martin_modulo_admin`.
- Accesos: usuarios internos (`base.group_user`) pueden leer/crear/editar/borrar componentes, ordenadores y sistemas operativos (`security/ir.model.access.csv`).

## Uso rápido

1. Instala o actualiza el módulo (`martinModulo`) y activa modo desarrollador.
2. Crea componentes con su precio y moneda.
3. Registra sistemas operativos disponibles.
4. Crea ordenadores, asigna usuario, añade componentes y sistemas operativos.
5. Revisa el campo “Precio total” calculado automáticamente y la “Última modificación”.
