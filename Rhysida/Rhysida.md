
**Malware Overview**
----------------

- **Rhysida** is a **business ransomware-as-a-service** attack that **encrypts files** and **exfiltrates data** for **double extortion**.

  - Targeted Sectors **Healthcare, Government, Military, Education, Industrial, Technology and Sports**.
- **Rhysida’s operators** have been known to use **phishing attacks** as a means of gaining **initial access** then use **Cobalt Strike** to drop a **powershell script** for **lateral movement** in infected machines.
- **Rhysida ransomware** was using **PsExec** to deliver a script.

  - Detected as **SILENTKILL**, to **terminate antivirus programs**.
  - The **ransomware appends the .rhysida extension** and **turns off** recovery tools.
- **Rhysida** is use of **TOR-based portals** for **victim interaction**.

  - Its **leak site** hosted on the **dark web**, listing **victims** and **leaked data**
- **Cybersecurity and Infrastructure Security Agency (CISA)** released that there are some similarities between the group’s **tactics, techniques, and procedures (TTPs)** and those of another ransomware group called **Vice Society**.

### **Rhysida Timeline**

---

- **May 2023**: First seen for **Rhysida ransomware group** despite having likely been active since January of that year.
- **October 2023**: Attacked the online information systems of the **British Library**.
- **December 2023**: **Insomniac Games data dump**, releasing details of the **Marvel's Wolverine game** and **employee details**.
- **May 2024**, **Rhysida breached the Chilean Army** via a **phishing attack**, stealing and leaking approximately **360,000 documents**.
- **July 2024**: Attack on **city of Columbus, Ohio** where over **3 TB of data** was released onto the **dark web**, after an attempt to extort **$1.7M (30 Bitcoin)**.
- **August 2024**: Attack on **Seattle-Tacoma International Airport**.
- **November 2024**: Attack on **Rutherford County Schools (Tennessee)**.
- **December 2024**: **Pembina Trails School Division**.

### **Country of Origin**

---

The group may be based in the **Commonwealth of Independent States** is a regional intergovernmental organization **in Eurasia.**

### **Rhysida infrastructure**

---

Regarding to **Recorded future report**, The group is **Multi-tiered Infrastructure** as being composed of three layers:

- **First**:  Used for for**malvertising-based delivery payload delivery**.
- **Second**: Used for the**post-infection handling** and **command-and-control(C2) communications**.
- **Third**:  The **higher-tier management infrastructure** which includes the **admin panel** and a **Zabbix server** for **infrastructure monitoring**.

### TTPs

| Stage                | Technique ID | Technique Name                                    | Description                                             |
| -------------------- | ------------ | ------------------------------------------------- | ------------------------------------------------------- |
| Initial Access       | T1566.001    | Spearphishing Attachment                          | Uses phishing emails with attachments to gain access    |
| Execution            | T1059.001    | Command and Scripting Interpreter                 | Uses PowerShell to execute commands                     |
| Persistence          | T1053.005    | Scheduled Task/Job                                | Creates a task named `Rhsd` to run malware at startup |
|                      | T1112        | Modify Registry                                   | Alters registry keys to drop the ransom note            |
| Privilege Escalation | T1098        | Account Manipulation                              | Modifies Active Directory passwords                     |
| Defense Evasion      | T1070.004    | File Deletion                                     | Deletes itself after execution                          |
|                      | T1222.002    | Linux File and Directory Permissions Modification | Changes file permissions to display ransom note         |
| Discovery            | T1083        | File and Directory Discovery                      | Enumerates files for encryption                         |
|                      | T1082        | System Information Discovery                      | Collects OS and hardware details                        |
| Lateral Movement     | T1021.006    | Windows Remote Management                         | Uses WinRM for lateral movement                         |
| Exfiltration         | T1041        | Exfiltration Over C2 Channel                      | Sends data via command and control channels             |
| Impact               | T1490        | Inhibit System Recovery                           | Deletes shadow copies and backups                       |
|                      | T1486        | Data Encrypted for Impact                         | Encrypts data using RSA-4096 and AES                    |

### **Automated Victim Scraping Script**

---

- Python script to automate the scraping of Rhysida's dark web leak site (DLS) and extract the list of published victims.
- The script uses Selenium with **Tor SOCKS** proxy (9050/9150) to access **.onion** sites.
- It parses the HTML using BeautifulSoup to **extract** victim names, descriptions, time listed, and number of leaked files.
- The script automatically retries with an alternate port (9150) if the default one (9050) fails.

### **References**

---

https://www.sentinelone.com/anthology/rhysida/

https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a

https://www.trendmicro.com/vinfo/us/security/news/ransomware-spotlight/ransomware-spotlight-rhysida

https://en.wikipedia.org/wiki/Rhysida_(hacker_group)

https://www.picussecurity.com/resource/blog/rhysida-ransomware-explained

https://www.fortinet.com/content/dam/fortinet/assets/threat-reports/rhysida-ransomware-intrusion.pdf

https://www.recordedfuture.com/research/outmaneuvering-rhysida-advanced-threat-intelligence-shields-critical-infrastructure-ransomware

https://www.avertium.com/resources/threat-reports/an-in-depth-look-at-rhysida-ransomware

https://blog.barracuda.com/2024/05/09/rhysida-ransomware--the-creepy-crawling-criminal-hiding-in-the-d
