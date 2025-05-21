import uvicorn 
import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

if __name__ == "__main__":
    reloads=os.getenv("ENVIRONMENT", "").upper() == "DEVELOPMENT"

    uvicorn.run(
        "src.rick_bot.main:app",
        host="0.0.0.0",
        port=7002,
        log_level="info",
        reload=reloads,
        app_dir="src",
    )