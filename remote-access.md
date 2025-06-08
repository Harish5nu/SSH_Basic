
# 🖥️ Remote Access Control - Windows

This note contains my learning from today's **Ethical Hacking class at Broadway Infosys**, focused on **Remote Access Control in Windows systems**.

---

## 🧠 What is Remote Access Control?

Remote Access Control allows you to **access and control another Windows machine** remotely over the network. It’s commonly used in:
- System Administration
- Remote Support
- Penetration Testing (as part of lateral movement)

---

## 📌 Key Topics Covered

### 🔹 1. Enabling Remote Desktop Protocol (RDP)
- On the target Windows machine:
  1. `Win + R` → type `SystemPropertiesRemote`
  2. Enable: **Allow remote connections to this computer**
  3. Ensure the firewall allows **RDP port 3389**

### 🔹 2. Adding a User to Remote Desktop Users
```bash
net localgroup "Remote Desktop Users" username /add
```

---

### 🔹 3. Connecting via RDP (Windows to Windows)
```cmd
mstsc
```
- Enter the **IP address** of the target machine.
- Login with the **remote user's credentials**.

---

### 🔹 4. Connecting via RDP (Linux to Windows)
On Kali Linux or other Linux distros:
```bash
xfreerdp /u:username /p:password /v:target_ip
```

Example:
```bash
xfreerdp /u:harry /p:Password123 /v:192.168.91.131
```

---

## 🔒 Security Concerns

- RDP is often targeted by brute-force attacks.
- Always use **strong passwords**.
- Consider using **VPNs**, **RDP Gateways**, or **Network Level Authentication (NLA)** for added security.

---

## 🧪 Tools Used

- Windows 10 / Windows 7 VM
- Kali Linux
- RDP Protocol (`mstsc`, `xfreerdp`)
- Network: Host-only or Bridged (via VirtualBox/VMware)



