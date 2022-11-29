import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

server_ip = '' # RPi IP ADDRESS
server_port = 1011

status = None

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

class MyServer(BaseHTTPRequestHandler):
  def do_POST(self):
    content_length = int(self.headers['Content-Length'])
    state = self.rfile.read(content_length).decode()
    
    if state == status:
      self.send_response(304)
     
    elif state == 'true':
      GPIO.output(18, GPIO.HIGH)
      self.send_response(201)
      status = 'true'
      
    elif state == 'false':
      GPIO.output(18, GPIO.LOW)
      self.send_response(200)
      status = 'false'
      
   self.end_headers()
  
Server = HTTPServer((server_ip, server_port), MyServer)
Server.serve_forever()
print('Server Online')
