# SalaryAi: Predict Employee Salaries with Machine Learning 🚀

![SalaryAi](https://img.shields.io/badge/SalaryAi-Predict%20Salaries-brightgreen)

Welcome to the **SalaryAi** repository! This machine learning-powered web application predicts employee salaries based on various input features. With an intuitive interface and robust backend, SalaryAi aims to make salary predictions accessible and reliable.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [API Documentation](#api-documentation)
7. [Contributing](#contributing)
8. [License](#license)
9. [Support](#support)

## Introduction

SalaryAi is designed to help users estimate employee salaries based on key factors such as age, gender, education level, job title, and years of experience. This application uses U.S. salary data to provide accurate predictions. Built with **FastAPI**, it offers a sleek frontend interface, making it easy for users to interact with the model.

You can download the latest release [here](https://github.com/tejbhanp/SalaryAi/releases). This file needs to be downloaded and executed to get started.

## Features

- **User-Friendly Interface**: A clean and intuitive design allows users to input data easily.
- **Accurate Predictions**: Utilizes machine learning models for reliable salary predictions.
- **Data-Driven**: Based on extensive U.S. salary data.
- **FastAPI Backend**: Ensures quick responses and efficient processing.
- **Responsive Design**: Works well on both desktop and mobile devices.

## Technologies Used

SalaryAi is built using a combination of technologies that work together seamlessly:

- **FastAPI**: A modern web framework for building APIs with Python.
- **HTML/CSS**: For creating the frontend interface.
- **JavaScript**: Enhances user interaction and experience.
- **Python**: The core programming language for machine learning models.
- **Jupyter Notebooks**: Used for prototyping and experimenting with machine learning algorithms.
- **Linear Regression**: A statistical method for predicting salaries.
- **Polynomial Regression**: An advanced technique for more complex relationships.
- **Machine Learning Pipelines**: Streamlines the process of training and deploying models.

## Installation

To set up SalaryAi on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tejbhanp/SalaryAi.git
   cd SalaryAi
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the App**: Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

Once the application is running, you can start predicting salaries. Follow these steps:

1. **Input Data**: Fill in the required fields:
   - Age
   - Gender
   - Education Level
   - Job Title
   - Years of Experience

2. **Submit**: Click the "Predict" button.

3. **View Results**: The predicted salary will be displayed on the screen.

## API Documentation

The API exposes several endpoints for interaction. Here’s a brief overview:

- **GET /predict**: Use this endpoint to get salary predictions based on input features.
- **POST /predict**: Send a JSON payload with the required features to receive a prediction.

### Example Request

```json
{
  "age": 30,
  "gender": "female",
  "education_level": "Bachelor's",
  "job_title": "Software Engineer",
  "years_of_experience": 5
}
```

### Example Response

```json
{
  "predicted_salary": 85000
}
```

## Contributing

We welcome contributions! If you want to help improve SalaryAi, follow these steps:

1. **Fork the Repository**: Click the "Fork" button on the top right of this page.
2. **Create a Branch**:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. **Make Your Changes**: Edit the code as needed.
4. **Commit Your Changes**:
   ```bash
   git commit -m "Add your message here"
   ```
5. **Push to Your Fork**:
   ```bash
   git push origin feature/YourFeatureName
   ```
6. **Open a Pull Request**: Go to the original repository and click on "New Pull Request".

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, feel free to reach out. You can also check the "Releases" section for updates and downloads.

For the latest release, visit [here](https://github.com/tejbhanp/SalaryAi/releases). This file needs to be downloaded and executed to get started.

---

Thank you for your interest in SalaryAi! We hope you find this application useful for predicting employee salaries. Happy coding!