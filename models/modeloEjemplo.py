from odoo import models, fields


class Ejemplo(models.Model):
    _name = "modelo.de.ejemplo"
    _description = "Modelo para hacer una prueba"

    # Campos que sí usas en las vistas XML
    name = fields.Char(string="Nombre")
    ex_field = fields.Char(string="Example")
    ex_field_2 = fields.Char(string="Otro campo")
    ex_field_3 = fields.Char(string="Oculto")
