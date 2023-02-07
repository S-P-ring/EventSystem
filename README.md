# EventSystem
>what it's about?
###This is an implementation of a simple event management application in which post requests come in.
>Installing

###git clone <repo>
cd <repo>
pip install virtualenv (if you don't already have virtualenv installed)
virtualenv venv to create your new environment (called 'venv' here)
source venv/bin/activate to enter the virtual environment
pip install -r requirements.txt to install the requirements in the current environment

1.Don't forget to create migrations and apply them(in particular, to generate a table of tokens).
2.Create a user, then sign in to create a token.
3.After that you can use this user to send post requests
