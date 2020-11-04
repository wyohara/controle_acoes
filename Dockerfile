FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /source_code
WORKDIR /source_code
ADD backend /source_code
ADD .env /source_code
ADD customers.csv /source_code
COPY req.txt /source_code
RUN pip install -r req.txt