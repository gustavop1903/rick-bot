import uvicorn 


if __name__ == "__main__":
    uvicorn.run(
        "rick_bot.main:app",
        host="0.0.0.0",
        port=7002,
        log_level="info",
        reload=True,
        app_dir="src",
    )