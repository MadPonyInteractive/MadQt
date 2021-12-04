from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='MadQt',
    version='0.0.1',    
    description='Tutorials and Tools for PyQt and PySide',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/MadPonyInteractive/MadQt',
    author='Fabio Goncalves',
    author_email='fabiogoncalves@live.co.uk',
    license='MIT',
    install_requires=['PyQt>=6.0',
                      'PySide>=6.0',                    
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Natural Language :: English',
        'Topic :: Desktop Environment',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: Education',
    ],
    package_dir={"": "MadQt"},
    packages=setuptools.find_packages(where="MadQt"),
    python_requires=">=3.9",  
)
