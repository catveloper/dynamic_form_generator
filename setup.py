from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='form_schema_generator',
    version='1.1',
    description='model base form schema generator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Dong Uk Im',
    author_email='donguk.im@datamaker.io',
    url='',
    download_url='',
    install_requires=[
        'Django>=3.2.0',
        'djangorestframework>=3.12.4',
        'drf-spectacular>=0.19.0'
    ],
    packages=find_packages(include=['form_schema_generator*']),
    python_requires='>=3',
    zip_safe=False,
)
