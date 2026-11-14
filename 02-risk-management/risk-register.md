# Information Security Risk Register

**Document ID:** ISMS-RSK-002  
**Scoring Methodology:** 5x5 Matrix (Likelihood 1–5 × Impact 1–5 = Risk Score 1–25)  
**Risk Acceptance Threshold:** Score ≤ 6 (Low)

## Risk Treatment Log

| Risk ID | Asset / Scope | Threat & Vulnerability | Inherent Risk (L×I) | Treatment Option | Mapped Annex A Controls | Residual Risk (L×I) | Risk Owner | Status |
| :--- | :--- | :--- | :---: | :---: | :--- | :---: | :--- | :--- |
| **RSK-01** | Production AWS Account | Compromised IAM credentials leading to unauthorized data access due to lack of MFA enforcement. | **20** (4×5) Critical | Mitigate | `A.5.15`, `A.5.17`, `A.8.5` (Enforce SSO + hardware MFA) | **5** (1×5) Low | Head of DevOps | Closed |
| **RSK-02** | Customer Database | Unencrypted backup snapshots exposed via misconfigured S3 bucket permissions. | **16** (4×4) High | Mitigate | `A.8.20`, `A.8.24` (Block public access + KMS encryption) | **4** (1×4) Low | Cloud Architect | Closed |
| **RSK-03** | Third-Party Vendors | Supply chain breach via unvetted SaaS sub-processor accessing customer metadata. | **15** (3×5) High | Mitigate | `A.5.19`, `A.5.20`, `A.5.21` (TPRM vetting & DPA review) | **6** (2×3) Low | GRC Lead | Monitoring |
| **RSK-04** | Employee Endpoints | Malware infection on remote laptops causing lateral movement into staging environments. | **12** (3×4) Medium | Mitigate | `A.8.1`, `A.8.7` (MDM enrollment & EDR deployment) | **4** (1×4) Low | IT Operations | Closed |
