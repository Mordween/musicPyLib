from setuptools import setup

setup(
    name='musicPyLib',
    version='1.0.0.dev1',
    description='petite librairie pour télécharger des musiques/playlist directement de Youtube',
    author='Alexandre Ridolfi',
    author_email="al.ridolfi@laposte.fr",
    packages= ['musicPyLib'],
    install_requires=[
        'tk >= 8.6.12',
        'pytube >= 15.0.0' 
    ],
)
