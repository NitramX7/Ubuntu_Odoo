# Ubuntu_Odoo: Gestión de Equipos

Este módulo añade gestión de ordenadores, componentes, incidencias y etiquetas de sistemas operativos.

## Modelos

- ubuntu_odoo.componente
  - name (Char): Nombre técnico.
  - especificaciones (Text): Especificaciones del componente.
  - price (Monetary) y currency_id (Many2one): Precio y moneda.

- ubuntu_odoo.so_tag
  - name (Char): Nombre del S.O.
  - color (Integer): Color para etiquetas.

- ubuntu_odoo.ordenador
  - numero_equipo (Char, requerido, único): Identificador del equipo.
  - user_id (Many2one a res.users, requerido): Usuario asignado.
  - componente_ids (Many2many a ubuntu_odoo.componente): Lista de piezas.
  - os_tag_ids (Many2many a ubuntu_odoo.so_tag): Sistemas operativos (widget tags con color).
  - incidencias (Text): Registro de incidencias.
  - ultima_modificacion (Date, compute+store): Fecha de última modificación (de write_date/create_date). No puede ser futura.
  - currency_id (Many2one a res.currency): Moneda del ordenador.
  - precio_total (Monetary, compute+store): Suma de precios de componentes con conversión de moneda.

## Lógica

- _compute_ultima_modificacion: Convierte write_date/create_date a fecha.
- _comprobar_fecha: Valida que ultima_modificacion no sea futura.
- _compute_precio_total: Suma precios; convierte divisas si difieren.

## Vistas y menús

- Componentes: vista árbol y formulario (views/componente_views.xml).
- Ordenadores: vista árbol y formulario con pestañas para Componentes, S.O. e Incidencias (views/ordenador_views.xml).
- Tags de S.O.: árbol/form con color_picker (views/so_tag_views.xml).
- Menú raíz "Equipos" con accesos a Ordenadores, Componentes y Sistemas Operativos (views/menu.xml).

## Seguridad

- Grupos existentes del módulo (Usuario/Administrador) se reutilizan.
- Accesos en security/ir.model.access.csv: Usuario (lectura), Admin (CRUD) para los tres modelos.

## Instalación/Actualización

1. Asegura que el módulo está en addons_path.
2. Actualiza la app: Ajustes → Activar modo desarrollador → Aplicaciones → Actualizar lista.
3. Instala o actualiza "martinModulo".
4. Asigna grupos a usuarios si procede.

## Notas

- Si necesitas multiempresa, añade company_id en modelos y usa su moneda.
- Se puede extender con mantenimiento (historial, costes) si lo requieres.
