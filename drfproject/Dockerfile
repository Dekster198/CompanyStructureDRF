FROM python:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /company_structure
COPY requirements.txt /company_structure/
RUN pip install -r requirements.txt
COPY . /company_structure/