FROM python:3.9
WORKDIR /neural-api
ADD requirements.txt .
ADD api_ex.py .

RUN pip install -r requirements.txt

CMD ["python", "./api_ex.py"]