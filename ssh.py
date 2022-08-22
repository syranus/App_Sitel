import paramiko
from paramiko import SSHClient

host = "51.158.145.195"
user = "jonathan"
password = "Carmelite44"

client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(host, username=user, password=password)


client.close()