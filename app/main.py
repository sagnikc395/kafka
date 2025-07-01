import socket  # noqa: F401
import struct

class KafkaResponseMessage:
    def __init__(self,header,body=None):
        # creating the message_header as a 32 bit(signed) with 0 value
        self.message_head = 0
        self.header = header
        self.body = body

    def get_message_head(self):
        return self.message_head

    def send_header(self,conn):
    # send the message_head and header as a response
    # both message_head and header will be packed as 32-bit big-endian
        packed_data = struct.pack(">II",self.message_head,self.header)
        conn.send(packed_data)




def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    conn,addr = server.accept() # wait for client
    while conn:
        print(f"Connected by {addr}")
        message = KafkaResponseMessage(header=7)
        message.send_header(conn)

    server.close()

if __name__ == "__main__":
    main()
