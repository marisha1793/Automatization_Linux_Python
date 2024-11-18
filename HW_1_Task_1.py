import subprocess

result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
lst = result.stdout.split("\n")


def my_func(command, text):
	if command.returncode == 0:
		if 'PRETTY_NAME="Ubuntu 22.04.5 LTS"' in text and 'VERSION="22.04.5 LTS (Jammy Jellyfish)"' in text:
			return True
		else:
			return False
	else:
		return False


if __name__ == '__main__':
	print(my_func(result, lst))
