FROM python:3 import http.server
import os print("Serving on port", os.environ.get("PORT", 8080))
import os print("Serving on port", os.environ.get("PORT", 8080))
print("Content-Type: text/html") with open("index.html", "r") as f:
print("Content-Type: text/html") with open("index.html", "r") as f:
    print(f.read())
