NoCodeKings Senior Project

1. How to use our application:

i. Install VSCode
ii. Clone our Github Repository which you should have access to we used:
Git: https://www.geeksforgeeks.org/how-to-install-git-in-vs-code/ (this article helps)

iii. When Git is installed and connected to your GitHub account either by the article or in the VSCode terminal, clone the GitHub repository.
https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette This helps with what we did.

Move to step (iv) once you can see our files in your VSCode instance.

At this point, we get into the Virtual Environment running. This will be a little hard to explain for us but we went ahead and installed it with: pipenv shell

iv. After working on the .venv and running a script similar to this aimed at your cloned repo location (& c:/Users/Trevor/Documents/GitHub/NoCodeKings/.venv/Scripts/Activate.ps1) we move on to installing Django, Requests and Plotly

v. Installing Django is done in the VSCode terminal by running: pip install django
vi. Installing Requests is done by running: pip install requests
vii. Installing Plotly is done by running: pip install plotly

2. Running the program:

i. Start the program after everything is installed and you are in the virtual environment with the code: python manage.py runserver
It should be accessible from: http://127.0.0.1:8000/
ii. Enter into the Financials tab
iii. Add a stock symbol in the designated area. (AAPL, GOOGL, TSLA)
iv. You will see the information from the stock_info page
v. Click Chart to see the Candlestick chart generated from the Stock symbol inputted
vi. That concludes the tutorial
