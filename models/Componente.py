from odoo import fields, models


class Componente(models.Model):
    _name = "ubuntu_odoo.componente"
    _description = "Componente de ordenador"

    name = fields.Char(string="Nombre técnico", required=True)
    especificaciones = fields.Text(string="Especificaciones")
    currency_id = fields.Many2one(
        'res.currency',
        string="Currency",

    )

    price = fields.Monetary(
        string="Price",
        currency_field='currency_id'
    )
