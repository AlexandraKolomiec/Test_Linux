import subprocess
import re
import string
string.punctuation

if __name__ == '__main__':
    result = subprocess.run('cat /etc/os-release', shell=True,
                            stdout=subprocess.PIPE, encoding='utf 8')
    out = result.stdout
    for p in string.punctuation:
        if p in out:
            out1 = out.replace(p, ' ')

    def func(com: str, text: str):
        if result.returncode == 0:
            if re.search(r'jammy', out1):
                print(True)
        else:
            print(False)


    func('cat', '/etc/os-release')
