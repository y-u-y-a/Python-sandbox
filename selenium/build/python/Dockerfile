FROM python:3.7

# Install Libraries
RUN set -x && \
  apt-get update && \
  apt-get install -y vim && \
  pip install selenium

# Don't create "/__pycache__"
ENV PYTHONDONTWRITEBYTECODE=1
ENV TZ=Asia/Tokyo
