import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-server-brand",
    description="Meta package for oca-server-brand Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-disable_odoo_online',
        'odoo11-addon-res_config_settings_enterprise_remove',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
