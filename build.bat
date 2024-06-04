@echo off
pip install cython
pip install setuptools
pip install distribute
python build.py build_ext --inplace
pause
