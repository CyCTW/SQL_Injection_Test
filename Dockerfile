FROM python:3.8.4
WORKDIR /app

COPY Pipfile* ./
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

COPY . /app
EXPOSE 80

CMD ["python", "app.py"]