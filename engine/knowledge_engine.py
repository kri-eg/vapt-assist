class KnowledgeEngine:
    def __init__(self):
        self.rules = {
            "ssh": [
                "Run detailed version scan",
                "Check for weak SSH authentication",
                "Look for outdated OpenSSH versions"
            ],
            "http": [
                "Check web server: curl http://<target>",
                "Run directory scan (future feature)",
                "Check HTTP headers and security configs"
            ],
            "nping-echo": [
                "Service used for testing network reachability",
                "Usually low risk but verify exposure"
            ],
            "tcpwrapped": [
                "Service is protected or filtered",
                "Further probing may be required"
            ]
        }

    def analyze(self, parsed_data):
        suggestions = []

        for host in parsed_data:
            for port in host["ports"]:
                service = port["service"]

                # Known services
                if service in self.rules:
                    actions = self.rules[service]

                # Pattern-based logic
                elif "http" in service:
                    actions = [
                        "Identify web application: curl http://<target>",
                        "Check for exposed endpoints",
                        "Analyze HTTP headers"
                    ]

                elif "rpc" in service or "msrpc" in service:
                    actions = [
                        "Enumerate RPC services",
                        "Check for Windows service exposure",
                        "Assess internal service risks"
                    ]

                elif "vmware" in service:
                    actions = [
                        "Check VMware service exposure",
                        "Ensure proper authentication is enforced",
                        "Verify service necessity"
                    ]

                else:
                    # Generic fallback
                    actions = [
                        "Perform service version detection",
                        "Research service name for known vulnerabilities",
                        "Assess if service should be exposed"
                    ]

                suggestions.append({
                    "port": port["port"],
                    "service": service,
                    "actions": actions
                })

        return suggestions