Documentation

1. User Guide:

  a. Install VSCode

  b. Clone our Github Repository which you should have access to we used:
    i. Git: https://www.geeksforgeeks.org/how-to-install-git-in-vs-code/ (this article helps)

    ii. When Git is installed and connected to your GitHub account either by the article or in the VSCode terminal, clone the GitHub repository.
        https://learn.microsoft.com/en-us/azure/developer/javascript/how-to/with-visual-studio-code/clone-github-repository?tabs=create-repo-command-palette%2Cinitialize-repo-activity-bar%2Ccreate-branch-command-palette%2Ccommit-changes-command-palette%2Cpush-command-palette This helps with what we did.

     iii. Move to step C once you can see our files in your VSCode instance.

   c. At this point, you will use pipenv shell to initialize and run the virtual environment through which the webpage will run through.

   d. After working on the .venv and running a script similar to this (& c:/Users/Trevor/Documents/GitHub/NoCodeKings/.venv/Scripts/Activate.ps1) we move on to installing Django, Requests and Plotly

     i. Installing Django is done in the VSCode terminal by running: pip install django
     ii. Installing Requests is done by running: pip install requests
     iii. Installing Plotly is done by running: pip install plotly

2. Running the program:
  a. The actual program is in the master branch, switch over to it if needed.
  
  b. Start the program after everything is installed and you are in the virtual environment with the code: python manage.py runserver
  
  c. It should be accessible from: http://127.0.0.1:8000/
  
  d. On the login page use the username ‘admin’ and enter the password ‘1234’. Alternate sign in is the username “admin” and password “1234”.
  
  e. Select the Financials tab
  
  f. Add a stock symbol in the designated area. (AAPL, GOOGL, TSLA, etc.)
  
  g. You will see the information from the stock_info page
  
  h. Click Chart to see the Candlestick chart generated from the Stock symbol inputted (There are many features to play around with here)
  
  i. Use the back arrow to move back to the homepage from the Financials page.
  
  j. Select the Accounts tab to view account information logged into the database.
  
  k. Select the blue hyperlinks to view further account information.
  
  l. Use the browser back arrow to navigate back to the home page.
  
  m. Select “log out” at the top right of the screen.
  
  n. This concludes the tutorial
  
	**DISCLAIMER: There are a few bugs in our systems. If you enter a string that is not found within our API then an error page will appear (Just click the browser back arrow to return to previous page). The “Invalid Symbol” message only appears when a non ‘US’ company is inputted and is present in our API. This is due to our API version. When the “Invalid Symbol” message appears, it will not go away unless the program is completely reset. 




3.Testing:
  We put our software through continuous testing during the implementation, which uncovered several issues such as bugs, software failures, and crashes. Despite encountering these challenges during testing, we kept testing during implementation and continued to make improvements to the code until we arrived at the current version of our product. We are still in the testing phase as we continue to add and change new features to make them better.
  For example, we recently identified a problem where attempting to enter tickers not present in the database caused the app to crash. To address this issue, we developed a redirect page that displays a prompt informing the user that the ticker is not available. We will continue to test as we add new features.
  We are currently white box testing our product. This means we are in the process of code review. This entails us looking for flaws visually and vulnerabilities the software may contain. On top of this, we are also doing integration testing. This entails individually testing software components to ensure they are working with previous sets of working code and continuing forward. This ensures we do not commit code not knowing at what stage it has been broken. This has been saving us time on the troubleshooting side when trying to correct code. 
  We also have members of the team working on simple black box testing. This entails loading up the website and entering inputs and documenting the outputs. The goal is to see what breaks the website so we can later go back and revise our code. 
