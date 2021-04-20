from setuptools import setup

setup(name='rabbitmq_models',
      version='0.2.0',
      description='General models for the Harmonium project',
      url='https://github.com/Enether/rabbitmq_models',
      author='Stanislav Kozlovski',
      author_email='familyguyuser192@windowslive.com',
      install_requires=['attrs==17.4.0',
                        'dateutils==0.6.6',
                        'pluggy==0.6.0',
                        'py==1.10.0',
                        'pytest==3.4.1',
                        'python-dateutil==2.6.1',
                        'pytz==2018.3',
                        'six==1.11.0'
                        ],
      packages=['rabbitmq_models'])
