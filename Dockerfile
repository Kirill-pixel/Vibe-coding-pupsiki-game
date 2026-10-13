FROM python:3.12-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1
RUN pip install --no-cache-dir aiogram
COPY app.py index.html ./
EXPOSE 15080
CMD ["python", "app.py"]
