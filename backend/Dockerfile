FROM debian:jessie

MAINTAINER Pascal Wengerter <pascal@wengerter.info>

RUN apt-get update && \
    apt-get install -y \
    python-pip \
    curl \
    yum \
    libxext6 \
    libfontconfig1 libxrender1 \
    fontconfig

RUN curl -L#o wk.tar.xz https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
    && tar xf wk.tar.xz \
    && cp wkhtmltox/bin/wkhtmltopdf /usr/bin \
    && cp wkhtmltox/bin/wkhtmltoimage /usr/bin \
    && rm wk.tar.xz \
    && rm -r wkhtmltox

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python","app/app.py"]
