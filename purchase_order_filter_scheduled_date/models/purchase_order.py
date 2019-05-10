# -*- coding: utf-8 -*-


from odoo import api, fields, models


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    @api.multi
    def _get_picking_state(self):
        for order in self:
            if len(order.picking_ids) != 0:
                for picking_id in order.picking_ids:
                    for pick in picking_id:
                        if pick.state == 'done':
                            order.has_been_shipped = True

    @api.multi
    def _search_value(self, operator, value):
        recs = self.search([]).filtered(lambda x: x.has_been_shipped is False)
        if recs:
            return [('id', 'in', [x.id for x in recs])]

    has_been_shipped = fields.Boolean(
        string='Delivered',
        compute=_get_picking_state,
        search='_search_value'
        )
