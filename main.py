from fastapi import FastAPI

app = FastAPI(
    title="Identity Threat Detection & Response Platform",
    version="1.0.0",
    description="A Cyber Security project for detecting identity-based threats."
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the Identity Threat Detection & Response Platform"
    }