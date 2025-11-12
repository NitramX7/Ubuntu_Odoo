from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Ordenador(models.Model):
    _name = "equipos_empresa.ordenador"
    _description = "Ordenador de la empresa"
    _rec_name = "numero_equipo"

    _sql_constraints = [
        (
            "numero_equipo_unique",
            "unique(numero_equipo)",
            "El número de equipo debe ser único.",
        )
    ]

    numero_equipo = fields.Char(string="Número de equipo", required=True)
    user_id = fields.Many2one("res.users", string="Usuario", required=True)
    componente_ids = fields.Many2many(
        "equipos_empresa.componente",
        string="Componentes",
    )
    os_tag_ids = fields.Many2many(
        "equipos_empresa.so_tag",
        string="Sistemas operativos",
    )
    incidencias = fields.Text(string="Incidencias")

    ultima_modificacion = fields.Date(
        string="Última modificación",
        compute="_compute_ultima_modificacion",
        store=True,
        readonly=True,
    )

    currency_id = fields.Many2one(
        "res.currency",
        string="Moneda",
        required=True,
        default=lambda self: self.env.company.currency_id,
    )
    precio_total = fields.Monetary(
        string="Precio total",
        compute="_compute_precio_total",
        store=True,
        currency_field="currency_id",
        readonly=True,
    )

    @api.depends("write_date", "create_date")
    def _compute_ultima_modificacion(self):
        for rec in self:
            dt = rec.write_date or rec.create_date
            rec.ultima_modificacion = fields.Date.to_date(dt) if dt else False

    @api.depends("componente_ids.price", "componente_ids.currency_id", "currency_id")
    def _compute_precio_total(self):
        company = self.env.company
        today = fields.Date.context_today(self)
        for rec in self:
            total = 0.0
            for comp in rec.componente_ids:
                amount = comp.price or 0.0
                if comp.currency_id and rec.currency_id and comp.currency_id != rec.currency_id:
                    amount = comp.currency_id._convert(amount, rec.currency_id, company, today)
                total += amount
            rec.precio_total = total

    @api.constrains("ultima_modificacion")
    def _comprobar_fecha(self):
        today = fields.Date.context_today(self)
        for record in self:
            if record.ultima_modificacion and record.ultima_modificacion > today:
                raise ValidationError("La fecha no puede ser futura")
