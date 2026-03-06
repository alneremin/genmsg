from setuptools import setup

package_name = 'genmsg'

setup(
    name=package_name,
    version='0.6.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Dirk Thomas',
    author_email='dthomas@osrfoundation.org',
    maintainer='Troy Straszheim',
    maintainer_email='',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: BSD',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Standalone Python library for generating ROS message and service data structures for various languages.',
    license='BSD',
    # tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)