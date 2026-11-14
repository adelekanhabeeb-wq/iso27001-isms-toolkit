# Statement of Applicability (SoA) – ISO/IEC 27001:2022

**Document ID:** ISMS-SOA-001  
**Version:** 1.0  
**Owner:** Information Security Lead  
**Approved By:** Chief Technology Officer (CTO)  
**Review Cycle:** Annual  

## 1. Purpose
This Statement of Applicability defines the ISO/IEC 27001:2022 Annex A controls applicable to **CloudPulse Ltd's** core SaaS platform, along with justifications for inclusion or exclusion and current implementation status.

## 2. Summary by Control Theme

| Theme | Total Controls | Applicable | Excluded |
| :--- | :---: | :---: | :---: |
| **A.5 Organizational Controls** | 37 | 37 | 0 |
| **A.6 People Controls** | 8 | 8 | 0 |
| **A.7 Physical Controls** | 14 | 5 | 9 |
| **A.8 Technological Controls** | 34 | 33 | 1 |
| **Total** | **93** | **83** | **10** |

## 3. Sample Control Mapping (Selected Controls)

| Control ID | Control Title | Applicable | Justification for Inclusion / Exclusion | Implementation Status | Evidence / Reference |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **A.5.1** | Policies for information security | Yes | Required to establish management direction and support for security. | Implemented | `POL-001 Information Security Policy` |
| **A.5.7** | Threat intelligence | Yes | Required to monitor emerging cloud and FinTech vulnerabilities proactively. | Implemented | AWS GuardDuty & NCSC Cyber Alerts feed |
| **A.5.23** | Information security for use of cloud services | Yes | Core SaaS production environment is hosted entirely on AWS. | Implemented | `STD-004 Cloud Security Standard` |
| **A.6.3** | Information security awareness, education and training | Yes | Reduces human error and phishing risk across remote workforce. | Implemented | Annual security training logs |
| **A.7.1** | Physical security perimeters | No | **Excluded:** CloudPulse operates 100% remotely with no corporate offices or on-premise data centres. AWS manages physical security under the Shared Responsibility Model. | N/A | AWS SOC 2 Type II Report |
| **A.8.9** | Configuration management | Yes | Prevents security drift across production containers and cloud infrastructure. | Implemented | Terraform IaC & AWS Config rules |
| **A.8.11** | Data masking | Yes | Protects customer PII in staging and analytics environments. | In Progress | Database anonymisation pipeline (`JIRA-412`) |
| **A.8.28** | Secure coding | Yes | Essential to prevent OWASP Top 10 vulnerabilities in SaaS product. | Implemented | GitHub Actions SAST & peer code review |
