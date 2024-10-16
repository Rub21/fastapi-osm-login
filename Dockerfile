FROM python:3.9
WORKDIR /main
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8000
COPY ./ .
WORKDIR /main/app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--log-level", "debug"]