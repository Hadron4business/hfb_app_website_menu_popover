# Website Menu Popover

Shows a confirmation dialog before a visitor follows a chosen website menu link.

## What it does

- **Per menu item** - Switch the popover on for the menu items that need it. All other links behave as usual.
- **Your own text** - Write the message the visitor sees, and translate it into every website language.
- **Continue or cancel** - The visitor follows the link only after pressing Continue. Cancel, Escape or a click outside closes the dialog.
- **No code** - Two fields in the standard menu editor. Nothing else to configure.
- **Any link** - Works for internal pages and for external addresses.
- **Lightweight** - A small script and no extra libraries.

## How to use it

1. Activate developer mode (Settings > Activate the developer mode), then open Website > Configuration > Menus.
2. Open the menu item you want to confirm (search by name; the list is grouped by website).
3. Tick Show Popover. A Popover Text field appears.
4. Type the message, for example: "You are about to leave this shop. Continue?" and save.
5. Open the website and click the menu item: the dialog appears. The link is followed only after Continue.
6. To translate the text, use the translate icon next to Popover Text (language button on the field).

## Good to know

- The popover appears on the exact link set in the menu item's URL. Other links to the same address on the page (for example a button) also show it.
- A menu item with sub-items (a dropdown) works too: set the popover on the sub-item you want to confirm.
- Button labels (Continue / Cancel) follow the visitor's language and can be translated in Settings > Translations.
- If a visitor has JavaScript disabled, the link simply works as a normal link.

## Technical

- `models/website_menu.py` - fields `show_popover`, `popover_text` (translatable) on `website.menu`.
- `models/website.py` - `_get_popover_menus_json()` builds the config for the current website.
- `views/popover_templates.xml` - injects the config as a `<script type="application/json">` tag into every page.
- `static/src/js/menu_popover.js` - intercepts the click and shows a hand-built overlay (no Bootstrap JS needed).
- Depends on: `website`.

## Status

Source: client module (Odoo 18), where it was built for a main shop to outlet shop link. Neutralised and made generic. Odoo 20 build.
