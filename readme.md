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

#### Access the Tenet
- create your free tier tenet on the [Auth0](https://auth0.com) website

#### Define the API
- under Applications / APIs create a new API which defines your backend endpoints
  - name: example-dev
  - identifier: https://api-dev.example.company.org
  - signing algorithm: RS256
- define permissions for the API
  - read:messages - read messages
  - write:messages - write messages
- review permission settings
  - enable Role Based Access Control (RBAC)
  - optionally, enable the permissions claim for the access token
  - optionally, allow offline access
    - this would be needed to implement token refresh
- review machine-to-machine applications
  - auth0 automatically creates a test application when you create the API
  - for this project we don't need the test application
  - so you can the test application and access, and eventually delete the unused application
- review general settings
  - the default token expiration is 24 hours
  - allow skipping user consent is enabled by default

#### Create the Client Application
- create the application
  - name: Example (SPA)
  - type: Single Page Application
- define the allowed callback urls
  - for starting out you can use the following for local development
    - http://localhost:8000/docs/oauth2-redirect
  - as you deploy your environments for your backend APIs you would add those urls as well
    - https://api-dev.example.company.org
    - https://api-stage.example.company.org
    - https://api.example.company.org
  - it's discouraged to use `localhost` in the allowed urls
    - the common practice is to modify your `/etc/hosts` file for developing applications locally
    - then you could add the url for that host in the allowed callbacks
      - https://api-local.example.company.org
- review advanced settings
  - optionally, disable the `Implicit` grant type, which is discouraged for obtaining access tokens for SPAs

#### Modify Config for FastAPI
- under the basic information for the client application you should see the following
  - domain (defaults to {tenent}.{region}.auth0.com)
  - client id
  - client secret
- review your environment variable from `local.env` and substitute the `AUTH0_HOST` and `AUTH0_CLIENT_ID`
  - we don't need the client secret since the application type is SPA
- also substitute the `AUTH0_AUDIENCE` based on the environment you're working with
  - the audience should match one of the logical APIs defined in your auth0 tenet

### Additional Notes

#### Note on Deploying
You could deploy the project code with the same AWS architecture from my medium tutorial:
- [FastAPI on AWS with MongoDB Atlas and Okta][medium-tutorial]

When you define the HTTP api gateway routes you can actually select which scopes are required upfront in the request.
- `GET /message` and `GET /message/{id}` would require the `read:messages` scope
- `POST /message` and `PUT /message/{id}` would require the `write:messages` scope

The only caveat for doing the above is that there's some coupling between infrastructure and application code. Instead of
having proxy+ routes in API Gateway that would forward all authenticated requests to the lambda function, we would have to
define more specific routes so that API Gateway can also handle request authorization.

#### Useful Links
- https://auth0.com/docs/get-started/authentication-and-authorization-flow/implicit-flow-with-form-post
- https://community.auth0.com/t/invalid-access-token-payload-jwt-encrypted-with-a256gcm/77893

[medium-tutorial]: https://medium.com/@rajan-khullar/fastapi-on-aws-with-mongodb-atlas-and-okta-6e37c1d9069
