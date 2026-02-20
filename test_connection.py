from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import os

# Try to get subscription ID from environment or paste it here
SUBSCRIPTION_ID = "c9e3892b-6798-439c-9848-e0a20a37970c"

try:
    credential = DefaultAzureCredential()
    client = ResourceManagementClient(credential, SUBSCRIPTION_ID)
    
    # List Resource Groups as a simple test
    print("Connecting to Azure...")
    groups = client.resource_groups.list()
    print("Connection Successful! Your Resource Groups:")
    for group in groups:
        print(f" - {group.name}")

except Exception as e:
    print(f"Connection Failed: {e}")