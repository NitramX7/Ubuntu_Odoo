from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Ordenador(models.Ordenador):
    _name = "ubuntu_odoo.ordenador"
    _description = "Un ordenador con diferentes componentes"

    name = fields.Char(string="Nombre técnico", required=True)
    user_id = fields.Many2one('res.users', string='Usuario')

    components_ids = fields.Many2many("pc.components", string="Componentes")

    ultima_modificacion = fields.Datetime(
        string='Última modificación',
        compute='_compute_ultima_modificacion',
    )
    precio = fields.Monetary(compute="_calcular_total")

    @api.depends("components_ids.precio")
    def _compute_total(self):
        for record in self:
            total = 0.0
            for componente in record.components_ids:
                total += componente.precio

            record.precio = total

    @api.depends('write_date', 'create_date')
    def _compute_ultima_modificacion(self):
        for record in self:
            record.ultima_modificacion = record.write_date or record.create_date

    @api.constrains('ultima_mod')
    def _comprobar_fecha(self):
        for record in self:
            if TEST:  # Sustituir test por la prueba booleana correspondiente
                raise ValidationError("La fecha no puede ser futura")
