#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # add creds in json
        with open('config.json', 'r') as f:
          distros_dict = json.load(f)
      
        user = distros_dict['user']
        blocked = distros_dict['blocked']
        forbidden_words = distros_dict['forbidden_words']

        

        # Send headers
        self.send_header('Content-type','text/html')
        self.send_header('X-ElQuePregunta',user)
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8080)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server on port '+str(server_address[1]) + '...')
  httpd.serve_forever()


run()