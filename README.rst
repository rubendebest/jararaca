Jararaca
========

Goal
----

Bootstrap `Amazon SQS <https://aws.amazon.com/sqs/>`__ and `Amazon
SNS <https://aws.amazon.com/sns/>`__ like a breeze.

Requirements
------------

-  Python 3
-  AWS Account

Installation
------------

1. Get the code

.. code:: bash

    $ cd <your_projects_folder>
    $ curl -L -o jararaca.zip http://github.com/rubendebest/jararaca/zipball/master/
    $ unzip -j jararaca.zip -d jararaca

2. Using a virtual environment is encouraged. Create it.

.. code:: bash

    $ python3 -m venv butantan
    $ source butantan/bin/activate
    $ cd jararaca 
    $ pip3 install -Ur requirements.txt

Usage
-----

Run it to see options:

.. code:: bash

    $ ./jararaca.py

Development
-----------

Run ``nosetests --rednose`` to run tests. It works when run at the root
directory.

Running ``nosetests --rednose --with-watch`` will run tests whenever a
``.py`` file is saved.

References
----------

-  `venv <https://docs.python.org/3/library/venv.html>`__
-  `reStructuredText <http://docutils.sourceforge.net/rst.html>`__
