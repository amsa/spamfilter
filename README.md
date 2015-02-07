# Spam Filter

This is a simple spam detection API implemented using Django which can easily be deployed to Heroku.

This way a list of messages is passed to the endpoint, and you will get a list back 
in the same order. Each value in the returned list is either 1 if the corresponding 
text is spam and 0 otherwise.

Sample:
```sh
curl -X POST -d 'text=EMAIL_BODY1&text=EMAIL_BODY2' http://127.0.0.1:5000/
```

Output:
```
[0, 1] # it means EMAIL_BODY1 is not a spam, but EMAIL_BODY2 is spam
```

## Running Locally

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started
$ pip install -r requirements.txt
$ python manage.py syncdb
$ foreman start web
```
Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create --buildpack https://github.com/thenovices/heroku-buildpack-scipy
$ git push heroku master
$ heroku run python manage.py syncdb
$ heroku open
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

