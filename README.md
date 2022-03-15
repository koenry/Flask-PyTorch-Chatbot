[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)](https://www.python.org/)
[![Torch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![Numpy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.0.x/)
[![JS](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![NGINX](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)](https://www.nginx.com/)
[![DigitalOcean](https://img.shields.io/badge/Digital_Ocean-0080FF?style=for-the-badge&logo=DigitalOcean&logoColor=white)](https://www.digitalocean.com/)
[![CAO](https://codeacademy.lt/wp-content/themes/codeacademy/dist/images/codeacademy-black.svg)](https://codeacademy.lt/)
# ChatBot (Beta version 1.0)

  My final project for [CodeAcademyLT](https://codeacademy.lt/)   programming course. A trained chatbot model with pytorch and flask.

# Table of Contents
1. [Plan](#Plan)
2. [How does it work?](#How-does-it-work)
3. [The Model](#The-Model)
4. [Intents](#intents)
5. [Requirements](#Requirements)
6. [Usage](#Usage)
7. [Deployment](#Deployment)
8. [Author Notes](#Author-Notes)
9. [Future Roadmap](#Future-Roadmap)

# Plan:
1. Learn various NLP concepts: Stemming, Tokenization, Bag of words
2. Create train data
3. Create a pytorch model and train the model
4. Save and load the model and implement the chat
5. Implement front-end
6. Fix bugs and Refactor the code
7. Enable CORS policy, create a dockerfile for the server build
8. Deploy


# How does it work?

* Tokenization - a method to split a sentence into tokens or words
    ``` what would you do? ```   ``` "what" "would" "you" "do" "?" ( string of words become an array )  ```  
* Stemming - is the process of reducing inflection in words to their root forms such as mapping a group of words to the same stem even if the stem itself is not a valid word in the Language.
 ```organize organizes organizing ```   ```organ organ organ   ```
 Though it might lose meaning : universe university - univers univers
 * Bag Of Words - is a representation of text that describes the occurrence of words within a document. (intents.json)
These are called ``` (NLP) - Neuro-linguistic programming ```  techniques  
* Lower all the words and exclude special characters
* Compare with Bag of words (intents.json)
* Calculate the probability - x vector

# The Model
input =>  'is anYone thErE?' \
tokenization => 'is' 'anYone' ''thErE' '?' \
stemming => 'is' 'anYon' 'thErE' '?' \
lower all words => 'is' 'anyon' 'there' '?' \
exclude special characters => 'is' 'anyon' 'there' \
bag of words (intents.json) =>  ```'is' 'anyon' 'there'```        intents.json``` 'are you there' 'is anyone here' ```  \

| bag of words    | input           | probabilities  |
| ------------- |:-------------:| -----:|
| are you there      | is' 'anyone' 'there | 001 |
| is anyone here     | is' 'anyone' 'there     |  110  |
|is there anyone| is' 'anyone' 'there      |  100   |
#####
 apply bag of words
  for each different pattern 
  if this word is included in the pattern 
  we put a 1 or 0 otherwise
  Patterns: ```hi how are you``` => greeting
```bye see you later``` => goodbye


# Intents

![image](https://user-images.githubusercontent.com/68077710/149459532-08d0375e-2f5f-4de1-b3c6-361fda404bd7.png)


```tags``` is the subject \
```patterns``` This is where the bot searches for patterns \
```responses``` This is how the bot will response using random module so its not the same response \


### We get the x  vector and it calculates which 'tag' is correct is it a greeting? a goodbye? a specific question?
Of course we might not get an answer we want because its not in our intents.json so if lets say the probabality is less than 0.75 we use duckduckgo API to search the web for an answer
If the user types in 'Keanu Reeves' it gives us a summary that its an actor. So the bot pretty much haves an answer to any user input.

# Requirements
```pip install nltk``` \
```pip install numpy``` \
```pip install torch``` \
```pip install flask``` \
```pip install flask-cors``` \
```pip install requests``` \
note: you might need to ```import nltk.download('punkt')``` its a tokenizer package inside train.py, its commented out but you might need it to manually* download it you need to run it only once. *By mnually I mean to uncomment and run the train data once afterwards you can comment it out.

# Usage
* Download the code \
![image](https://user-images.githubusercontent.com/68077710/149556782-c6cf4e8a-2072-4a0f-bb45-004994115858.png)

* pip install -r requirements.txt ( in the shell )
![image](https://user-images.githubusercontent.com/68077710/149461757-7c18885d-697d-4abc-be51-78eaf21dda27.png)

* run train.py this will train your data and save it to pickle file for your model.py to use \
 ![image](https://user-images.githubusercontent.com/68077710/149461833-94c26e44-2715-4d43-b1db-0c3979b4ddd6.png)

* run run.py to start the development server \
 ![image](https://user-images.githubusercontent.com/68077710/149461870-428c4bf5-f3b0-4568-9589-915afc1827e1.png)

* go to [localhost:5000](http://127.0.0.1:5000/)
* Start Typing! \
![image](https://user-images.githubusercontent.com/68077710/149461951-b7b1e300-d359-4866-a21a-1fd3b07045d4.png) \
```p.s. the front-end design is still in early alpha```

### Quick Notes
* You can always use your own intents.json and run train.py (just delete the data pickle file from the root folder if you ran train.py )
* This is an open source project so you can use it anywhere you want \

# Deployment
I have created a Docker image for this app to deploy to DigitalOcean. The image can be found here: https://hub.docker.com/r/koenry/chatbot \
I have used NGINX for a reverse proxy. \
This was my first time trying to deploy an app to Docker. I have learned quite a bit about nginx and docker while preparing the image.

### Docker Instructions
* use docker pull koenry/chatbot to get the image 
* docker run -dt -p 80:80 -p 5000:5000 --name NAME koenry/chatbot      -- to create a process
* docker exec -it NAME bash      -- to get into the container
* Inside the contained start chatbot.ini and nginx:  systemctl restart nginx && systemctl restart chatbot
* Enter your server IP to your browser


# Author Notes
*I Learned the proper way how to import functions and not use one .py file for everything 
* One of the best helping hand was: ```I Learned that  Everything in python is considered as object so functions are also objects.``` So you can use this method as well.
Lets say chat.answerBot = 'ok' and when I import the function I can easily call it chat.answerBot or we can even call local scope variables this is where OOP really shines.
* Learned how back-end and front-end communicates via GET and/or POST requests.
* Started using f strings for better readabiltiy of concat strings.
* Read more about machine learning and how an AI is trained

# Future Roadmap

* update intents.json
* Implement Jenkins/GithubActions for CD/CI 
* Try  implementing sentiment analysis
