import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-server-brand",
    description="Meta package for oca-server-brand Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-disable_odoo_online',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
