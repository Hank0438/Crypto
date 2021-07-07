FROM ubuntu:18.04
MAINTAINER hank
RUN apt-get update
RUN apt-get install xinetd -y
RUN useradd -m lsb_oracle
RUN chmod 774 /tmp
RUN chmod -R 774 /var/tmp
RUN chmod -R 774 /dev
RUN chmod -R 774 /run
RUN chmod 1733 /tmp /var/tmp /dev/shm
RUN chmod -R 775 /home/lsb_oracle
#RUN chown -R root:root /home/lcg
RUN apt-get update
RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip
RUN pip3 install pycrypto
RUN pip3 install gmpy2
CMD ["/usr/sbin/xinetd","-dontfork"]

