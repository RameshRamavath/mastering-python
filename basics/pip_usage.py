"""
pip --version

pip install <package name>

pip uninstall <package name>

pip search <package name>

pip list # get all the installed modules/packages

pip list -outdated  # check package latest version vs installed version for all the packages

pip install -U <package name>

*** provide list of packages we are using in our project to others - to run our code in their local env

option 1:  pip list   - manually copy down the list
option 2:  pip freeze  - this will give list of packages with version

            pip freeze > requirements.txt

*** how to install all the packages from requirement file

    pip install -r requirements.txt   # -r represents, requirements.txt file

"""
