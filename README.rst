===============================
configurer
===============================

.. image:: https://circleci.com/gh/jamielennox/configurer.svg?style=svg
    :target: https://circleci.com/gh/jamielennox/configurer

Intro
=====

Configurer is a reflection of the way I think about application configuration.

The Basics
==========

Configurer defines a prioritized pool of sources from which we can fetch configuration values.
We explicity define the options that we need for our application and then fetch them individually from this pool.


.. code:: python

    >>> import configurer
    >>> import configurer.validators
    >>> from configurer.readers.environ import EnvironmentReader

    >>> class MyComponent(configurer.Component):
    ...
    ...    my_val = configurer.Option('my_val',
    ...                               parser=str,
    ...                               validators=[
    ...                                   configurer.validators.Required()
    ...                               ])
    ...
    ...    def make(self):
    ...        return (self.my_val,)
    ...

    >>> conf = configurer.ConfigManager([EnvironmentReader('TEST')])
    >>> conf_creator = MyComponent(conf)
    >>> conf_creator.make()


For more information checkout the `docs`_.

The Pieces
==========

ConfigManager
-------------

The `ConfigManager` defines the options pool and the way that config values are retrieved.

Reader
------

A reader is a single source of configuration value. Multiple readers can be
attached to the same ConfigManager to provide fallback for options to multiple
places.

Option
------

An option is a single config option that we need for our application.

Component
---------

A component is a series of Options, it ties together options that are related
to each other, for example connecting to a database often requires a series of
options together. These will all come from the same configuration option namespace.

Parser
------

A parser translates the option value from the source type to the type expected
by your application. For many configuration sources (like Environment
variables, INI files) the values are always received as strings and we need to
convert it into things like an integer for port numbers, or split a string into
a list of items.

Validator
---------

Validate the config value to make sure it matches your expectations.

Reporting Bugs
==============

Development and bug tracking is performed on `GitHub`_.

License
=======

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.

.. _docs: https://configurer.readthedocs.io/
.. _GitHub: https://github.com/jamielennox/requests-mock
