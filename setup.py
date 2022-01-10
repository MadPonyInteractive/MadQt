import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='MadQt',
    version='0.0.31',
    description='Tutorials and Tools for PySide',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/MadPonyInteractive/MadQt',
    author='Fabio Goncalves',
    author_email='fabiogoncalves@live.co.uk',
    license='MIT',
    install_requires=['PySide6 >=6.0.0',# we need it to be able to compile resources
                      'Pillow >= 8.3.0',
                      'pyinstaller >= 4.7'
                     ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Natural Language :: English',
        'Topic :: Desktop Environment',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: Education',
    ],
    # scripts=['scripts/MadQt-rcc'],
    entry_points={
        'console_scripts': [
            'MadQtProjectManager=MadQt.scripts.ProjectManager:main',
            'MadQtPluginCreator=MadQt.scripts.PluginCreator:main',
        ],
    },
    include_package_data=True,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",  
)
