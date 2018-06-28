from distutils.core import setup

setup(
    name='PyAIHW',
    version='0.3',
    license='',
    long_description=open('README.txt').read(),
    packages = ['pyaihw',],
    package_data = {
        # include all python source code
        '': ['*.py'],
        # include any datafiles
        'pyaihw': ['data/*.txt'],
    },
    install_requires=[
        'tqdm'
    ]
)
