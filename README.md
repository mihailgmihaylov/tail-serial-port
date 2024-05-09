# tail-serial-port
A sample project to create a tool that tails logs from a given serial port

The end product is a python script that can run as a standalone tool or in a docker container.
It can be used to tail a serial port and put all messages in a file.

The script supports arguments and can be templatable.

## How to use

First you need to setup the python environment. You can either create a virtual env or try the script out in a container

Using venv:

```
python3 -m venv .venv
source .venv/bin/activate
pip install pyserial
```

Using docker container:

```
docker pull python:3.12
docker run -it --name python -v ./tail_serial_port:/scripts python:3.12 /bin/tail -f /etc/hosts&
docker exec -ti python /bin/bash
```

```
pip install pyserial
```

Next, you simply execute the script:

```
python tail_serial_port.py -p <serial_port> -o <output_file>
```

Example:
```
python tail_serial_port.py -p /dev/ttys006 -o output.txt
Start collecting serial port data...
Opened serial port: /dev/ttys006

```

*Note* that there are other flags. The full list can be seen by:

```
python tail_serial_port.py --help                                                                                                                                                                                                                     <aws:mine>
usage: tail_serial_port.py [-h] [-p PORT] [-o OUTPUT] [-b BYTESIZE] [-brate BAUDRATE] [-pa PARITY] [-s STOPBITS]

Collecting logs over a serial port.

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Serial port name (e.g., /dev/pts/2)
  -o OUTPUT, --output OUTPUT
                        File to store the logs (e.g., -o=serial_data.txt)
  -b BYTESIZE, --bytesize BYTESIZE
                        Set serial bytesize (e.g., -b=8)
  -brate BAUDRATE, --baudrate BAUDRATE
                        Set serial baudrate (e.g., -brate=8)
  -pa PARITY, --parity PARITY
                        Set serial parity (e.g., -brate=8)
  -s STOPBITS, --stopbits STOPBITS
                        Set serial stopbits (e.g., -s=1)
```

If you want to simulate a Serial port, there are different ways to do so. One is simply:

```
socat -d -d -b 8192 pty,raw,echo=0,b115200,parenb=0,stop=1 pty,raw,echo=0,b115200,parenb=0,stop=1
```

## How to build container

If you like to build it locally and test, simply:
```
docker build -t tail-serail-port:v0.0.1 .
```

If you like to build the container to support multi-arch and push it to a repository:

```
docker buildx build --push --platform linux/amd64 -t mihailgmihaylov/tail-serail-port:v0.0.1 .
docker buildx build --push --platform linux/arm64/v8 -t mihailgmihaylov/tail-serail-port:v0.0.1 .
```

## Sources

https://pyserial.readthedocs.io/en/latest/shortintro.html
https://docs.python.org/3/howto/argparse.html
https://www.irongeek.com/i.php?page=backtrack-3-man/socat
