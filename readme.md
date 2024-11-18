# JWT Authentication 

<p align="center">
  <em>JWT Authentication with FastAPI</em>
</p>

## How to run this code?

1. Clone the repository and navigate to the directory

   a) Start by cloning the repository to your desired location.
   
   b) Next, change into this directory

2. Create a `.env` file

   Copy env.sample to .env and update the values as needed.

3. Install dependencies

   Install the required Python packages with pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application

   Launch the application using Uvicorn with the following command:

   ```bash
   uvicorn main:app --reload
   ```

   The `--reload` flag will automatically reload the application whenever you make changes to the code. You can also use `--host 0.0.0.0` to make the API accessible on your local network.

## Authentication and Authorization

   The system utilizes JWT for handling access and refresh tokens. To obtain these tokens, log in through the `/login` endpoint using a POST request with your credentials in the body. Access tokens expire as set by the environment variable.
