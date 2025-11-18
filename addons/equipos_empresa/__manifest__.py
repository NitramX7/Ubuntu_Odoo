{
    "name": "Equipos de la Empresa",
    "summary": "Registro de ordenadores, componentes, incidencias y usuarios.",
    "description": "Gestiona ordenadores de la empresa, sus componentes, incidencias, precio total y usuario asignado.",
    "version": "1.1.0",
    "author": "Your Company",
    "category": "Operations/IT",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/componente_views.xml",
        "views/ordenador_views.xml",
        "views/so_tag_views.xml",
        "views/menu.xml",
    ],
    "application": True,
}
