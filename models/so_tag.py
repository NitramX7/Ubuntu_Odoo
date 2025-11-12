from odoo import fields, models


class SistemaOperativoTag(models.Model):
    _name = "ubuntu_odoo.so_tag"
    _description = "Etiqueta de sistema operativo"

    name = fields.Char(string="Nombre", required=True)
    color = fields.Integer(string="Color")
