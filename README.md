# Alphaline
Alphaline webscraper

This is a Django Rest Api application that takes input as company name and returns a json object containing the 
nseprice , bsepriice and the diffrence betwwen these prices for 1 min interval

For testing purpose chart2.html file is inlucded in the repository

Installtion steps to run the Application locally

pre-requisties
python version => 3.6
git

Steps for installtion

1) Clone the code from the repository or download zip:
    > git clone https://github.com/Harshad-Chavan/Alphaline.git
 
2) Create a virtual environment
    > cd Alphaline
    > python -m venv env
    
 3) activate the virtual environment:
    > cd env/scripts
    > acitvate
    
    for linux:
    # source env/bin/activate
    
4) Once virtual environment is activated
   
   (env) > pip install -r requrements.txt
   
5)Next steps to run the project
  > cd stockprice
  > python manage.py runserver (this will run the prject on a local host 127:0:0:0:8000)
    
    to run the project with different ip adn port
    python manage.py runserver <ip>:<port> (also change the url in chart2.html)
    
 6)Now open the HTML file Chart2.html to check the incoming data  
  
    
  



