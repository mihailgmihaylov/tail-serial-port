import argparse
import time
import serial

def tail_serial_port(
        output,
        port,
        bytesize,
        baudrate,
        parity,
        stopbits
):
    with open(output, 'a') as file:
        with serial.Serial(port=port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits) as ser:
            print(f"Opened serial port: {port}")
            while ser.is_open:
                message = time.strftime("%Y-%m-%d %H:%M:%S ") + ser.readline().decode().strip() + '\n'
                file.write(message)

def main():
    print("Start collecting serial port data...")

    tail_serial_port(
        args.output,
        args.port,
        args.bytesize,
        args.baudrate,
        args.parity,
        args.stopbits
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Collecting logs over a serial port.')
    parser.add_argument('-p', '--port', type=str, help='Serial port name (e.g., /dev/pts/2)', default='/dev/pts/2')
    parser.add_argument('-o', '--output', type=str, help='File to store the logs (e.g., -o=serial_data.txt)', default='serial_data.txt')
    parser.add_argument('-b', '--bytesize', type=int, help='Set serial bytesize (e.g., -b=8)', default=8)
    parser.add_argument('-brate', '--baudrate', type=int, help='Set serial baudrate (e.g., -brate=8)', default=115200)
    parser.add_argument('-pa', '--parity', type=str, help='Set serial parity (e.g., -brate=8)', default='N')
    parser.add_argument('-s', '--stopbits', type=int, help='Set serial stopbits (e.g., -s=1)', default=1)
    args = parser.parse_args()

    main()
