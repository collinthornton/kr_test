from setuptools import find_packages, setup

package_name = 'kr_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        (f'share/ament_index/resource_index/packages', [f'resource/{package_name}']),
        (f'share/{package_name}', ['package.xml']),
        (f'share/{package_name}/hook', [f'resource/ros_package_path.dsv'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Collin Thornton',
    maintainer_email='collin.thornton@swri.org',
    description='Test the ROS2 CBun for the Kassow KR1410 robotic manipulator',
    license='BSD',
    tests_require=['pytest'],
    scripts=[
        'scripts/position_node.py',
        'scripts/velocity_node.py'
    ]
)
