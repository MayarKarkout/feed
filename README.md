# Django feed app

Django feed app is an app written in Python with the Django framework for calculating the number of items in an XML RSS feed.
It also calculates the number of items in stock and groups items by their labels.

## Installation

Clone the repository locally.
```bash
git clone https://github.com/MayarKarkout/feed.git
```
Go to the root folder and install the requirements.
```bash
pip install -r requirements.txt
```
Make sure to add a default secret key in ```settings.py```.
```python
SECRET_KEY = os.getenv('SECRET_KEY', 'some-default-value')
```

## Check it out online

Go to https://feed-br.herokuapp.com/ for the hosted version of the app.

## Usage

Paste a link to a well-formatted XML link and click 'Submit input'.
Eg. https://feed.hitspot.media/rajapack.xml


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)