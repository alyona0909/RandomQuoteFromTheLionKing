# Random Quote From The Lion King
A free site to generate a random quote from The Lion King cartoon.

http://lionkingquotes.pythonanywhere.com/

## Getting Started
Before using you need to install :

```sh
pip install -r requirements.txt
```

## How to use

### Data collection:
You can use script `read_quotes.py` to collect data from site : http://itmydream.com/citati/mult/korol-lev-the-lion-king/1. The result is two files : `result.csv` and `result.txt`.

To choose random quote you can use script `choose_phrase.py` with fucntions for all heroes and for each picked hero.

### For local server:
To launch it from the local server you need:

```sh
set FLASK_APP=server.py
python -m flask run
```
