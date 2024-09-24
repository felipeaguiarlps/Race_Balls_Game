from setuptools import setup, find_packages

setup(
    name='random_map_simulation',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'random-map-sim=random_map_simulation.game:play_game',
        ],
    },
)
