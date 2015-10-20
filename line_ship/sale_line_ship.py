# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Odoo.com.
#    Copyright (C) 2015 Openies.com.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    order_partner_id = fields.Many2one(
        "res.partner", string='Customer', readonly=False, related=False)


class SaleOrder(models.Model):
    
    _inherit = 'sale.order'
    
    def _prepare_order_line_procurement(
            self, cr, uid, order, line, group_id=False, context=None):
        vals = super(SaleOrder, self)._prepare_order_line_procurement(cr, uid, order, line, group_id, context)
        if line and line.order_partner_id:
            vals['partner_dest_id'] = line.order_partner_id.id
        return vals


class procurement_order(models.Model):
    
    _inherit = 'procurement.order'
    
    def _run_move_create(self, cr, uid, procurement, context=None):
        vals = super(procurement_order, self)._run_move_create(cr, uid, procurement, context)
        if procurement.partner_dest_id.id:
            vals.update({'partner_id': procurement.partner_dest_id.id})
        return vals


class StockMove(models.Model):
    
    _inherit = 'stock.move'

    @api.multi
    def _picking_assign(self):
        vals = super(StockMove, self)._picking_assign()
        pick_obj = self.env['stock.picking']
        for move in self:
            line_partner_id = \
                move.procurement_id.sale_line_id.order_partner_id.id
            picking_partner_id = move.picking_id.partner_id.id
            if not line_partner_id:
                continue
            if picking_partner_id != line_partner_id:
                picks = pick_obj.search([
                    ('partner_id', '=', line_partner_id),
                    ('group_id', '=', move.group_id.id),
                    ('location_id', '=', move.location_id.id),
                    ('location_dest_id', '=', move.location_dest_id.id),
                    ('picking_type_id', '=', move.picking_type_id.id),
                    ('printed', '=', False),
                    ('state', 'in',
                        ['draft', 'confirmed', 'waiting',
                         'partially_available', 'assigned'])
                    ], limit=1)
                if len(picks):
                    move.write({'picking_id': picks.id})
                else:
                    print "in the elseeee"
                    values = {
                        'partner_id': line_partner_id,
                        'origin': move.origin,
                        'company_id': move.company_id and move.company_id.id or False,
                        'move_type': move.group_id and move.group_id.move_type or 'direct',
                        'picking_type_id': move.picking_type_id and move.picking_type_id.id or False,
                        'location_id': move.location_id.id,
                        'location_dest_id': move.location_dest_id.id,
                    }
                    picks = pick_obj.create(values)
                    move.write({'picking_id': picks.id})
        return vals
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
