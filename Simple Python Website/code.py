
import socket
import requests
import urllib.parse
import urllib.request as request
from http import HTTPStatus
import http.server
import socketserver
import os

"""
MyHTTPServer

A simple Python web server which implements GET and POST
"""


def run_file():
    os.system('python P1.py')
    return 'http://localhost:8503/'


class Handler(http.server.SimpleHTTPRequestHandler):
    # This class serves files from the directory directory and below, or the current directory if directory is not provided, directly mapping the directory structure to HTTP requests.
    def do_GET(self) -> None:
        try:
            print(self.path)
            if '?' in self.path:  # if query strings available

                # get the query string part only
                self.path = self.path.split('?')[1]
                # print(self.path)

                # convert query strings to dictionary
                res = dict(urllib.parse.parse_qsl(self.path))
                file_to_open = open(self.path[1:]).read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                # write content of page
                self.wfile.write(file_to_open.encode())
            else:
                # if no query strings available
                if self.path == '/':
                    self.path = '/index.html'  # the basic file
                if self.path.endswith('.html'):
                    file_to_open = open(self.path[1:]).read()  # intended file
                    self.send_response(200)

                self.end_headers()
                self.wfile.write(bytes(file_to_open, 'utf-8'))
        except:
            pass  # Some attributes error may occur

    def do_POST(self) -> None:
        self.send_response(HTTPStatus.OK)
        print(self.path+"post")
        if (self.path == '/test.html'):
            # <--- Gets the size of data
            content_length = int(self.headers['Content-Length'])
            # <--- Gets the data itself
            post_data = self.rfile.read(content_length)
            page = "<html><body><h1>POST!</h1><pre>" + \
                str(post_data).strip('b') + "</pre></body></html>"
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(page.encode())
        if (self.path == '/Form.html'):

            # <--- Gets the size of data
            content_length = int(self.headers['Content-Length'])
            # <--- Gets the data itself
            post_data = self.rfile.read(content_length)
            axes = str(post_data).strip('b').strip("'").split("&")
            x = " ".join(axes[0].strip("x=").split("+"))
            y = " ".join(axes[1].strip("y=").split("+"))
            file_to_open = " "
            if (x.lower() == "Day of Year".lower() and y.lower() == 'Min and Max averages'.lower()):
                print("BAR")
                file_to_open = open('bar.html').read()
            elif (x.lower() == 'Month'.lower() and y.lower() == 'Temperature comparison'.lower()):
                print("SCATTER")
                file_to_open = open('scatter.html').read()
            elif (x.lower() == 'Month'.lower() and y.lower() == 'Moving Average of Temperature of 12 months'.lower()):
                print("LINE")
                file_to_open = open('line.html').read()
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(file_to_open.encode())


ADDRESS = '127.0.0.1'
PORT = 12345
# It creates and listens at the HTTP socket, dispatching the requests to a handler.
httpd = socketserver.TCPServer((ADDRESS, PORT), Handler)
httpd.serve_forever()
