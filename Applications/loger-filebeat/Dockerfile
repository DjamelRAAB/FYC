FROM centos:7

#Installation filebeat
COPY filebeat-6.8.13-x86_64.rpm /tmp/
RUN rpm -vi /tmp/filebeat-6.8.13-x86_64.rpm

#Execution 
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]                           