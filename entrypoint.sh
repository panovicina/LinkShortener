#!/bin/bash

uvicorn app.main:init_app --host ${FASTAPI_HOST:-'0.0.0.0'} --port ${FASTAPI_PORT:-8000} --reload