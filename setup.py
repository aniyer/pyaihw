from distutils.core import setup

setup(
    name='PyAIHW',
    version='0.2dev',
    license='',
    long_description=open('README.txt').read(),
    packages = ['src',],
    package_data = {
        # include all python source code
        '': ['*.py'],
        # include any datafiles
        'src': ['data/*.txt'],
    },
    install_requires=[
        "tqdm"
    ]
)
