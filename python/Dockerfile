FROM python:3.9-slim
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
 && rm -rf /var/lib/apt/lists/*

COPY . /usr/src/app
RUN pip install jupyterlab
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8888

CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]