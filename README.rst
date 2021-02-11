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

3. Configure your AWS account settings

- Credentials ``~/.aws/credentials``:

.. code-block:: ini

    [default]
    aws_access_key_id = YOUR_KEY
    aws_secret_access_key = YOUR_SECRET

- Default region ``~/.aws/config``:

.. code-block:: ini

    [default]
    region=us-east-1


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
- ` boto3 (the AWS SDK for Python) <https://boto3.readthedocs.io/en/latest/>`__
-  `reStructuredText <http://docutils.sourceforge.net/rst.html>`__

How to Contribute
-----------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _`the repository`: http://github.com/rubendebest/jararaca
.. _AUTHORS: https://github.com/rubendebest/jararaca/blob/master/AUTHORS.rst