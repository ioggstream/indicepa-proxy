#!/usr/bin/bash
docker build -t swagger_server .
docker run -p 8080:8080 swagger_server

