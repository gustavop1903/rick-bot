import uvicorn 
import os

if __name__ == "__main__":
    reloads=os.getenv("ENVIRONMENT", "").upper() == "DEVELOPMENT"

    uvicorn.run(
        "rick_bot.main:app",
        host="0.0.0.0",
        port=7002,
        log_level="info",
        reload=reloads,
        app_dir="src",
    )