# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (c) 2010-2012 Elico Corp. All Rights Reserved.
#    Author:            Andy Lu <andy.lu@elico-corp.com>
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Purchase Order Approvement',
    'version': '1.0',
    'category': 'Sales & Purchases',
    'description': """
        Button on PO will pop a question, give the operator a chance to confirm.
    """,
    'author': 'Elico Corp',
    'website': 'http://www.openerp.net.cn',
    'depends': ['purchase'],
    'init_xml': [],
    'update_xml': [
        'purchase_confirm_view.xml',
    ],
    'demo_xml': [], 
    'test': [],
    'installable': True,
    'active': False,
    'certificate': '',
}