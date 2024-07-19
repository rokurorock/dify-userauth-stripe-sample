
## What is this repository?

This repository is a sample implementation of user authentication and subscription functionality in a Dify application. 

**By simply changing the .env file, you can easily try it out.**

The implementation uses Dify through an API call, and Dify and other functionalities are completely independent, achieving loose coupling between modules. This allows Dify developers to focus on developing LLM applications using the latest Dify apps.

Additionally, user authentication is implemented using Supabase, which allows free user authentication for up to 50,000 users. Supabase is a BaaS service operated by a startup based in Singapore and offers features such as database and storage functionalities, making it easy to expand your LLM application!


## Tech Stack Overview
llm app : dify
flontend : streamlit
user_auth : supabase
pyment : stripe
 
## how to use at Local
It's as simple as 5 easy steps!

### Step 1: Copy your Dify app into the dify-userauth-stripe-sample directory.
Copy your Dify app into the dify-userauth-stripe-sample directory. 
If you are using Dify for the first time, please git clone dify-userauth-stripe-sample.

### Step 2: .env 
```
cp myapp/.env.template .env 
```
Enter the API key and other information into the .env file.
```
DIFY_API_KEY = #dify api key
ROOT_URL = "http://*.*.*.*/" #dify api root url
SUPABASE_URL = #supabase url
SUPABASE_KEY = #supabase key
STRIPE_API_KEY = #stripe api key
STRIPE_API_KEY_TEST = #stripe api key for test
STRIPE_TEST_MODE = "true" #stripe test mode true or false
STRIPE_LINK = #stripe link
STRIPE_LINK_TEST =  #stripe link for test mode
```

### Step3: Build the Dify application.
```
cd dify/docker
docker-compose up -d
```

### Step4: Build the Myapp application.
```
cd myapp
docker-compose up -d
```

### Step5 Start the Myapp
http://localhost:8501/


## Todo
This is just a sample created in one day. There are many features that are not implemented:
- Subscription cancellation feature
- Support for Dify APIs other than chatapi
- Production environment support
etc.