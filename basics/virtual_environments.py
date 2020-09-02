"""
Separate Python environments for diff projects -

* If two diff projects using diff versions of a particular package - then if we update that package in global site.packages
it may lead to prob's to older version based project

* install virtualenv
  pip install virtualenv # globally

* creating virtual environments

  mkdir Environments
  cd Environments

  -> ls

  virtualenv project1_env    # creates new Python executable in  project1_env/bin/python

* activate the env  - go to bin and activate

  source project1_env/bin/activate

* to check the current virtualenv
  -> which python

* write packages to requirements.txt - only from virtualenv

  -> pip freeze --local > requirements.txt

* come out of virtual environment

  -> deactivate


* remove the env and delete the folder

  -> rm -rf project1_env  # force remove the dir and files in it




"""