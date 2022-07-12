import setuptools

setuptools.setup(name='my-package-20CS10019',
                 version='1.0',
                 description='Python DS assignment',
                 author='KV',
                 packages=setuptools.find_packages(),
                 install_requires=['torch',
                                   'torchvision',
                                   'matplotlib',
                                   'Pillow',
                                   'numpy']
                 )
