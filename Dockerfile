FROM python:3.11.9-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

FROM base AS builder

COPY requirements.txt ./requirements.txt
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip setuptools wheel \
    && /opt/venv/bin/pip install -r requirements.txt

FROM base AS runtime

ENV PATH="/opt/venv/bin:$PATH" \
    SERVICE_HOST=0.0.0.0 \
    SERVICE_PORT=8001 \
    ENVIRONMENT=production

COPY --from=builder /opt/venv /opt/venv
COPY . .

RUN addgroup --system appgroup \
    && adduser --system --ingroup appgroup --home /app appuser \
    && chown -R appuser:appgroup /app

USER appuser

EXPOSE 8001

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=5 \
  CMD curl -fsS "http://127.0.0.1:${SERVICE_PORT}/health" || exit 1

CMD ["sh", "-c", "uvicorn app.main:app --host ${SERVICE_HOST} --port ${SERVICE_PORT} --proxy-headers"]