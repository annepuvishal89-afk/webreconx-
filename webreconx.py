from passive import passive_recon
from active import active_recon
from colorama import Fore, Style

def banner():
    print(Fore.CYAN + """
    ===========================
        WebReconX Tool
    Python Web Reconnaissance
    ===========================
    """ + Style.RESET_ALL)

def main():
    banner()
    target = input("Enter target URL (example: https://example.com): ")

    print(Fore.GREEN + "\n[+] Starting Passive Recon...\n")
    passive_recon(target)

    choice = input("\nDo you want Active Recon? (yes/no): ")
    if choice.lower() == "yes":
        print(Fore.RED + "\n[+] Starting Active Recon...\n")
        active_recon(target)
    else:
        print("\nRecon Finished.")

if __name__ == "__main__":
    main()
