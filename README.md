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
