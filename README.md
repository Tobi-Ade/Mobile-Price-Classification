# Mobile-Price-Classification

![Mobile Phones](http://koreabizwire.com/wp/wp-content/uploads/2020/07/thumb_2949993309_IAzvNfTX_01.jpg)

## Table of Contents 
1. [Problem Definition](#problem-defintion)
2. [Project Outline](#project-outline)
3. [How to Run the Project](#how-to-run-the-project)
4. [References](#References)
5. [Contact Me](#contact-me)

## Problem Definition
Claaifying prices of  devices for your mobile phone store is no easy feat. You have to take into account various features of a device and come up with a suitable price range. Doing this for every device is definitely a full time job! But what if we can just input the features of the device and get the price range automatically? Sounds cool!

In this project, we build a model that classifies the price-range of a mobile device based on it's features. The project covers everything from loading the data, to eventually deploying the model. By now we can tell that the price-range column is going to be our target column.
 
The dataset used for this project, as well as the description, can be found [here](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification?select=train.csv)


## Project Outline 
- [Jupyter Notebook](https://github.com/Tobi-Ade/Mobile-Price-Classification/blob/main/Mobile%20Price.ipynb)<br>
  Here we clean the data, carry out exploratory data analysis, train and tune different machine learning models and see how well they perform on the data
 
- [Training the Model](https://github.com/Tobi-Ade/Mobile-Price-Classification/blob/main/train.py)<br>
Here the final training occurs. We select the best model, and save it to a file so that it can be used on new data 

- [Creating a Flask App](https://github.com/Tobi-Ade/Mobile-Price-Classification/blob/main/predict.py)<br>
This is where we write a script for serving the model. We use the saved model to classify any new device when its features are sent to this flask app. 

- [Testing the service ](https://github.com/Tobi-Ade/Mobile-Price-Classification/blob/main/request.py)<br>
Here we write a script for testing our classification service. We send a request to the flask app and it returns the price range of the device.

- [Creating a Dockerfile](https://github.com/Tobi-Ade/Mobile-Price-Classification/blob/main/Dockerfile)<br>
- We create a virtual environment using docker and run our classificatiion service here.

## How to Run The Project
Please note that these steps are to be carried out in a terminal window like command prompt or git bash<br>
  - Clone the repository to your computer using:  <br>
  ```bash
  git clone https://github.com/Tobi-Ade/Mobile-Price-Classification.git
  ```
  <br>
  
  - Navigate to the directory where you cloned the repo and cd into the cloned repo by running: <br>
  ```bash
  cd Mobile-Price-Classification
  ```
  <br>
  You should now be in the project folder
  
  - The libraries used in this project can be found in the **requirements.txt** file. It is advisable to run this project in a virtual environment to avoid issues with your system configuration. To create a virtual environment with venv <br>
  ```bash
  python -m venv mobile-env
  ```
  
   Activate mobile-env with: <br>
   ```bash
   mobile-env\Scripts\activate.bat
   ```
   <br>
   
   Now install the libraries from the requirements.txt file by running:<br>
   
   ```bash
   pip install -r requirements.txt
   ```
   
   As we saw earlier, the model was already trained and saved in the train.py file. However, you may want to retrain the model for some reason. You do this by executing the file. In terminal, run:<br>
   ```bash 
   python train.py
   ```
   
  Now deploy the flask app locally by running the predict.py file. It is recommended to do this with a production server like waitress(windows OS) or gunicorn(UNIX).<br>
  You can still run it directly, with:   <br>
  ```bash
  python predict.py
  ```
  
  with waitress: <br>
 
  ```bash
  waitress-serve --listen=0.0.0.0:9696 predict:app
  ```
  
   with gunicorn: <br>
 
  ```bash
  gunicorn --bind 0.0.0.0:9696 predict:app
  ```
  
  Now the classification service should be running locally on "http://0.0.0.0:9696"
  
  Finally, you send a POST request to the service. You can do this by running the request.py file or use the file to understand the format in which the request will be sent, and then create your own request. This is how you run it:<br>
  ```bash
  python request.py
  ```
  
  You can also decide to build and run the Dockerfile for the project. To build this locally:
  ```bash
  docker build -t mobile_price_class .
  ```
  
  Then to run it:<br>
  ```bash
  docker run -it --rm -p 9696:9696 mobile_price_class:latest
  ```
  
  ### Cloud Deployment for this project is still in progress!
  
  
  ## References 
  - [ML Zoomcamp project criteria](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/projects)
  - [Data Source and Problem information](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification)
  - [Image source](http://koreabizwire.com/wp/wp-content/uploads/2020/07/thumb_2949993309_IAzvNfTX_01.jpg)
  - [Insurance Forecast by Carolina Dias](https://github.com/diascarolina/project-insurance-forecast)
  - [Learn Markdown](https://www.youtube.com/watch?v=bTVIMt3XllM&t=5s)
  - [Docker Hub Quickstart](https://docs.docker.com/docker-hub/)


 ## Contact Me 
 [<img src="https://img.shields.io/badge/tobi-ade-000000?style=flat-square&logo=github&logoColor=white" />](https://github.com/Tobi-Ade) [<img src="https://img.shields.io/badge/gabriel-adeleke-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/gabriel-adeleke/) [<img src="https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](mailto:themarveloustobi@gmail.com)
