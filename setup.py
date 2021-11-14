from setuptools import setup

setup(
    name='django_site_variables',
    version='0.1',
    packages=['django_site_settings', 'django_site_settings.migrations'],
    url='',
    license='MIT',
    author='Mikhail Badrazhan',
    author_email='svne@devilweb.ru',
    description='Site variables application',
    python_requires='>=3.0',
    install_requires=['django>=2.2']
)
