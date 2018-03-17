.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

===================================
Settings - Remove Enterprise Fields
===================================

This module removes enterprise-only features from all settings views.
Note that it does not remove the possibility to install
Enterprise modules. If necessary, all Enterprise Edition code is still
available and can be manually installed via the Apps menu.

Usage
=====

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/252/11.0

Known issues / Roadmap
======================

Keep in mind that this module does not mark the enterprise fields as invisible.
Instead, it completely removes them, so any modules that are referencing those fields in
the settings views will break.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/server-brand/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://odoo-community.org/logo.png>`_.

Contributors
------------

* Brett Wood <bwood@laslabs.com>
* Michell Stuttgart <michellstut@gmail.com>
* Andrea Stirpe <a.stirpe@onestein.nl>

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.
