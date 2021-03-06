<div align="center">
<h1>Synthetiseur de texte</h1>
<blockquote>
<p><i>Synthétiseur de texte is a transcript-generating summarizer that aims to help students to create a comprehensive and concise summary of recorded lectures and save their time.</b></i></p>
</blockquote>
</div>
Live Working Demo: <a href="https://0dwf3qmn8j.execute-api.us-east-1.amazonaws.com/dev"> Website </a>


# Motivation
<i> During the global pandemic students attended online classes instead of physical classes.But due to network issues all were not able to follow what was being taught in the class. So to overcome this we came up with Synthetiseur_de_texte.Technology can never take place of the teacher but stil we tried to bridge the gap as much as possible.</i>

# Key features 
* **Recorded lectures** can be provided which are then converted into summary for quick **revision**.

* **Questions** are also generated from the summary to help better understand the lecture.

* If the recorded lecture is not available **youtube link** to the video can be provided.

# Screenshots


<div align="center"><i><h3>Upload file</h3></i></div>

![ss1](/website-1.JPG)




<div align="center"><h3><i>Copy UUID </i></h3></div>

![ss2](/webiste-2.JPG)




<div align="center"><h3><i>Summary and questions generated</h3></i></div>

![ss3](/website3.JPG)




# Technologies used
## Django and Python 
Django and python have been used to write the web app.
## NLTK Library
NLTK libraries have been used to **generate questions and summary**.
## AWS Services
- AWS Lambda - Used for deploying Web app (serverless architecture)
- AWS API Gateway - USed to route HTTP requests
- AWS RDS - Used to host MYSQL DB
- AWS Elastic File System - To hold the large sized binaries
- AWS VPC - For consolidating the various services and handling their interactions

# Running the project on local machine:
First clone the project to your local machine:
```
git clone https://github.com/arunav11/Synthetiseur_de_texte.git
```
Install the dependencies:
```
pip install -r requirements.txt 
```
Apply migrations to the database:
```
python manage.py makemigrations
python manage.py migrate
```
Now run the project:
```
python manage.py runserver
```

The project should be up and running on (http://127.0.0.1:8000)

# Deployment
```
# Update corresponding zappa settings in zappa_settings.json and run the following command
zappa update dev 

# For watching logs
zappa tail

# NOTE: Make sure your aws credentials are set in ~/.aws/credentials
```

## Testing 
Sample <a href="https://synthetiseur-de-texte-files.s3.amazonaws.com/files/sample.mp4"> file </a> has been provided for testing.
 
 
 
 Sample <a href="https://www.youtube.com/watch?v=beAvFHP4wDI&ab_channel=OneMinuteEconomics"> youtube link </a> has been provided for testing.
 
 


