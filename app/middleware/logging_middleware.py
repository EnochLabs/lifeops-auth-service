import time
from fastapi import Request
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Extract request info
        method = request.method
        url = request.url.path
        client_host = request.client.host if request.client else "unknown"

        logger.info(f"Incoming request: {method} {url} from {client_host}")

        try:
            response = await call_next(request)

            process_time = (time.time() - start_time) * 1000
            status_code = response.status_code

            log_message = f"Request completed: {method} {url} - Status: {status_code} - Duration: {process_time:.2f}ms"

            if status_code >= 400:
                logger.warning(log_message)
            else:
                logger.info(log_message)

            return response

        except Exception as e:
            process_time = (time.time() - start_time) * 1000
            logger.exception(f"Request failed: {method} {url} - Error: {str(e)} - Duration: {process_time:.2f}ms")
            raise
