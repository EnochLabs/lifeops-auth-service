# -------- Base Image --------
FROM python:3.11.9-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# -------- Builder --------
FROM base AS builder

COPY requirements.txt .

RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install -r requirements.txt

# -------- Runtime --------
FROM base AS runtime

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONPATH="/app/src"

# Create user FIRST (important optimization)
RUN addgroup --system appgroup \
    && adduser --system --ingroup appgroup --home /app appuser

# Copy venv
COPY --from=builder /opt/venv /opt/venv

# Copy code with ownership (avoids slow chown)
COPY --chown=appuser:appgroup src ./src
COPY --chown=appuser:appgroup requirements.txt .

USER appuser

EXPOSE 8001

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=5 \
  CMD curl -fsS "http://127.0.0.1:8001/health" || exit 1

CMD ["sh", "-c", "uvicorn src.app.main:app --host 0.0.0.0 --port 8001"]
