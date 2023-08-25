## Hello Auth0
Example project for getting started with FastAPI and Auth0.

### Prerequisites
- [x] [asdf](https://asdf-vm.com)
- [x] [direnv](https://direnv.net)

### Local Setup
- define python version
```shell
asdf local python 3.11.4
```
- create and activate your venv
```shell
pip install pipenv
pipenv install --dev
```
- prepare config
```shell
cp .envrc.dist .envrc
cp local.env.dist local.env
# substitute config values while going through auth0 setup
```

### Running Locally
```shell
python server.py
```

### Auth0 Setup
TBD

#### Links
- https://community.auth0.com/t/invalid-access-token-payload-jwt-encrypted-with-a256gcm/77893
