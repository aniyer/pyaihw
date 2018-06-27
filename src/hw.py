import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

def say():
    with open(os.path.join(dir_path, 'data', 'name.txt')) as fp:
        name = fp.read()
    print('Hello {}'.format(name))