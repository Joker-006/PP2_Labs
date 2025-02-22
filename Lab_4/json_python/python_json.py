import json
# Reading a JSON file
with open('sample-data.json', 'r') as file:
    data = json.load(file)

# Title
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-" * 80)

# Iterating through interfaces and outputting information
for interface in data['interfaces']:
    dn = interface.get('dn', 'N/A')
    description = interface.get('description', 'N/A')
    speed = interface.get('speed', 'N/A')
    mtu = interface.get('mtu', 'N/A')
    
    print(f"{dn:<50} {description:<20} {speed:<6} {mtu:<6}")