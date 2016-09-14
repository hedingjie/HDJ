#-*- coding:utf-8 -*-  
  
from SocketServer import ThreadingTCPServer, BaseRequestHandler  
import traceback  
  
class MyBaseRequestHandlerr(BaseRequestHandler):  
    """ 
    #��BaseRequestHandler�̳У�����дhandle���� 
    """  
    def handle(self):  
        #ѭ����������ȡ�����Կͻ��˵�����  
        while True:  
            #���ͻ��������Ͽ�����ʱ��self.recv(1024)���׳��쳣  
            try:  
                #һ�ζ�ȡ1024�ֽ�,��ȥ�����˵Ŀհ��ַ�(�����ո�,TAB,\r,\n)  
                data = self.request.recv(1024).strip()  
                if not data:
			break  
                #self.client_address�ǿͻ��˵�����(host, port)��Ԫ��  
                print "receive data from  (%r):%r" % (self.client_address, data)  
                  
                #ת���ɴ�д��д��(������)�ͻ���  
                self.request.send('complete sending data!')  
            except:  
                traceback.print_exc()  
                break  
  	self.request.close()
if __name__ == "__main__":  
    #telnet 127.0.0.1 9999  
    host = ""       #��������������ip,��localhost��������,��""  
    port = 12345     #�˿�  
    addr = (host, port)  
      
    #����TCPServer����  
    server = ThreadingTCPServer(addr, MyBaseRequestHandlerr)  
      
    #�����������  
    server.serve_forever()  
