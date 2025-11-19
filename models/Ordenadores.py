from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo import fields as odoo_fields


class Ordenador(models.Model):
    _name = "ubuntu_odoo.ordenador"
    _description = "Un ordenador con diferentes componentes"

    name = fields.Char(string="Nombre técnico", required=True)
    user_id = fields.Many2one('res.users', string='Usuario')

    components_ids = fields.Many2many(
        "ubuntu_odoo.componente", string="Componentes")

    ultima_modificacion = fields.Datetime(
        string='Última modificación',
        compute='_compute_ultima_modificacion',
    )

    currency_id = fields.Many2one(
        'res.currency',
        string="Moneda",
        required=True,
        default=lambda self: self.env.company.currency_id.id,
    )

    precio = fields.Monetary(
        string="Precio total",
        currency_field='currency_id',
        compute='_compute_total',
    )

    @api.depends("components_ids.price")
    def _compute_total(self):
        for record in self:
            total = 0.0
            for componente in record.components_ids:
                total += componente.price or 0.0
            record.price = total

    @api.depends('write_date', 'create_date')
    def _compute_ultima_modificacion(self):
        for record in self:
            record.ultima_modificacion = record.write_date or record.create_date

    @api.constrains('ultima_modificacion')
    def _comprobar_fecha(self):
        ahora = odoo_fields.Datetime.now()
        for record in self:
            if record.ultima_modificacion and record.ultima_modificacion > ahora:
                raise ValidationError("La fecha no puede ser futura")
