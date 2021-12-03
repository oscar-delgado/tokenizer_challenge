# tokenizer_challenge #

This sample project contains a tokenizer. Basically, a tokenizer breaks a stream of text into tokens, usually by looking for whitespaces (including tabs, spaces, new lines, etc.). This version tokenizes any text and tries to recognize the language of a text (if it's clear).

### Installation and build ###

This project uses Docker for running locally, so you have to have installed Docker and docker-compose in your machine. 
For a local installation of the project, please follow these steps:
- Copy the file in dev/doker_settings.py in the folder tokenizer_challenge.
- Run the following command to build the project.
```bash
docker-compose build
```

### Run ###

For running the project locally, just run the following command.
```bash
docker-compose up
```
If you want to run it in Detached Mode (without seeing the container console), run the following command.
```bash
docker-compose up -d
```

### Test ###

For running the tests of the project, you have to enter to the web container running the following command. (Note that you have to have the container running. Follow the 'run' section above)
```bash
docker-compose exec web /bin/bash
```
Inside the container, you can run the following command to run all tests.
```bash
python3 manage.py test
```

### Description of the API ###

Once you have the container running, you can make GET requests to the following url. (Note that in the body you have to include a json object with the parameter 'text' with a string of the text to tokenize and, optionally, a parameter 'lang' with a string with the language in ISO Alpha2)
```bash
http://localhost:8000/api/tokenizer/
```
```json
{
    "text": "Text to tokenize locally",
    "lang": "en"
}
```


### Deployment to Heroku ###

Likely in the section above, you can make GET requests to the following Heroku url with the same parameters as in the last section.
```bash
http://tokenizer-challenge.herokuapp.com/api/tokenizer/
```
```json
{
    "text": "Text to tokenize in Heroku",
    "lang": "en"
}
```