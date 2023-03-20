from setuptools import setup, find_packages


setup(
        name='pptract',
        version='1.0.0',
        py_modules=['pptract'],
        install_requires=find_packages(),
        entry_points={
            "console_scripts": ['pptract = pptract:run']
        }
)
