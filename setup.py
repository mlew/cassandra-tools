from distutils.core import setup

with open(u'requirements.txt') as f:
    required = f.readlines()

setup(
    name=u'cassandra-tools',
    version=u'0.1',
    author=u'Mark Lewandowski',
    author_email=u'mark.e.lewandowski@gmail.com',
    packages=[u'cassandratools'],
    scripts=[u'bin/cassandradump'],
    install_requires=required
)
