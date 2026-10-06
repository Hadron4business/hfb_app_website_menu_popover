# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=0 shiftwidth=4 smarttab expandtab fileformat=unix
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
{
    'name': "Website Menu Popover",
    'summary': "Ask visitors to confirm before they follow a website menu link",
    'description': """
Website Menu Popover
====================

Sometimes a menu link should not be followed blindly: a link to another
shop, to a different country site, or to a page with different terms.

This app adds two settings to every website menu item: "Show Popover" and
"Popover Text". When a visitor clicks such a menu item, a dialog with your
text appears first, with "Continue" and "Cancel" buttons. The visitor is
taken to the link only after pressing Continue. The text can be translated
into every website language.
""",
    'version': "20.0.1.0.1",
    'author': "Hadron for Business sp. z o.o.",
    'website': "http://hadronforbusiness.com",
    'license': "OPL-1",
    'category': "Website/Website",
    'depends': [
        'website',
    ],
    'data': [
        'views/website_menu_views.xml',
        'views/popover_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'hfb_app_website_menu_popover/static/src/js/menu_popover.js',
        ],
    },
    'images': [
        'static/description/banner_screenshot.png',
    ],
    'installable': True,
    'application': False,
}
