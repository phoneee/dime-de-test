FROM apache/airflow:2.7.3

USER root
RUN apt-get update && \
    apt-get install -y build-essential openjdk-11-jdk procps && \
    apt-get clean &&  \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-arm64
# Verify Java installation
RUN java -version

# Switch back to the non-root user (Airflow user)
USER airflow

# Install additional requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt