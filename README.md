
# News App

This is a Flask web application that fetches and displays news articles based on the selected date using the News API.

## Features

- Select a date to view news articles published on that day.
- Display news articles in a modern card layout.
- Uses AJAX to dynamically fetch news articles without page reload.
- Deployable on Google Cloud Platform (GCP) with continuous integration using GitHub Actions.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ChoudhariNikita/News-App.git
   ```

2. Navigate to the project directory:
   ```
   cd News-App
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

5. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

6. Obtain an API key from the News API website (https://newsapi.org/):
   - Sign up for an account if you don't have one.
   - Create a new API key.
   - Copy the API key and replace `YOUR_NEWS_API_KEY` in `app.py` with your actual API key.

7. Run the Flask app:
   ```
   python app.py
   ```

8. Open your web browser and navigate to `http://127.0.0.1:5000` to view the app.

## Deployment

You can deploy this Flask app on Google Cloud Platform (GCP) App Engine for production use. Follow these steps to deploy:

1. Sign in to your GCP Console and create a new project.

2. Install the Google Cloud SDK if you haven't already.

3. Initialize the App Engine app:
   ```
   gcloud app create --project=YOUR_PROJECT_ID
   ```

4. Deploy the app:
   ```
   gcloud app deploy
   ```

5. Access the deployed app using the provided URL.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
