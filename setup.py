from setuptools import setup, find_packages

setup(
   name='nekoslife',
   version='0.0.1',
   author='Blank-c',
   packages=find_packages(),
   url='https://github.com/Blank-c/NekosLife',
   description='An unofficial wrapper for nekos.life api with proxy support.',
   long_description=open('README.md').read(),
   long_description_content_type='text/markdown',
   install_requires=['aiohttp'],
   keywords='nekoslife'
)
