# Internal Audit Report & Corrective Action Log (CAPA)

**Document ID:** ISMS-AUD-001  
**Version:** 1.0  
**Audit Standard:** ISO/IEC 27001:2022 (Clauses 9.2 & 10.2)  
**Lead Internal Auditor:** Information Security Lead  
**Audit Period:** Q4 2026 (Stage 1 Readiness Audit)  
**Audited Scope:** CloudPulse Core SaaS Platform (`ISMS-SCP-001`)  

---

## 1. Executive Audit Summary (Clause 9.2)
An internal audit was conducted across Engineering, DevOps, and People Operations to evaluate conformity with ISO/IEC 27001:2022 requirements and CloudPulse Ltd's internal ISMS policies prior to Stage 1 external certification.

- **Overall Conclusion:** The ISMS is effectively designed and largely conformant. Two minor nonconformities and one opportunity for improvement (OFI) were identified and logged for corrective action.
- **Audit Methods:** Document review, AWS console/IaC configuration sampling, HR onboarding record inspection, and staff interviews.

| Finding Category | Count | Status |
| :--- | :---: | :--- |
| **Major Nonconformity** | 0 | N/A |
| **Minor Nonconformity** | 2 | 1 Closed, 1 In Progress |
| **Opportunity for Improvement (OFI)** | 1 | Open |

---

## 2. Audit Findings & Evidence Summary

| Clause / Control | Area Audited | Audit Evidence Reviewed | Result |
| :--- | :--- | :--- | :--- |
| **Clause 4.3 & 5.2** | ISMS Governance | Verified approved Scope Statement (`ISMS-SCP-001`) and Information Security Policy (`ISMS-POL-001`). | **Conformant** |
| **Clause 6.1.2** | Risk Management | Reviewed Risk Register (`ISMS-RSK-002`); risk owners and treatment plans are clearly assigned. | **Conformant** |
| **Annex A.5.18** | Access Rights | Sampled 15 user access reviews from Q3 2026; 2 contractor accounts lacked documented manager sign-off within the 30-day SLA. | **Minor NC-01** |
| **Annex A.6.3** | Security Awareness | Checked LMS completion logs; 58 of 60 employees completed annual training within 30 days of hire. 2 new hires were overdue by 10 days. | **Minor NC-02** |
| **Annex A.8.5** (Trace: [`RSK-04`](../02-risk-management/risk-register.md)) | Secure Authentication & Staging Access | Inspected Okta authentication policies and sampled 10 engineering user logins to staging AWS accounts; confirmed hardware/FIDO2 MFA is enforced and legacy password-only fallbacks are disabled. | **Conformant** |
| **Annex A.8.24** | Cryptography | Executed automated S3 encryption audit script (`check_aws_s3_encryption.py`); 100% of production buckets use SSE-KMS. | **Conformant** |
| **Annex A.8.15** | Logging & Monitoring | CloudTrail logs are centralized, though alert routing to Slack lacks severity tagging for low-priority events. | **OFI-01** |

---

## 3. Nonconformity & Corrective Action (CAPA) Log (Clause 10.2)

| Finding ID | Type & Clause | Finding Description | Root Cause Analysis | Corrective Action Plan | Owner & Due Date | Verification & Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **NC-01** | Minor NC (`A.5.18`) | 2 external contractor accounts in Okta were not reviewed during the Q3 quarterly access certification cycle. | Contractor accounts were tagged under a legacy HR group excluded from the automated Okta review workflow. | Update Okta user-group filter to include all `Contractor` roles and complete immediate access sign-off for both accounts. | IT Operations Lead (`2026-11-28`) | **Closed** – Verified updated Okta rule and signed review log on `2026-11-20`. |
| **NC-02** | Minor NC (`A.6.3`) | 2 new engineers exceeded the 30-day onboarding window for mandatory security awareness training. | Automated LMS reminder emails were blocked by a strict spam filter rule on newly provisioned email aliases. | Whitelist LMS sender domain in Google Workspace and enforce automated Slack reminders at Day 14 and Day 25. | People Ops Manager (`2026-12-05`) | **In Progress** – Whitelist applied; awaiting completion evidence for 2 staff. |
| **OFI-01** | OFI (`A.8.15`) | Security alert notifications in the `#sec-alerts` Slack channel do not visually distinguish between Medium and Low severity findings. | Default AWS EventBridge payload formatting did not map severity labels to Slack message blocks. | Update EventBridge input transformer to prefix alerts with `[HIGH]`, `[MEDIUM]`, or `[LOW]` severity tags. | DevOps Lead (`2026-12-15`) | **Open** – Tracked in backlog (`JIRA-509`). |

---

## 4. Continual Improvement Statement (Clause 10.1)
All corrective actions are tracked to closure and reviewed during the quarterly **Management Review Meeting (Clause 9.3)** to ensure root causes are eliminated and systemic controls improve over time.
