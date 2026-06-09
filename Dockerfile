FROM python:3.9-slim
WORKDIR /project
COPY . /project
CMD ["python", "ecomic.py"]