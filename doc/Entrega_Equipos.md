# Entrega: Gestión de Equipos (Ubuntu_Odoo)

Autor: martinModulo

## Introducción
Este documento describe las funcionalidades añadidas al módulo Ubuntu_Odoo para gestionar:
- Ordenadores de la empresa
- Componentes de hardware
- Incidencias asociadas
- Tags de sistemas operativos (con colores)

## Modelado realizado
- Modelo `ubuntu_odoo.componente`
  - Nombre técnico, especificaciones, precio (moneda configurable)
- Modelo `ubuntu_odoo.so_tag`
  - Etiquetas de sistemas operativos con color
- Modelo `ubuntu_odoo.ordenador`
  - Número de equipo (único y obligatorio)
  - Usuario asignado (`res.users`) [Many2one]
  - Lista de piezas [Many2many a componentes]
  - Incidencias (texto largo)
  - Tags de S.O. [Many2many]
  - Última modificación [compute+store], validada para no ser futura
  - Precio total [compute+store], suma de piezas con conversión de moneda

## Restricciones y comportamiento
- Unicidad: `numero_equipo` no se puede repetir.
- Fecha: `ultima_modificacion` no puede ser futura; se toma de `write_date`/`create_date`.
- Precio total: suma automática de `price` de cada componente; si hay distintas monedas, se convierte a la del ordenador usando la moneda de la compañía.

## Vistas y menús
- Componentes: vista lista + formulario.
- Ordenadores: lista + formulario con pestañas para Componentes, S.O. e Incidencias.
- Tags de S.O.: lista + formulario con `color_picker`.
- Menú raíz: "Equipos" con accesos a Ordenadores, Componentes y Sistemas Operativos.

## Seguridad
- Se reutilizan los grupos del módulo: Usuario (lectura) y Admin (CRUD).
- Permisos definidos en `security/ir.model.access.csv`.

## Cómo usar
1) Actualiza/instala el módulo desde Aplicaciones.
2) Ve a: Equipos → Componentes y crea tus piezas.
3) Ve a: Equipos → Ordenadores y crea el equipo asignando usuario y componentes.
4) Opcional: Equipos → Sistemas Operativos (Tags) para gestionar etiquetas.

## Capturas de pantalla (dónde ponerlas)
- Coloca tus imágenes en `Ubuntu_Odoo/doc/capturas` con formato PNG o JPG.
- Nombres sugeridos:
  - `01_componentes_lista.png`
  - `02_componentes_form.png`
  - `03_ordenadores_lista.png`
  - `04_ordenador_form.png`
  - `05_tags_so.png`
- Al volver a generar el PDF, el script insertará todas las imágenes encontradas en esa carpeta en orden alfabético.

## Regenerar PDF
- Requisitos: Python con `reportlab`.
- Comando: `python doc/build_pdf.py` desde la carpeta del módulo `Ubuntu_Odoo`.
- Salida: `doc/Entrega_Equipos.pdf`.

## Créditos y mantenimiento
- Código y vistas en `models/` y `views/` del módulo Ubuntu_Odoo.
- Ajustes futuros: multiempresa, mantenimiento programado, importación de catálogos.
