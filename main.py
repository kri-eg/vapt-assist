from scanner.nmap_executor import NmapExecutor
from parser.nmap_parser import NmapParser
from engine.knowledge_engine import KnowledgeEngine
from engine.workflow_engine import WorkflowEngine

def main():
    print("\n=== VAPTAssist: Nmap Workflow Assistant ===\n")

    target = input("Enter target (IP address or domain): ").strip()

    if not target:
        print("[-] Error: Target cannot be empty.")
        return

    # 🔹 Run scan
    scanner = NmapExecutor()
    xml_file = scanner.run_scan(target)

    if not xml_file:
        print("[-] Scan failed.")
        return

    # 🔹 Parse results
    print("\n[+] Parsing scan results...\n")

    parser = NmapParser(xml_file)
    results = parser.parse()

    print("[+] Parsed Results:\n")

    for host in results:
        print(f"Host: {host['host']}")

        if not host["ports"]:
            print("  No open ports found")

        for port in host["ports"]:
            print(f"  Port {port['port']} → {port['service']} ({port['state']})")

        print()

    # 🔹 Analyze results
    print("\n[+] Analyzing results...\n")

    engine = KnowledgeEngine()
    suggestions = engine.analyze(results)

    print("[+] Suggested Next Steps:\n")

    for item in suggestions:
        print(f"Port {item['port']} ({item['service']}):")

        for action in item["actions"]:
            print(f"  → {action}")

        print()

    workflow = WorkflowEngine(target)
    workflow.start(suggestions)


if __name__ == "__main__":
    main()