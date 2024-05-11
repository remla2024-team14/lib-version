from setuptools import setup, find_packages

setup(
    name='team-14-lib-version',
    use_scm_version={'root': '.', 'relative_to': __file__, 'write_to': 'src/version.py',
                     },
    setup_requires=['setuptools_scm'],
    packages=find_packages(),
    description='version aware library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Team 14',
    author_email='justinluu2000@gmail.com',
    url='https://github.com/remla2024-team14/lib-version',
    install_requires=[
        'flask',  'flask-cors'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)