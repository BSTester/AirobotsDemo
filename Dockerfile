FROM python
USER root
VOLUME /data
WORKDIR /data
COPY ./requirements.txt /data/requirements.txt

RUN cd /data && \
    pip3 install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple && \
    pip3 install -r /data/requirements.txt -i https://mirrors.aliyun.com/pypi/simple && \
	ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN pip3 install opencv-python-headless -i https://mirrors.aliyun.com/pypi/simple 

ENTRYPOINT ["airobots"]