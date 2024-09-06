# Hack Reactor Token Scrape

This is a script for those taking the Hack Reactor bootcamp. If you are a student, this script will log you in, 
go through the steps to get to where the token drops and then will scrape the page looking for the token to pull 
it and submit it on your behalf. You will of course need to adjust a few things in the script for it to work for 
you but they are minor. This is also running on a 64-bit update and not a 32-bit. It was the first full piece of 
code I ever wrote so there are adjustments that could be made I am sure. I encourage you to play with it and try 
to make a better script!

## Initialization

### Requirements

You will need to be familiar with an IDE of your choice. I utilize VSCode. I also run my terminal outside of my 
IDE but that is personal choice. Some familiarity with Python is necessary and I HIGHLY recommend you take the 
time to look through the script to understand what is actually happening. 

### Steps

Follow these steps to run your own script. Just copy and paste everything!

- Open your IDE of choice
- Create a new directory for this script
- Run your terminal of choice in that directory
- At this point there shouldn't be anything in the directory yet!
- Go ahead and create your virtual enviornment:
    **For windows:**
  - python -m venv .venv
  - .venv\Scripts\activate

    **For macOS:**
  - python -m venv .venv
  - source ./.venv/bin/activate

- In your directory, make a new file called requirements.txt and copy and paste the requirements.txt from here
- In your activated virtual environment that you just created, run:
  - python -m pip install --upgrade pip
  - pip install -r requirements.txt

- In the directory, also copy and paste the main.py file into your own
- Change your email, password, and cohort number. This script shows 143 for my cohort so you'll want to change that number.

- Once all that is changed you should be good to run the script in your terminal! Run: python main.py
- Deactivated your terminal when the token has been submitted.

### Notes

I usually started the script about 5 minutes before the token drop so I could get settled without worrying about 
it. Depending on where you are located from the servers will depend on how quickly it submits. There were only 2 
of us in my cohort that wrote scripts and the other girl did hers differently. She was also closer to the server so
beat out my script even after adjusting it. Good luck and happy coding!
