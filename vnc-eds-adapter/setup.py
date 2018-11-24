from setuptools import setup, find_packages

setup(
    name='vnc-eds-adapter',
    description='Displays the content of a vnc session on an e-paper display',
    author='Carla Iten, Diego Bienz, Michael Blättler, Philipp Leu',
    version='0.1.0-dev',
    install_requires=['pillow', 'spidev', 'vncdotool'],
    packages=find_packages(),
    license='MIT',
    entry_points={
        'console_scripts': [
            'vnc_eds = vnc_eds.main:main'
        ]
    },
    long_description=open('README.md').read()
)
