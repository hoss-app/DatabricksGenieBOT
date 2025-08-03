import os
from app import app

if __name__ == "__main__":
    from aiohttp import web
    
    # Get port from environment (Azure sets this)
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    
    web.run_app(app, host=host, port=port)