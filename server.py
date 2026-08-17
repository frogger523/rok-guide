from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from waitress import serve

from app import create_app


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


def get_port() -> int:
    raw_port = os.getenv("PORT", "41783")
    try:
        port = int(raw_port)
    except ValueError as exc:
        raise SystemExit(f"PORT must be a number, received: {raw_port!r}") from exc
    if not 1 <= port <= 65535:
        raise SystemExit("PORT must be between 1 and 65535")
    return port


if __name__ == "__main__":
    port = get_port()
    print("\n  ROK META // FIELD INTELLIGENCE")
    print(f"  Open http://127.0.0.1:{port}\n")
    serve(create_app(), host="127.0.0.1", port=port, threads=6)

