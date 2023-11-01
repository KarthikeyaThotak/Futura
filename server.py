from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
import openai

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)

openai.api_key=""

@app.get("/")
async def main():
    return {"message":"hello world"}

@app.get("/Education")
def Education(edu: str):
    def ask_openai(message):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt = message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
       )
        answer = response.choices[0].text.strip()
        return answer
    question = "Top 3 common " + edu + " degrees that you need in the cybersecurity field, degree names only."
    return ask_openai(question)


@app.get("/Certifications")
def Certifications(degree: str):
    def ask_openai(message):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt = message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return answer
    question = "Top 3 certifications that you need in the " + degree + " field, certification names only."
    answer = ask_openai(question)
    return answer


@app.get("/Experiences")
def Experiences(degree: str):
    def ask_openai(message):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt = message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return answer
    question = "Top 3 types of practical experiences, for beginners, that you need in the " + degree + " field, practical experience names only."
    return ask_openai(question)


@app.get("/Salary")
def Salary(degree: str):
    def ask_openai(message):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt = message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return answer
    question = "Salary range for working in the " + degree + " field, entry-level position, mid-level position and senior-level position (one each), only salary ranges."
    return ask_openai(question)


@app.get("/YouTube")
def YouTube(degree: str):
    def ask_openai(message):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt = message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return answer
    question = "Top 3 youtube channels  to learn " + degree + ", youtube channel names only"
    return ask_openai(question)


@app.get("/Companies")
def Companies(degree: str):
    def ask_openai(message):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt = message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
        )
        answer = response.choices[0].text.strip()
        return answer
    question = "Top 3 companies that provide " + degree + " cybersecurity jobs and internships, company names only."
    return ask_openai(question)


