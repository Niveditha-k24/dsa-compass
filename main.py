from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def read_root():
    greeting={"message":"hello user"}
    return greeting

@app.get("/health")
def health():
    h={"status":"ok"}
    return h