# Photo-Estimator

Ever Wonder whether an image you just took wil get as many views and likes as you think it would , will maybe not but major companies would for their marketing and business,
PhotoEstimator is a web application that determines whether the photo you're going to upload on Instagram is likely to be a "good" one or not. By analyzing your past Instagram photos and their performance, it uses a Convolutional Neural Network (CNN) to predict the potential success of your new photo based on the number of likes it might receive.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Instagram Integration**: Connect your Instagram profile to the web app.
- **Photo Analysis**: Scrapes and analyzes your past photos and likes.
- **Predictive Modeling**: Uses a CNN to predict the success of a new photo.
- **User-Friendly Interface**: Simple interface to upload and analyze photos.

## How It Works

1. **Instagram Profile Connection**: The user enters their Instagram profile, and the web app sends a follow request using the Instagram API.
2. **Data Scraping**: The app scrapes the user's photos and gathers data on the number of likes each photo received.
3. **Model Training**: The application trains a Convolutional Neural Network (CNN) using the scraped photos and their like counts to understand patterns and features of popular photos.
4. **Prediction**: When the user wants to upload a new photo, the app predicts whether it will be a hit or not relative to the maximum and minimum number of likes received on the user's past photos.

## Installation

### Prerequisites

- Python 3.x
- Flask
- Instagram API credentials
- Machine Learning libraries (e.g., TensorFlow ,keras,sklearn)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/Amine-Zitoun/Photo-Estimator.git
    cd Photo-Estimator
    ```

2. Set up the backend:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set up Instagram API:
    - Obtain Instagram API credentials and set them up in the environment variables or a configuration file.


5. Run the application:
    ```bash
    flask run
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
2. Enter your Instagram profile username.
3. Allow the app to send a follow request and scrape your photos.
4. Upload a new photo to see the prediction on its potential success.

## Technologies Used

- **Python**: Backend processing and data handling.
- **Flask**: Web framework for the backend.
- **Instagram API**: To connect and scrape user data.
- **TensorFlow/Keras**: For training and using the Convolutional Neural Network.
- **HTML/CSS**: Frontend development.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for review.

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Description of your changes"
    ```
4. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
5. Submit a pull request.

