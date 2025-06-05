
# 🔐 SSH for Beginners

Welcome to the beginner guide for **SSH (Secure Shell)**. This guide is ideal for students, beginners in cybersecurity, or anyone getting started with remote server access.

---

## 📌 What is SSH?

**SSH (Secure Shell)** is a cryptographic network protocol used to securely connect to a remote machine over an unsecured network.

It provides:
- Encrypted communication
- Remote command-line access
- File transfers (SCP/SFTP)
- Port forwarding

---

## 🧠 How SSH Works?

Here's a visual explanation of how SSH works internally (Credits: ByteByteGo):

![How SSH Works](./ssh.gif)

**Key Steps:**
1. TCP connection established
2. Version & algorithm negotiation
3. Key pairs generated
4. Public key shared
5. Server validates against `~/.ssh/authorized_keys`
6. Session key is calculated
7. Secure encrypted session begins

---

## 🧪 Common SSH Commands

### 🔗 Basic SSH Connection
```bash
ssh username@ip_address
```

Example:
```bash
ssh msfadmin@192.168.91.131
```

If you're facing a key algorithm error (common in older systems):
```bash
ssh msfadmin@192.168.91.131 -oHostKeyAlgorithms=+ssh-rsa
```

---

### 🛠️ Start/Stop SSH Service (Linux)

Start the SSH service:
```bash
sudo service ssh start
```

Stop the SSH service:
```bash
sudo systemctl stop ssh
```

Check SSH status:
```bash
sudo systemctl status ssh
```

---

## 🔐 Key-Based Authentication

### 1. Generate SSH Key Pair
```bash
ssh-keygen
```

### 2. Copy the Public Key to the Server
```bash
ssh-copy-id username@ip_address
```

This appends the public key to the server's:
```
~/.ssh/authorized_keys
```

---

## 🚪 SSH Port Forwarding

To forward local port `p1` to server port `p2`:
```bash
ssh -L p1:server:p2 username@remote
```

**Example**:
```bash
local$ ssh -L 8080:192.168.91.131:80 msfadmin@192.168.91.131
```

---

## 🧰 Tips & Troubleshooting

- Ensure `openssh-server` is installed on your server.
- If you face `Permission denied`, check:
  - Correct username?
  - Is SSH running?
  - Are you using the right key?
- You can restart SSH to refresh configuration.

---

## 📚 Resources

- [SSH Manual (man ssh)](https://man.openbsd.org/ssh)
- [TryHackMe SSH Room](https://tryhackme.com)

---

> ✅ SSH is essential in the world of Linux, DevOps, and Cybersecurity. Practice it regularly to master remote systems.

---

### 🧑‍💻 Author
Maintained by Harish Saud
