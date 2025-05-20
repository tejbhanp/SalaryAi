from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Load your pipeline
pipeline = joblib.load("predict_salary.pkl")

# Initialize FastAPI app
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Define the input schema using Pydantic
class SalaryInput(BaseModel):
    Age: float
    Gender: str
    Education_Level: str = Field(..., alias="Education Level")
    Job_Title: str = Field(..., alias="Job Title")
    Years_of_Experience: float = Field(..., alias="Years of Experience")

    model_config = {
        "populate_by_name": True
    }

@app.get("/")
def root():
    return FileResponse("static/index.html")

# Define the prediction endpoint
@app.post("/predict")
def predict_salary(data: SalaryInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([{
        "Age": data.Age,
        "Gender": data.Gender,
        "Education Level": data.Education_Level,
        "Job Title": data.Job_Title,
        "Years of Experience": data.Years_of_Experience
    }])

    # Make prediction
    prediction = pipeline.predict(input_df)[0]
    
    return {"Predicted Salary": f"${round(prediction, 2)} / annum"}

@app.get("/dropdown-options")
def get_dropdown_options():
    df = pd.read_csv("fdataset.csv")  # Load your dataset
    return {
        "gender_options": ['Female', 'Male', 'Other'],
        "education_options": sorted(df["Education Level"].dropna().unique().tolist()),
        "job_title_options": sorted(df["Job Title"].dropna().unique().tolist())
    }