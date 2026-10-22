import os
import httpx
from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
VIRUSTOTAL_URL = "https://www.virustotal.com/api/v3/urls"


def analyze_url(url: str) -> dict:
    if not VIRUSTOTAL_API_KEY:
        raise HTTPException(status_code=500, detail="VirusTotal API key not configured")

    with httpx.Client(timeout=30.0) as client:
        response = client.post(
            VIRUSTOTAL_URL,
            headers={"x-apikey": VIRUSTOTAL_API_KEY},
            data={"url": url}
        )

        if response.status_code == 200:
            result = response.json()
            analysis = result.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
            return {
                "url": url,
                "malicious": analysis.get("malicious", 0),
                "suspicious": analysis.get("suspicious", 0),
                "harmless": analysis.get("harmless", 0),
                "undetected": analysis.get("undetected", 0),
                "total_engines": sum(analysis.values()),
                "is_safe": analysis.get("malicious", 0) == 0 and analysis.get("suspicious", 0) == 0
            }
        elif response.status_code == 404:
            raise HTTPException(status_code=404, detail="URL not found in VirusTotal database")
        else:
            raise HTTPException(status_code=response.status_code, detail="VirusTotal API error")


@app.get("/", response_class=HTMLResponse)
async def home():
    return Path("templates/index.html").read_text()


@app.post("/scan")
async def scan_url(url: str = Form(...)):
    return analyze_url(url)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
