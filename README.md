# Spam Filter

This is a simple spam detection API implemented using Django which can easily be deployed to Heroku.

The API accepts an array of texts as input, and returns an array back 
in the same order with values being either 1 for spam or 0 for ham.

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
$ pip install -r requirements.txt
$ python manage.py syncdb
$ foreman start web
```
Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create --buildpack https://github.com/thenovices/heroku-buildpack-scipy
$ git push heroku master
$ heroku open
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)

