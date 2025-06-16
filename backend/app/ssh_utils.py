import os
import paramiko
import subprocess

from paramiko.auth_strategy import PrivateKey

def setup_ssh_key(ip, puerto, usuario, password):
    ssh_dir = "/home/nimbuscore/.ssh"
    private_key_path = os.path.join(ssh_dir, 'id_rsa')
    public_key_path = private_key_path + '.pub'
    
    os.makedirs(ssh_dir, mode=0o700, exist_ok=True)
    
    if not os.path.exists(private_key_path):
        subprocess.run([
            'ssh-keygen', '-t', 'rsa', '-b', '2048',
            '-f', private_key_path, '-N', ''
        ], check=True)
        os.chmod(private_key_path, 0o600)
        os.chmod(public_key_path, 0o644)
    
    with open(public_key_path, 'r') as f:
        public_key = f.read().strip()
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, puerto, usuario, password=password)
    
    comandos = [
        f'mkdir -p ~/.ssh',
        f'echo "{public_key}" >> ~/.ssh/authorized_keys',
        f'chmod 700 ~/.ssh',
        f'chmod 600 ~/.ssh/authorized_keys',
    ]
    
    for cmd in comandos:
        ssh.exec_command(cmd)

    ssh.close()