import subprocess
import re

if __name__ == '__main__':
    result = subprocess.run('cat /etc/os-release', shell=True,
                            stdout=subprocess.PIPE, encoding='utf 8')
    out = result.stdout
    #print(out)


    def func(com: str, text: str):
        if result.returncode == 0:
            if re.search(r'jammy', out):
                print(True)
        else:
            print(False)


    func('cat', '/etc/os-release')
