import xml.etree.ElementTree as ET

class NmapParser:
    def __init__(self, xml_file):
        self.xml_file = xml_file

    def parse(self):
        results = []

        tree = ET.parse(self.xml_file)
        root = tree.getroot()

        for host in root.findall("host"):
            address = host.find("address").get("addr")

            ports_data = []

            ports = host.find("ports")
            if ports:
                for port in ports.findall("port"):
                    state = port.find("state").get("state")

                    if state == "open":
                        port_id = port.get("portid")
                        service_elem = port.find("service")
                        service = service_elem.get("name") if service_elem is not None else "unknown"

                        ports_data.append({
                            "port": port_id,
                            "service": service,
                            "state": state
                        })

            results.append({
                "host": address,
                "ports": ports_data
            })

        return results