from odoo import fields, models


class Componente(models.Model):
    _name = "equipos_empresa.componente"
    _description = "Componente de ordenador"

    name = fields.Char(string="Nombre técnico", required=True)
    especificaciones = fields.Text(string="Especificaciones")
    price = fields.Monetary(string="Precio")
    currency_id = fields.Many2one(
        "res.currency",
        string="Moneda",
        required=True,
        default=lambda self: self.env.company.currency_id,
    )
