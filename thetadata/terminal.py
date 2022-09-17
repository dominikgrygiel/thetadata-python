import os
import urllib.request


def launch_terminal(username: str = None, passwd: str = None):

    if username is None or passwd is None:
        os.system("java -jar ThetaTerminal.jar")
    else:
        os.system("java -jar ThetaTerminal.jar " + username + " " + passwd)


def check_download(auto_update: bool):
    if os.path.exists('ThetaTerminal.jar') or auto_update:
        jar = urllib.request.urlopen("https://download-latest.thetadata.us")
        with open('ThetaTerminal.jar', 'wb') as output:
            output.write(jar.read())
            output.close()


