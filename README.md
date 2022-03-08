=====
Libary App
=====

Library App is a django  application that enables  a  crud operation using MVT architecture(django views and templates). It also exposes a Rest Framework API that enables a user to perform all crud operations as well. It also implents api authentication using jwt tokens


## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* virtualenv

### Cloning
* In your terminal:

        $ git clone https://github.com/Lourine/LibraryApp
        $ cd LibraryApp

## Running the Application
* Creating the virtual environment

        $ python3.8 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python
* Run pip3 install -r requirements.txt on your virtual environment
* Open psql shell and create Postgres database
* touch .env on your root directory and include all configs in .env.sample in your .env file
* Set MODE='dev' for your development environment.
* python manage.py migrate

* To run the application, in your terminal:

        $ python3.8 manage.py runserver

* Open the application on your browser `127.0.0.1:8000`.

## Testing the Application
* To run the tests for the class files:

        $ python3.8 manage.py tests

### To contribute to this project on any modules, follow these easy steps:

- Fork the repo
- Create a new branch in your terminal (git checkout -b improve-feature)
- Make appropriate changes in file(s)
- Add the changes and commit them (git commit -am "Improve App")
- Push to the branch (git push origin improve-app)
- Create a Pull request

## Contact Information 

If you have any question or contributions, please email me at [lourine.millicent@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2022 **Lourine Millicent*