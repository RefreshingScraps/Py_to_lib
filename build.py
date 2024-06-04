from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("random.pyx"),
    version='1.0',
    description='Random in Python for other language',
    author='Jiangmen NewCompany Co., Ltd.',
    author_email='YourFamily_00000000000000000023bffd864b3b20@groups.outlook.com'
)
