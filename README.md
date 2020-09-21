<div align="center">
<h1>Synthetiseur_de_texte</h1>
<blockquote>
<p><i>Synthétiseur de texte is a transcript-generating summarizer that aims to help students to create a comprehensive and concise summary of recorded lectures and save their time.User can either upload a lecture video or audio file or can enter a youtube video link to get the summary and probable questions.</b></i></p>
</blockquote>
</div>


# Key features and technologies
## Django and python 
Django and python have been used to write the web app.
## NLTK
NLTK libraries have been used to **generate questions and summary**.

# Running the project on local machine:
First clone the project to your local machine:
```
git clone https://github.com/arunav11/Synthetiseur_de_texte.git
```
Install the dependencies:
```
pip3 install -r requirements.txt (Python 3)
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

##Testing 
Sample **file** have been provided for testing.
 https://synthetiseur-de-texte-files.s3.amazonaws.com/files/sample.mp4
 Sample **youtube link** have been provided for testing.
 https://www.youtube.com/watch?v=beAvFHP4wDI&ab_channel=OneMinuteEconomics
