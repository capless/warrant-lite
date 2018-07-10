# warrant-lite
Small Python library for process SRP requests for AWS Cognito. This library was initially included in the [Warrant](https://www.github.com/capless/warrant) library. We decided to separate it because not all projects and workfows need all of the helper classes and functions in Warrant.

## Install

```python
pip install warrant-lite
```

## Usage

```python
from warrant_lite import WarrantLite


wl = WarrantLite(username='username', password='password',
                          pool_id='pool_id',client_id='client_id', 
                          client_secret='client_secret')

tokens = wl.authenticate_user() #client is an optional (keyword) argument

#Verify Tokens
wl.verify_token(tokens['AuthenticationResult']['AccessToken'], 'access_token', 'access') #Access Token example


```
