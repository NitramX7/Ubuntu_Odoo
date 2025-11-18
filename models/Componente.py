from odoo import fields, models


class Componente(models.Model):
    _name = "ubuntu_odoo.componente"
    _description = "Componente de ordenador"

    name = fields.Char(string="Nombre técnico", required=True)
    especificaciones = fields.Text(string="Especificaciones")
    price = fields.Monetary(string="Precio")
