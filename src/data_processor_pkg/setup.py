from setuptools import setup

package_name = 'data_processor_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aliure',
    maintainer_email='example@example.com',
    description='Data processor package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'data_processor = data_processor_pkg.data_processor_node:main',
        ],
    },
)
