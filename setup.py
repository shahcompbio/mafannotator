from setuptools import setup, find_packages
import versioneer

setup(
    name='mafannotator',
    packages=find_packages(),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='anno maf',
    author='Douglas'
    #entry_points={'console_scripts': ['single_cell = single_cell.run:main']}
    #package_data={'':['scripts/*.py', 'scripts/*.R', 'scripts/*.npz', "config/*.yaml", 'scripts/*.Rmd', 'scripts/*.sh', "data/*"]}
)
