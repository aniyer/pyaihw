from distutils.core import setup

setup(
    name='PyAIHW',
    version='0.2dev',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    packages = ['pyaihw',],  # include all packages under src

    package_data = {
        # If any package contains *.txt files, include them:
        '': ['*.py'],
        # And include any *.dat files found in the 'data' subdirectory
        # of the 'mypkg' package, also:
        'pyaihw': ['data/*.txt'],
    }
)
