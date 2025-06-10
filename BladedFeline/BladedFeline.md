**APT Overview**
------------

- **BladedFeline** is an **Iranian-aligned Advanced Persistent Threat (APT)** group focused on **cyberespionage**. Active since at least **2017**, BladedFeline has managed to remain clandestine within critical government and telecom networks in **Kurdistan**, **Iraq**, and **Uzbekistan** for nearly eight years while continuously expanding its cyberespionage capabilities.

  - Targeted Sectors: **Government, Telecommunications**.
- **BladedFeline’s operators** have been known to exploit **vulnerabilities in public-facing applications** to gain **initial access**, then use **custom backdoors** and **reverse tunnels** for **persistence** and **lateral movement**.
- **BladedFeline** deploys **custom malware** such as **Shahmaran**, **Whisper**, and **PrimeCache** to maintain long-term access and exfiltrate data.
- **ESET researchers** first identified that the group’s persistence was unmasked after the deployment of its signature backdoor, **Shahmaran**, against Kurdish diplomatic officials in early **2023**. This revelation revealed that the group had been hidden within the network for 8 years.
- Technical forensics further revealed that **BladedFeline** likely operates as a subgroup of the well-documented Iran-aligned **OilRig (APT34/Hazel Sandstorm)**, with overlapping code bases, tools, and tactical objectives.

### **BladedFeline Timeline**

---

- **September 2017**: First known activity, compromising systems in the **Kurdistan Regional Government (KRG)** using **VideoSRV** and **RDAT**.
- **2023**: **ESET** discovers BladedFeline through the deployment of the **Shahmaran backdoor** against Kurdish diplomatic officials.
- **2023**: Attack on a **telecommunications provider in Uzbekistan**, potentially compromised since **May 2022**.
- **2024**: Deployment of advanced tools including **Whisper**, **PrimeCache**, **Laret**, and **Pinar** in KRG and Iraqi government networks.
- **2024**: **PrimeCache** and **Whisper v2** uploaded to **VirusTotal**, indicating ongoing tool development.

### TTPs

| Stage                | Technique ID | Technique Name                                       | Description                                              |
| -------------------- | ------------ | ---------------------------------------------------- | -------------------------------------------------------- |
| Initial Access       | T1190        | Exploit Public-Facing Application                    | Exploits vulnerabilities in internet-facing web servers  |
| Execution            | T1059.001    | Command and Scripting Interpreter: PowerShell        | Uses PowerShell for execution and lateral movement       |
| Persistence          | T1547.001    | Boot or Logon Autostart Execution: Registry Run Keys | Deploys malware in Startup directories and registry keys |
|                      | T1053.005    | Scheduled Task/Job                                   | Creates scheduled tasks for persistence                  |
| Privilege Escalation | T1078        | Valid Accounts                                       | Uses compromised credentials for elevated access         |
| Defense Evasion      | T1070.006    | Timestomp                                            | Alters file timestamps to evade detection                |
|                      | T1222.002    | Linux File and Directory Permissions Modification    | Modifies permissions to hide malicious activity          |
| Discovery            | T1083        | File and Directory Discovery                         | Enumerates files and directories for targeting           |
|                      | T1082        | System Information Discovery                         | Collects OS and hardware details                         |
| Lateral Movement     | T1021.006    | Windows Remote Management                            | Uses WinRM for lateral movement                          |
| Exfiltration         | T1041        | Exfiltration Over C2 Channel                         | Sends data via command and control channels              |
| Impact               | T1490        | Inhibit System Recovery                              | Deletes backups and disables recovery tools              |

### **Custom Malware and Tools**

---

- **Shahmaran**: A **64-bit backdoor** deployed in the Startup directory for persistence. It enables command execution and data exfiltration.
- **Whisper**: A backdoor that uses **compromised Microsoft Exchange webmail accounts** for command and control (C&C) via email attachments.
- **PrimeCache**: A **malicious IIS module** with similarities to OilRig’s **RDAT backdoor**, used for maintaining access.
- **Laret and Pinar**: **Reverse tunnels** for persistent network access.
- **Flog**: A **webshell** used for initial access and persistence.
- **Hawking Listener**: A tool for maintaining long-term access to compromised systems.
- **VideoSRV and RDAT**: Shared with OilRig, used for espionage operations.
- **P.S. Olala**: A **PowerShell executor** for additional persistence.
- **Slippery Snakelet**: A **Python-based backdoor** for command execution.
- **Sheep Tunneler**: A tool for network tunneling.

### **References**

---

- https://www.welivesecurity.com/en/eset-research/bladedfeline-whispering-dark/
- https://www.darkreading.com/threat-intelligence/iranian-apt-bladedfeline-hides-network-8-years
- https://thehackernews.com/2025/06/iran-linked-bladedfeline-hits-iraqi-and.html
- https://gbhackers.com/iranian-apt-bladedfeline-remains-hidden/
- https://www.technadu.com/bladedfeline-campaign-unveiled-targeting-kurdish-and-iraqi-government-officials/598585/
- https://www.it-boltwise.de/iranische-hackergruppe-bladedfeline-zielt-auf-kurdische-und-irakische-regierungsstellen.html
- https://web-assets.esetstatic.com/wls/en/papers/threat-reports/eset-apt-activity-report-q4-2023-q1-2024.pdf
- https://web-assets.esetstatic.com/wls/en/papers/threat-reports/eset-apt-activity-report-q2-2024-q3-2024.pdf
