from setuptools import setup

package_name = 'people_detector'


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/people_detection.py']),
        ('share/' + package_name, ['data/yolov8n.pt']),
        ('share/' + package_name, ['data/video.mp4'])        

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robot',
    maintainer_email='robot@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'video_publisher = people_detector.video_pub:main',
        	'people_detect_subscriber = people_detector.people_detect:main',
        ],
    },
)
