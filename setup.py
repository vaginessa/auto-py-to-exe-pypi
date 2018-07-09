from io import open
from setuptools import setup

setup(
    name='auto-py-to-exe',
    version='1.2.0',
    url='https://github.com/brentvollebregt/auto-py-to-exe',
    license='MIT',
    author='Brent Vollebregt',
    author_email='brent@nitratine.net',
    description='Converts .py to .exe using a simple graphical interface.',
    long_description=open('README.md', encoding='utf-8').readlines()[1],
    keywords=['gui', 'executable'],
    packages=['auto_py_to_exe'],
    include_package_data=True,
    install_requires=['Eel>=0.9.9', 'pyinstaller'],
    python_requires='>=2.7,!=3.7.*',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'autopytoexe=auto_py_to_exe.__main__:run',
            'auto-py-to-exe=auto_py_to_exe.__main__:run'
        ],
    },
)