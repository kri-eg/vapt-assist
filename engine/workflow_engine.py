from engine.ai_agent import AIAgent
import subprocess


class WorkflowEngine:
    def __init__(self, target):
        self.target = target
        self.ai = AIAgent()

    def start(self, suggestions):
        print("\n=== Interactive Workflow Mode ===\n")

        for item in suggestions:
            port = item["port"]
            service = item["service"]
            actions = item["actions"]

            print(f"\nPort {port} ({service}):")

            for i, action in enumerate(actions, start=1):
                print(f"{i}. {action}")

            print("9. Ask AI Expert")
            print("0. Skip")

            choice = input("Enter your choice: ").strip()

            if choice == "0":
                continue

            elif choice == "9":
                print("\n[+] Consulting AI Expert...\n")
                response = self.ai.analyze_service(self.target, port, service)
                print(response)
                continue

            try:
                choice = int(choice)

                if 1 <= choice <= len(actions):
                    self.handle_action(actions[choice - 1])
                else:
                    print("Invalid choice")

            except ValueError:
                print("Invalid input")

    def handle_action(self, action):
        print(f"\n[+] Selected: {action}")

        command = None

        if "version" in action.lower():
            command = f"nmap -sV {self.target}"

        elif "http" in action.lower():
            command = f"curl http://{self.target}"

        elif "rpc" in action.lower():
            command = f"nmap --script=rpcinfo {self.target}"

        if command:
            print(f"[+] Suggested Command: {command}")

            run = input("Run this command? (y/n): ").strip().lower()

            if run == "y":
                subprocess.run(command, shell=True)
        else:
            print("[+] Manual investigation recommended")

        print()