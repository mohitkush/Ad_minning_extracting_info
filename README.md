# AdEase_task
Machine Learning Engineer  Internship Task 

## Step by Step process to run the programs:
1. Clone the repository ``` git clone https://github.com/mohitkush/AdEase_task.git ```
2. Create new python virtual enviornment ``` python3 -m venv /path/to/new/virtual/environment ```
3. Activate the newly created python enviornment ```source venv/bin/activate```
4. Install all the required python libraries from using ``` python3 -m pip install -r requirements.txt```
5. Now if you want to run the program in jupyter notebook [suggested], install libraries from requirements.txt in your local python server and run ```jupyter notebook``` on your terminal (make sure jupyter notebook is added in your PATH)
6. Otherwise if you want to run the .py files type ```python3 ad_scrape.py``` and ```python3 model.py``` for the respective files.
7. Details regarding the input output for both the files are discussed below

## ad_scrape.py/ad_scrape.ipynb
python program to scrape ads from two webpages, https://www.speedtest.net/ and https://www.forbes.com. This file takes no input, I have hard-codded the two webpages, it returns the scrapped ads in the ```./Scraped_ads/{webpage}.jpg``` format

## model.py/model.ipynb
python program to extract text, logo and the call of action button. see some example below:
For Samsung ad:


## Scraped_ads
This directory contains the scraped ads from the above mentioned websites. You can run the model.py on these ads to check if the model is working fine.
