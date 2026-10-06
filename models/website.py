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
"""	@version	20.0.1.0.3
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.06

	Popover menu data for the frontend
	Builds the JSON list of popover-enabled menu items of the current website,
	including the translated button labels, which the frontend script reads to
	intercept clicks.
"""
import json

from markupsafe import Markup

from odoo import _, models


class Website(models.Model):
    _inherit = 'website'

    def _get_popover_menus_json(self):
        """JSON list [{'url', 'text', 'continue_label', 'cancel_label'}, ...]
        of this website's menu items that have a popover, read by
        static/src/js/menu_popover.js.

        Returned as Markup: it is written into a <script type="application/json">
        body by QWeb, and HTML-escaping would corrupt the JSON as soon as a
        popover text contains a quote or an ampersand."""
        if len(self) != 1:
            return Markup('[]')
        # url is computed in Odoo 20; its search does not handle "!= False",
        # so empty urls are filtered in Python.
        menus = self.env['website.menu'].sudo().search([
            ('website_id', '=', self.id),
            ('show_popover', '=', True),
        ]).filtered('url')
        continue_label = _("Continue")
        cancel_label = _("Cancel")
        return Markup(json.dumps([{
            'url': menu.url,
            'text': menu.popover_text or '',
            'continue_label': continue_label,
            'cancel_label': cancel_label,
        } for menu in menus]).replace('<', '\\u003c'))

#EoF
