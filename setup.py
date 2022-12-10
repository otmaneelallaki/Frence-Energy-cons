from setuptools import setup

setup(
    name="fecDv",
    version='0.0.1',
    description="France energy prediction",
    url="https://github.com/otmaneelallaki/Frence-Energy-cons",
    author="ELALLAKI,David,Sofian",
    author_email="otmane.allai1@gmail.com",
    license="MIT",
    packages=['fec','fec.src.xgboost','fec.src.louad_db'],
    zip_safe=False,
)