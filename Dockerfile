FROM dorowu/ubuntu-desktop-lxde-vnc
USER root
VOLUME /data
WORKDIR /data
COPY ./requirements.txt /data/requirements.txt

RUN cd /data && apt-get update -y && apt-get install -y python3-pip && \
    pip3 install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple && \
    pip3 install -r /data/requirements.txt -i https://mirrors.aliyun.com/pypi/simple && \
	ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN pip3 install opencv-python-headless -i https://mirrors.aliyun.com/pypi/simple 

RUN export DISPLAY=':1'
RUN export NODE_IN_DOCKER=1
RUN export RESOLUTION=1920x1080

CMD ["/startup.sh", "&"]