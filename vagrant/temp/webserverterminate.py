from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

class webserverHandler(BaseHTTPRequestHandler):
       def do_GET(self):
              try:
                     if self.path.endswith("/hello"):
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()

                            output=""
                            output+="<html><body>Hello!</body></html>"
                            self.wfile.write(output)
                            print output
                            return

                     if self.path.endswith("/hola"):
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.end_headers()

                            output=""
                            output+="<html><body>&#161Hola! <br/> <a href='/hello'>Back to Hello</a></body></html>"
                            self.wfile.write(output)
                            print output
                            return

              except Exception as e:
                     self.send_error(404, "File not found %s" % self.path)


       def do_POST(self):
              try:
                     self.send_response(301)
                     self.end_headers()

                     ctype, pdict = cgi.parse_header(self.headers.gethearder('content-type'))
                     if ctype=='multipart/form-data':
                            fields = cgi.parse_multipart(self.rfile, pdict)
                            messageContent = fields.get('message')

                     output=""
                     output+="<html><body>"
                     output+="<h2>Okay, how about this: </h2>"
                     output+="<h1> %s </h1>" % messageContent[0]
              except Exception as e:
                     raise e
              
              

def main():
       port=8080
       server = HTTPServer(('',port), webserverHandler)
       print "web server stopped on port %s" %port

if __name__ =='__main__':
       main()