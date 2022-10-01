import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-server-brand",
    description="Meta package for oca-server-brand Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-disable_odoo_online',
        'odoo13-addon-portal_odoo_debranding',
        'odoo13-addon-remove_odoo_enterprise',
        'odoo13-addon-remove_odoo_mobile_appstore',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 13.0',
    ]
)
