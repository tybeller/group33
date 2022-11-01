# group33

# How to install the python environment

Run the following commands:  
  
Install the venv package  
`pip3 install venv`  
  
Create a virtual environment named venv  
`python -m virtualenv venv`  
  
Import the necessary packages (ones listed in requirements.txt) into the virtual environment  
`pip3 install -r requirements.txt`  
  
Check the packages are installed correctly  
`pip list --local`  
  
** Optional **  
Upgrade version of pip  
`python.exe -m pip install --upgrade pip`  

# How to setup PyMongo/MongoDB
1. Acquire the MongoDB connection string from Kevin.
2. Put the connection string in config.json.
3. Run pymongo_example.py to verify if setup was successful.

