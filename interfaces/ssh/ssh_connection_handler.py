import paramiko

"""
Fasade Pattern for pythons paramiko libraray to make sending 
commands to a simple and a nested server using SSH protocol easier.
Paramikos errors are not caught here.
"""


def send_request_to_server(
    hostname: str,
    username: str,
    password: str,
    request: str,
    port: int = 22,
) -> str:
    """
    Helper function to send a request to an SSH server. Creates a
    SSH client instance. Sends a command to the server receives
    a response (stdout), closes the client and all connections
    and returns the response.
    Returns: Response as a str.
    """
    client = establish_simple_connection(
        hostname=hostname, username=username, port=port, password=password
    )
    stdin, stdout, stderr = client.exec_command(command=request)
    client.close()
    return stdout.read().decode()


def send_request_to_nested_server(
    hostname: str,
    nested_hostname: str,
    username: str,
    password: str,
    request: str,
    port: int = 22,
    nested_port: int = 0,
) -> str:
    """
    Helper function to send a request to a nested SSh sever
    """
    client = establish_nested_connection(
        hostname=hostname,
        port=port,
        nested_hostname=nested_hostname,
        nested_port=nested_port,
        username=username,
        nested_password=password,
    )
    stdin, stdout, stderr = client.exec_command(command=request)
    client.close()
    return stdout.read().decode()


def establish_simple_connection(
    hostname: str, username: str, password: str, port: int = 22
) -> paramiko.SSHClient:
    """
    Helper function to create a simple SSH connection and
    returns a
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=hostname, username=username, port=port, password=password)
    return client


def establish_nested_connection(
    hostname: str,
    nested_hostname: str,
    username: str,
    nested_password: str,
    port: int = 22,
    nested_port: int = 0,
) -> paramiko.SSHClient:
    """
    Created a connection to a nested server by creating a transport
    channel between SSHClient instances and passing it as socket
    to the connect method of the intended client.
    """

    # create bosh ssh clients
    client = paramiko.SSHClient()
    nested_client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    nested_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # create a transport instance and create a channel between ssh clients
    transport = client.get_transport()
    channel = transport.open_channel(
        kind="direct-tcpip",
        dest_addr=(hostname, port),
        src_addr=(nested_hostname, nested_port),
    )

    # connect to the nested client threw the hostname of the client and
    # the channel that is passed as socked
    nested_client.connect(
        hostname=hostname, username=username, password=nested_password, sock=channel
    )
    return nested_client
