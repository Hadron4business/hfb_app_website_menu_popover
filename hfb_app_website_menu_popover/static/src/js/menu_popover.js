/** @odoo-module ignore */
'use strict';

/* Confirmation popover before following a configured menu link (Website >
 * Site > Menus > a menu item's "Show Popover" + "Popover Text") - works for any
 * menu item an admin flags this way.
 *
 * Config comes from a <script type="application/json"> tag injected into
 * every page (views/popover_templates.xml, website._get_popover_menus_json())
 * - not inline JS, just data, so nothing here executes unless a matching
 * link is actually clicked.
 *
 * The dialog itself is a plain, hand-built overlay - not Bootstrap's own
 * Modal API. Odoo's frontend bundle doesn't reliably expose a global
 * `window.bootstrap` object (confirmed live: "Cannot read properties of
 * undefined (reading 'Modal')"), even though Bootstrap's CSS is always
 * loaded - so only Bootstrap's CSS classes are used here, for styling, not
 * its JS.
 */
(function () {
    function onReady(fn) {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', fn);
        } else {
            fn();
        }
    }

    function normalizeUrl(href) {
        try {
            var u = new URL(href, window.location.href);
            // origin+pathname, not just pathname: two different websites on
            // this database can share the same path (e.g. both have "/"),
            // and only comparing pathname would wrongly match a same-site
            // link too.
            return u.origin + u.pathname.replace(/\/+$/, '');
        } catch (e) {
            return href;
        }
    }

    function escapeHtml(text) {
        return (text || '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
    }

    function showPopover(match, onContinue) {
        var overlay = document.createElement('div');
        overlay.className = 'hfb_menu_popover_overlay';
        overlay.setAttribute('style',
            'position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:2000;' +
            'display:flex;align-items:center;justify-content:center;padding:16px;');

        var dialog = document.createElement('div');
        dialog.setAttribute('style',
            'background:#fff;border-radius:.5rem;max-width:420px;width:100%;' +
            'padding:1.5rem;box-shadow:0 1rem 3rem rgba(0,0,0,.25);');
        dialog.innerHTML =
            '<div class="mb-3">' + escapeHtml(match.text).replace(/\n/g, '<br/>') + '</div>' +
            '<div class="text-end">' +
                '<button type="button" class="btn btn-secondary me-2" data-hfb-cancel="1">' + escapeHtml(match.cancel_label || 'Cancel') + '</button>' +
                '<button type="button" class="btn btn-primary" data-hfb-continue="1">' + escapeHtml(match.continue_label || 'Continue') + '</button>' +
            '</div>';
        overlay.appendChild(dialog);
        document.body.appendChild(overlay);

        function close() {
            overlay.remove();
            document.removeEventListener('keydown', onKeydown);
        }
        function onKeydown(ev) {
            if (ev.key === 'Escape') {
                close();
            }
        }

        overlay.addEventListener('click', function (ev) {
            if (ev.target === overlay) {
                close();
            }
        });
        dialog.querySelector('[data-hfb-cancel]').addEventListener('click', close);
        dialog.querySelector('[data-hfb-continue]').addEventListener('click', function () {
            close();
            onContinue();
        });
        document.addEventListener('keydown', onKeydown);
    }

    onReady(function () {
        var dataEl = document.getElementById('hfb_menu_popover_data');
        if (!dataEl) {
            return;
        }
        var menus;
        try {
            menus = JSON.parse(dataEl.textContent || '[]');
        } catch (e) {
            return;
        }
        if (!menus.length) {
            return;
        }

        var byUrl = {};
        menus.forEach(function (m) {
            if (m.url) {
                byUrl[normalizeUrl(m.url)] = m;
            }
        });

        // Capture phase on window + stopImmediatePropagation: Google Tag
        // Manager's "Link Click" trigger with "Wait for tags" re-navigates
        // to the href itself ~1s later, ignoring preventDefault(), so it
        // must never see this click at all.
        window.addEventListener('click', function (ev) {
            var link = ev.target.closest && ev.target.closest('a[href]');
            if (!link) {
                return;
            }
            var match = byUrl[normalizeUrl(link.href)];
            if (!match) {
                return;
            }

            ev.preventDefault();
            ev.stopImmediatePropagation();
            var targetHref = link.href;
            showPopover(match, function () {
                window.location.href = targetHref;
            });
        }, true);
    });
})();
//EoF
