from odoo import models, fields


class SistemaOperativo(models.Model):
    _name = "ubuntu_odoo.sistema_operativo"
    _description = "Sistema Operativo"

    name = fields.Char(string="Nombre", required=True)
