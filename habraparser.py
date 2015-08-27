# -*- encoding: utf-8 -*-

__author__ = 'Илья'
import BaseHTTPServer as bhs, requests as req, urlparse, re, webbrowser

PORT = 8232
six = re.compile(r"\b(\w{6})\b",re.UNICODE)

class RequestHandler(bhs.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse.urlparse(self.path)
        r = req.get("http://habrahabr.ru%s" % parsed.path)
        if r.status_code != 200:
            self.send_response(200)
            self.end_headers()
            return

        (response,count) = six.subn(u"\\1\u2122",r.text)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.encode("utf-8"))
        return

def run(server_class=bhs.HTTPServer, handler_class=RequestHandler):
    server_address = ('127.0.0.1', PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()
    webbrowser.open("http://localhost:%d" % PORT)
    print("Serving at port %d" % PORT)

def main():
    run()

if __name__ == '__main__':
    main()