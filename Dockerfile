FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install pipenv 
RUN pipenv install --system --deploy --ignore-pipfile

#WORKDIR /app/src
CMD ["python", "main.py"]
