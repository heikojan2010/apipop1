from fastapi_csv import FastAPI_CSV

app = FastAPI_CSV("pop1Codes.csv")

@app.get("/")
def hello():
    return app()