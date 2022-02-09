import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-server-brand",
    description="Meta package for oca-server-brand Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-disable_odoo_online',
        'odoo14-addon-portal_odoo_debranding',
        'odoo14-addon-remove_odoo_enterprise',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
