import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-server-brand",
    description="Meta package for oca-server-brand Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-disable_odoo_online>=16.0dev,<16.1dev',
        'odoo-addon-portal_odoo_debranding>=16.0dev,<16.1dev',
        'odoo-addon-remove_odoo_enterprise>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
