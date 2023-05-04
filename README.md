NoCodeKings Senior Project

2. How to use our application:
Install VSCode

Clone our Github Repository which you should have access to we used:
Git: https://www.geeksforgeeks.org/how-to-install-git-in-vs-code/ (this article helps)

When Git is installed and connected to your GitHub account either by the article or in the VSCode terminal, clone the GitHub repository.
https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette This helps with what we did.

Move to step C once you can see our files in your VSCode instance.

At this point, we get into the Virtual Environment running. This will be a little hard to explain for us but we went ahead and installed it with: pipenv shell

After working on the .venv and running a script similar to this (& c:/Users/Trevor/Documents/GitHub/NoCodeKings/.venv/Scripts/Activate.ps1) we move on to installing Django, Requests and Plotly

Installing Django is done in the VSCode terminal by running: pip install django
Installing Requests is done by running: pip install requests
Installing Plotly is done by running: pip install plotly

3. Running the program:
Start the program after everything is installed and you are in the virtual environment with the code: python manage.py runserver
It should be accessible from: http://127.0.0.1:8000/
On the login page use the username ‘admin’ and enter the password ‘1234’
Enter into the Financials tab
Add a stock symbol in the designated area. (AAPL, GOOGL, TSLA)
You will see the information from the stock_info page
Click Chart to see the Candlestick chart generated from the Stock symbol inputted
That concludes the tutorial

