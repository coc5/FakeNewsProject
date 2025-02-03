# FastAPI 관련 코드(python 백엔드) FastAPI 엔트리 포인트

from fastapi import FastAPI

app = FastAPI()  # ✅ FastAPI 애플리케이션 객체 정의

@app.get("/fastapi/data")
def get_data():
    return {"message": "Hello from FastAPI", "status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    
    # cmd에서 uvicorn fastapi_app:app --host 0.0.0.0 --port 8000 --reload 실행