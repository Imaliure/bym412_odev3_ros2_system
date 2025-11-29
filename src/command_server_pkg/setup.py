from setuptools import setup

package_name = 'command_server_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/command_server_pkg/launch', ['launch/system_launch.py']),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aliure',
    maintainer_email='example@example.com',
    description='Command server package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'command_server = command_server_pkg.command_server_node:main',
        ],
    },
)
