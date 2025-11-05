from odoo import fields, models


class Ejemplo(models.Model):
    _name = "modelo.de.ejemplo"
    _descriptio = "Modelo para hacer una prueba"

    name = fields.Char(string="Nombre")
