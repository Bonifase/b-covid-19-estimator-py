# #BuildForSDG Cohort-1 Python Assessment

> Build an overly simplified COVID-19 infection impact estimator

This is an eligibility assessment for the 2020 [#BuildforSDG](https://buildforsdg.andela.com/) program

The assessment empowers me to **attempt** helping society and leaders prepare for the **real big problem** of COVID-19, which is **its impact on lives, health systems, supply chains, and the economy**:

> 1.  Too many patients, not enough hospitals and beds. A serious shortage of ventilators, masks and other PPE - if _we don’t practice social distancing_.
> 2.  Job losses or freezes, low cash flow and low production (even for essentials like food). These and more from too many people being sick, a sizable number dying (including some of the best people in many fields), and many others affected by the impact of losing loved ones or a world operating in slow motion

## How To Proceed

### Project Setup & Submission Process

> Go to [this Google Drive](https://drive.google.com/drive/u/0/folders/132af5VHpYX5LDTzqQETThXpDpw6Q6jRv) for guides on [how to setup your project](https://drive.google.com/file/d/1izTv3RdKwJf2V0RsarRc2ULDemKEAC16/view), take the assessment in one of the supported programming languages (Javascript, Python, or PHP), and how to submit your work. Make sure you read the instructions carefully, because missing a step might cost you in the long run.

---

## The backend API

A simple REST API built around the estimator function and hosted on Heroku service.

It is implemeted using **Flask** and the whole functionality resides in the **app.py** file.

The REST API allows a user make a HTTP POST request, providing the data
normally passed to the estimator function, and get back the estimation data produced by the estimator function.
Specifically, the API has the following endpoints:

- /api/v1/on-covid-19 endpoint that takes the input data and return the default estimation for it in a JSON format.
- /api/v1/on-covid-19/xml which produce the response in XML format.
- /api/v1/on-covid-19/json which produce the response in JSON format.
- /api/v1/on-covid-19/logs which produce the HTTP request/response logs in string format.

### To run the API

Install virtual environment, activate it and in the root directory run pip install to install additional packages.

Simply run **python app.py** in the terminal to have the API up and running.
