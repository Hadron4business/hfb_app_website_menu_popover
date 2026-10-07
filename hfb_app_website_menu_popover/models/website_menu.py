# -*- coding: utf-8 -*-
#################################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2017-2026 Hadron for Business sp. z o.o. (http://hadronforbusiness.com)
#
# This program is proprietary software, licensed under the Odoo Proprietary
# License v1.0 (OPL-1). Its use is governed by the Odoo Apps terms available
# at https://www.odoo.com/documentation/user/legal/licenses.html and the
# license agreement accepted at purchase / installation.
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the
# Software or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in
# all copies or substantial portions of the Software.
#
#################################################################################
"""	@version	17.0.1.0.0
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.06

	Menu item popover settings
	Adds the Show Popover flag and the translatable Popover Text to website menu
	items.
"""
from odoo import fields, models


class WebsiteMenu(models.Model):
    _inherit = 'website.menu'

    show_popover = fields.Boolean(
        string="Show Popover",
        help="Show a confirmation popover with the text below before "
             "following this menu item's link.",
    )
    popover_text = fields.Text(
        string="Popover Text", translate=True,
        help="Shown in the popover when a visitor clicks this menu item, "
             "before they are taken to its link.",
    )

#EoF
