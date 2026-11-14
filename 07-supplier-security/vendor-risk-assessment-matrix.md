# Third-Party Vendor Risk Assessment Matrix

**Document ID:** ISMS-VRM-001  
**Version:** 1.0  
**Owner:** Information Security Lead  
**Control Mapping:** ISO/IEC 27001:2022 Annex A.5.19 – A.5.22  
**Review Cycle:** Semi-Annual (Critical/High) / Annual (Medium/Low)  

---

## 1. Vendor Tiering Methodology
Suppliers are classified into risk tiers based on the sensitivity of data accessed and operational criticality to the CloudPulse SaaS platform:

- **Tier 1 (Critical):** Hosts, processes, or stores customer production/financial data, or provides core authentication/infrastructure. *Requires SOC 2 Type II or ISO 27001 certification, signed DPA, and semi-annual review.*
- **Tier 2 (High):** Processes employee PII or accesses internal corporate systems/source code. *Requires security questionnaire, signed DPA, and annual review.*
- **Tier 3 (Low):** No access to customer data or production networks (e.g., standalone marketing tools). *Standard terms review only.*

## 2. Approved Supplier Register & Due Diligence Log

| Vendor ID | Supplier Name | Service Provided | Data Classification | Risk Tier | Assurance Evidence Verified | DPA / SLA Signed | Residual Risk | Next Review Date |
| :--- | :--- | :--- | :--- | :---: | :--- | :---: | :---: | :---: |
| **VND-01** | Amazon Web Services (AWS) | Cloud infrastructure & production hosting (`eu-west-2`) | Customer Financial & PII | **Tier 1 (Critical)** | ISO/IEC 27001:2022 Cert, SOC 2 Type II Report, Shared Responsibility Review | Yes | Low | 2027-05-01 |
| **VND-02** | Okta | Enterprise Identity Provider (SSO & MFA) | Employee & Admin Credentials | **Tier 1 (Critical)** | ISO/IEC 27001 Cert, SOC 2 Type II, Penetration Test Summary | Yes | Low | 2027-05-01 |
| **VND-03** | GitHub | Source code hosting & CI/CD pipelines | Proprietary Source Code & Secrets | **Tier 1 (Critical)** | SOC 2 Type II Report, ISO/IEC 27001 Cert | Yes | Low | 2027-05-01 |
| **VND-04** | Plaid / TrueLayer | Open Banking payment initiation API | Customer Bank Metadata | **Tier 1 (Critical)** | FCA Registration, ISO/IEC 27001 Cert, TLS 1.3 & OAuth2 verification | Yes | Low | 2027-05-01 |
| **VND-05** | Rippling | HRIS & employee onboarding management | Employee PII & Payroll | **Tier 2 (High)** | SOC 2 Type II Report, Completed Vendor Security Questionnaire | Yes | Low | 2027-11-01 |
| **VND-06** | Slack | Internal team communications & alert routing | Internal Operational Data | **Tier 2 (High)** | ISO/IEC 27001 Cert, SOC 2 Type II, Retention & DLP settings verified | Yes | Low | 2027-11-01 |

## 3. Supplier Offboarding & Incident Escalation
- Upon contract termination, supplier API tokens and SSO integrations are revoked within **24 hours**, and written confirmation of data deletion is logged against the supplier record.
- All Tier 1 and Tier 2 DPAs mandate breach notification to CloudPulse Ltd within **24 to 48 hours** of discovery to support GDPR 72-hour regulatory reporting timelines.
