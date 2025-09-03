from shodan import Shodan

# Introduce your Shodan API key here

API_KEY = "YOUR API KEY"

api = shodan.Shodan(API_KEY)

def main():
    print("Welcome to F00tpr1nt3r")
    print("This tool will help you find information about a target IP address using Shodan.")
    while True:
        cmd = input("F00tpr1nt3r> ").strip()
        if cmd == "exit":
            print("Exiting F00tpr1nt3r. Goodbye!")
            break
        elif cmd.startswith("search "):
            query = cmd[len("search "):]
            buscar(query)
        elif cmd.startswith("host "):
            ip = cmd[len("host "):]
            host_info(ip)
        elif cmd == "help":
            print("Commands:")
            #next commands
            print("  exit             - Exit the tool")
        else:
            print("Command not recognized. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()
