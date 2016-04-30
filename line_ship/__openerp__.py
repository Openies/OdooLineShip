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

{
    'name': 'Line ship',
    'version': '1.0',
    'category': 'Sales Management',
    'description': """
Enables functionality to use allotment partner on the sale order line.
If the allotment partner is defined on the sale order line, when you confirm the order it will group the delivary order based on allotment partner.
""",
    'summary': "Order Line, Allotment Partner, Shipment",
    'author': 'Openies Services',
    'website': 'http://www.Openies.com/',
    'images': [],
    'depends': ['sale_stock'],
    'data': [
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
