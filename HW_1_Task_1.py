import subprocess

result = subprocess.run("cat /etc/os-release", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
lst = result.stdout.split("\n")


def my_func(command, text):
	if command.returncode == 0:
		if 'PRETTY_NAME="Ubuntu 22.04.5 LTS"' in text and 'VERSION="22.04.5 LTS (Jammy Jellyfish)"' in text:
			print("TRUE")
		else:
			print("FALSE")
	else:
		print("FALSE")


print(my_func(result, lst))
