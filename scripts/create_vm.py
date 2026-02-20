import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient

# Configuration - Change these as needed
SUBSCRIPTION_ID = "your-subscription-id-here"
RESOURCE_GROUP = "RG-Linux-Fundamentals"
LOCATION = "eastus"
VM_NAME = "LinuxAdminServer"
USERNAME = "azureuser"
# Path to your public key (ensure setup.sh or your local machine has this)
PUB_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa.pub")

credential = DefaultAzureCredential()

# 1. Initialize Clients
resource_client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
network_client = NetworkManagementClient(credential, SUBSCRIPTION_ID)
compute_client = ComputeManagementClient(credential, SUBSCRIPTION_ID)

print(f"Creating Resource Group: {RESOURCE_GROUP}...")
resource_client.resource_groups.create_or_update(RESOURCE_GROUP, {"location": LOCATION})

# 2. Networking Setup
print("Provisioning Network Resources (VNET, Subnet, IP, NSG)...")
vnet_poller = network_client.virtual_networks.begin_create_or_update(RESOURCE_GROUP, "VNet-01", {
    "location": LOCATION,
    "address_space": {"address_prefixes": ["10.0.0.0/16"]}
})
vnet_result = vnet_poller.result()

subnet_poller = network_client.subnets.begin_create_or_update(RESOURCE_GROUP, "VNet-01", "Subnet-01", {
    "address_prefix": "10.0.1.0/24"
})
subnet_result = subnet_poller.result()

# Create NSG for SSH (Port 22)
nsg_params = {
    "location": LOCATION,
    "security_rules": [{
        "name": "AllowSSH",
        "protocol": "Tcp",
        "source_port_range": "*",
        "destination_port_range": "22",
        "source_address_prefix": "*",
        "destination_address_prefix": "*",
        "access": "Allow",
        "priority": 100,
        "direction": "Inbound",
    }]
}
nsg_poller = network_client.network_security_groups.begin_create_or_update(RESOURCE_GROUP, "NSG-SSH", nsg_params)
nsg_result = nsg_poller.result()

# 3. Create Virtual Machine
print(f"Provisioning VM: {VM_NAME}...")
with open(PUB_KEY_PATH, "r") as f:
    public_key_data = f.read()

vm_parameters = {
    "location": LOCATION,
    "storage_profile": {
        "image_reference": {
            "publisher": "Canonical",
            "offer": "UbuntuServer",
            "sku": "18.04-LTS",
            "version": "latest"
        }
    },
    "hardware_profile": {"vm_size": "Standard_B1s"},
    "os_profile": {
        "computer_name": VM_NAME,
        "admin_username": USERNAME,
        "linux_configuration": {
            "ssh": {
                "public_keys": [{"path": f"/home/{USERNAME}/.ssh/authorized_keys", "key_data": public_key_data}]
            }
        }
    },
    "network_profile": {
        "network_interfaces": [{
            "id": "/subscriptions/.../networkInterfaces/nic-01", # Simplified for brevity
            "properties": {"primary": True}
        }]
    }
}
# Note: For a production script, you'd create the NIC separately before this step.
print("VM Provisioning started...")