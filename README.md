# Guvi Courses Rating Prediction

## Project Overview
This project aims to predict the rating of Guvi courses based on various features using regression algorithms. The predictive model is trained on a dataset of Guvi courses, and the predictions can be made using a Streamlit web application.

## Project Structure
The project is structured as follows:

### 1. Jupyter Notebook (Notebook.ipynb)
- Data Cleaning: Loading and preprocessing the Guvi courses data.
- Model Training: Training a DecisionTreeRegressor model for rating prediction.
- Saving Model: Saving the trained model using pickle.

### 2. PyCharm (Streamlit Web App)
- Streamlit web application for user interaction.
- Prediction Page: Allows users to select a regression algorithm, predict ratings, and input new data.
- About Guvi Page: Provides information about Guvi, including its introduction and history.

## Instructions for Running the Streamlit Web App
1. Ensure Python and the required libraries are installed. You can install dependencies using `pip install -r requirements.txt`.
2. Open the PyCharm project and run the Streamlit web app script.

## File Descriptions
- **Notebook.ipynb**: Jupyter Notebook containing data cleaning, model training, and model saving.
- **app.py**: PyCharm script containing the Streamlit web application.
- **cleaned_guvi_data.csv**: Cleaned dataset used for training the regression model.
- **requirements.txt**: List of Python dependencies for the project.

## Usage
1. Run the Jupyter Notebook to preprocess data and train the regression model.
2. Open the Streamlit web app using PyCharm and interact with the prediction and information pages.

## Acknowledgments
- The dataset used in this project is sourced from [Guvi Courses](#).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
