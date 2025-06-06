
# 🛠️ Service Checker + SSH for Beginners

Welcome! This repository contains:

1. A **simple Python script** to check if SSH or Telnet is open on a remote system.
2. A **beginner-friendly guide** to understanding and using SSH.

---

## 📌 1. Service Checker Script

A lightweight script written in Python to check if **Telnet (port 23)** and **SSH (port 22)** are open on a given IP.

### 🐍 How to Use:

```bash
python3 service_checker.py
```

Enter the target IP address when prompted:

```
Enter target IP address: 192.168.1.1
```

### ⚙️ Requirements:

- Python 3  
(No external libraries needed)

### 🛡️ Note:

- Telnet is outdated and insecure. Disable it if not needed.
- SSH is secure but must be properly configured.

---

## 🔐 2. SSH for Beginners

Welcome to the beginner guide for **SSH (Secure Shell)**. This is ideal for students, beginners in cybersecurity, or anyone starting with remote server access.

### 📌 What is SSH?

**SSH (Secure Shell)** is a secure protocol for accessing remote machines over an unsecured network.

It provides:
- Encrypted communication
- Remote terminal access
- File transfers (SCP/SFTP)
- Port forwarding

---

### 🧠 How SSH Works?

Here's a visual explanation of SSH (Credits: ByteByteGo):

![How SSH Works](./ssh.gif)

Key steps:
1. TCP connection is created
2. Algorithm negotiation
3. Key exchange & validation
4. Session key setup
5. Secure session begins

---

### 🧪 Common SSH Commands

#### 🔗 Basic SSH Connection

```bash
ssh username@ip_address
```

Example:
```bash
ssh msfadmin@192.168.91.131
```

If you face a key algorithm error (in older systems):
```bash
ssh msfadmin@192.168.91.131 -oHostKeyAlgorithms=+ssh-rsa
```

---

#### 🛠️ Start/Stop SSH Service (Linux)

```bash
sudo service ssh start     # Start SSH
sudo systemctl stop ssh    # Stop SSH
sudo systemctl status ssh  # Check SSH status
```

---

### 🔐 Key-Based Authentication

1. Generate SSH key pair:
```bash
ssh-keygen
```

2. Copy public key to server:
```bash
ssh-copy-id username@ip_address
```

This adds it to:
```
~/.ssh/authorized_keys
```

---

### 🚪 SSH Port Forwarding

Forward local port `p1` to a remote server's port `p2`:

```bash
ssh -L p1:server:p2 username@remote
```

Example:
```bash
ssh -L 8080:192.168.91.131:80 msfadmin@192.168.91.131
```

---

### 🧰 Tips & Troubleshooting

- Make sure `openssh-server` is installed on the server.
- If `Permission denied` error occurs:
  - Check username
  - Ensure SSH is running
  - Use correct key or password
- Restart SSH to reload config changes.

---

## 📚 Resources

- [SSH Manual (man ssh)](https://man.openbsd.org/ssh)
- [TryHackMe SSH Room](https://tryhackme.com)

---

> ✅ SSH is essential in the world of Linux, DevOps, and Cybersecurity. Practice regularly to master it.

---

### 🧑‍💻 Author

Maintained by **Harish Saud**  
Ethical Hacking Trainee @ Broadway Infosys  
TryHackMe Streak: 118+ days | GitHub Streak: 98+ days  
