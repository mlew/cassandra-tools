Cassandra-Tools
===============

This package is a set of tools for exporting cassandra data in different formats.

Installation
------------

To install cassandra-tools, simply:

    pip install -U -e 'git+ssh://git@git.ops.betable.com/betable/cassandra-tools.git#egg=cassandra-tools'

Or, for development:

    git clone git@git.ops.betable.com:betable/cassandra-tools.git
    cd cassandra-tools
    pip install -U -e .

Make sure you have python headers installed so you can compile the C extension for thrift.

    sudo apt-get install python-dev

