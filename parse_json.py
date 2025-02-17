import json


with open("sample-data.json", "r") as file:
    data = json.load(file)


interfaces = data.get("imdata", [])

interface_list = []
for item in interfaces:
    attributes = item.get("l1PhysIf", {}).get("attributes", {})
    dn = attributes.get("dn", "N/A")  
    speed = attributes.get("speed", "inherit")  
    mtu = attributes.get("mtu", "N/A") 
    interface_list.append((dn, speed, mtu))


header = f"{'DN':<60} {'Description':<20} {'Speed':<10} {'MTU':<5}"
separator = "=" * len(header)

table_rows = [f"{dn:<60} {'':<20} {speed:<10} {mtu:<5}" for dn, speed, mtu in interface_list]

print(header)
print(separator)
for row in table_rows:
    print(row)
