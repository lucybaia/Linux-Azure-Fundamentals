# Linux & Azure Fundamentals 🐧☁️

This repository marks the first milestone of my DevOps Journey, focusing on Prerequisites and Infrastructure Provisioning.

## 🎯 Project Goal

To automate the creation and initial configuration of a Linux environment in the cloud, moving away from manual portal clicks to Infrastructure as Code (IaC) principles.

## 🛠️ Tech Stack

- **Cloud:** Microsoft Azure (Azure for Students)
- **Language:** Python 3.x (using `subprocess` for automation)
- **OS:** Ubuntu 22.04 LTS
- **CLI:** Azure CLI & Bash Scripting

## 🧠 DevOps Concepts Applied

- **OS & Linux Basics:** Managing a server via the Command Line Interface (CLI) and Shell commands.
- **Security:** Implementing SSH Key Management and configuring Firewalls via Network Security Groups (NSG) to secure access.
- **Automation:** Using a `setup.sh` script to handle post-provisioning tasks like system updates and essential tool installation (`git`, `curl`, `vim`).

## 🚀 How to Run

1. Log in to Azure: `az login`
2. Execute the provisioning script:
```bash
python scripts/create_vm.py
```

## Project Milestone: Automated Infrastructure Deployment

I successfully automated the provisioning of a Linux-based administration server on Azure using Python and the Azure SDK. This process involved the programmatically defined creation of a Resource Group, Virtual Network (VNet), and Network Security Group (NSG) to ensure a secure environment. During deployment, I encountered real-world Cloud Capacity challenges where the requested VM size was unavailable in certain regions (SkuNotAvailable). I resolved this by performing a regional failover and re-configuring the infrastructure deployment for a more stable availability zone. The attached screenshot demonstrates a successful SSH connection to the live Ubuntu 24.04 LTS instance, where I utilized core Linux utilities (uname, df, free) to verify that the hardware specifications and kernel were correctly provisioned according to the deployment script.

![Linux VM Verification](file:///C:/Users/DELL%20G15/Roadmap-Azure-DevOps/Linux-Azure-Fundamentals/images/azure-vm-screenshot.png)
*Figure 1: Verifying system resources and kernel version via SSH.*
