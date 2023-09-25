import subprocess

#Running curl from here
def run_curl_command(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print(f"Error: {error}")
    else:
        print(output.decode())

#The long one
def main():
    print("1. Basic curl")
    print("2. Basic HTTP Auth")
    print("3. HTTP with Encoded Auth")
    print("4. Output HTTP headers and cookie data")
    print("5. Check if a site is down")
    print("6. List contents of a directory")
    choice = input("Choose an option (1-6): ")

    url_choice = input("Do you want to enter a full URL? (yes/no if you want to give the server IP and port): ")
    if url_choice.lower() == "yes":
        url = input("Enter full URL: ")
    else:
        server_ip = input("Enter SERVER_IP: ")
        port = input("Enter PORT: ")
        url = f"http://{server_ip}:{port}/"

    if choice == "1":
        cmd = f"curl -i {url}"
    elif choice == "2":
        username = input("Enter USERNAME: ")
        password = input("Enter PASSWORD: ")
        cmd = f"curl -v http://{username}:{password}@{url}"
    elif choice == "3":
        auth_type = input("Enter auth type (Basic or Bearer): ")
        token = input("Enter TOKEN: ")
        cmd = f"curl -H 'Authorization: {auth_type} {token}' {url}"
    elif choice == "4":
        cmd = f"curl --dump-header headers_and_cookies.txt {url}"
    elif choice == "5":
        cmd = f'curl --head --show-error "{url}"'
    elif choice == "6":
        cmd = f'curl --list-only "{url}"'
    else:
        print("Invalid option. Please enter 1, 2, 3, 4, 5, or 6.")
        return

    run_curl_command(cmd)

if __name__ == "__main__":
    main()