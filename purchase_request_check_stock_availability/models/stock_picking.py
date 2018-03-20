# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from odoo import api, fields, models, exceptions, _

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:

class StockPicking(models.Model):
    
    # 1. Private attributes
    _inherit = 'stock.picking'

    # 2. Fields declaration

    purchase_request_id = fields.Many2one(
        comodel_name='purchase.request',
        string='Purchase Request'
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods