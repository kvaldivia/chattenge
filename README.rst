Chattenge
=========

The chat challenge

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: BSD

Setup
--------

Environment files
^^^^^^^^^^^^^^^^^^^^^
* IMPORTANT! Extract the .envs directory in the project's root.


Starting up containers
^^^^^^^^^^^^^^^^^^^^^

* This project's been built using docker-compose, so getting all services up and running is pretty easy. Run the following::

  $ docker-compose -f local.yml up -d


Setting up RabbitMQ
^^^^^^^^^^^^^^^^^^^^^

* We need to setup rabbitmq from the command line, you can find the commands in `compose/local/rabbitmq/create-main-channel.sh`. Run the following::

    $ rabbitmqctl add_user $MAIN_USER $MAIN_USER_PASSWORD
    $ rabbitmqctl add_vhost $MAIN_VHOST
    $ rabbitmqctl set_permissions -p $MAIN_USER $MAIN_VHOST ".*" ".*" ".*"
    $ rabbitmq-plugins enable rabbitmq_web_stomp

Setting Up Sample Chatrooms
^^^^^^^^^^^^^^^^^^^^^
* To create sample chatrooms (i.e. predefined chatrooms), you can run the following command::

  $ create_sample_chatrooms

* The rabbitmq management ui is available at port 15672.


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Superuser
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy chattenge

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html



Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd chattenge
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.




Email Server
^^^^^^^^^^^^

In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``

.. _mailhog: https://github.com/mailhog/MailHog



Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html



