from setuptools import setup, find_packages

setup(
    name='slider_mp',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/chagama-g/slider_mp',
    license='MIT License',
    author='chagama-g',
    author_email='55901504+chagama-g@users.noreply.github.com',
    description='multiprocessing によってnon-blockingな Slider を表示する',
    install_requires=["matplotlib"]
)
