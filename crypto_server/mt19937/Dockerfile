FROM ubuntu:18.04
MAINTAINER hank
RUN apt-get update
RUN apt-get install xinetd -y
RUN useradd -m mt19937
RUN chmod 774 /tmp
RUN chmod -R 774 /var/tmp
RUN chmod -R 774 /dev
RUN chmod -R 774 /run
RUN chmod 1733 /tmp /var/tmp /dev/shm
RUN chmod -R 775 /home/mt19937
#RUN chown -R root:root /home/mt19937
RUN apt-get install -y python3.7
RUN apt-get install -y python3-pip
RUN pip3 install pycrypto
CMD ["/usr/sbin/xinetd","-dontfork"]

