# specification-service


## Getting started

Create a postgres database for the application

    createdb standards_manager


Create a python virtualenv then run:

    make init

Copy .env.example to .env

Run any db migations

    make upgrade-db


Load specification/standards seed data

  flask data load

To run the application run:

    flask run

(you may see some errors on console due to inconsistencies in seed data)

If you need to reload seed data run:

  flask data drop && flask data load


To create new data migrations:

    flask db migrate -m "some message about the migration"


## Adding new python packages to the project

This project uses pip-tools to manage requirements files. [https://pypi.org/project/pip-tools/](https://pypi.org/project/pip-tools/)

When using fresh checkout of this repository, then make init will take care of the initial of packages from the checked
in requirements and dev-requirements files.

These instructions are only for when you add new libraries to the project.

To add a production dependency to the main application, add the package to the [requirements.in](requirements.in)
file.

To add a development library, add a line to [dev-requirements.in](dev-requirements.in).

Then run the piptools compile command using make:

    make reqs

That will generate a new requirements.txt file in the requirements directory.

Then to install all the packages run:

    make sync
