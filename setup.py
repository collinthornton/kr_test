from setuptools import setup

package_name = 'kr_test'

sources = ['gen_traj.py', 'position_traj.py', 'velocity_traj.py']

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('lib/' + package_name, [package_name + "/" + name for name in sources]),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Collin Thornton',
    maintainer_email='collin.thornton@swri.org',
    description='Test the ROS2 CBun for the Kassow KR1410 robotic manipulator',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'position_node = kr_test.position_node:main',
            'velocity_node = kr_test.velocity_node:main'
        ],
    },
)
