01-context-and-scope/scope-statement.md → title: 1. ISMS Scope (Clause 4.3) and nav_order: 2

# Information Security Management System (ISMS) Scope Statement

**Document ID:** ISMS-SCP-001  
**Version:** 1.0  
**Owner:** Information Security Lead  
**Approved By:** Chief Executive Officer (CEO) & Chief Technology Officer (CTO)  
**Review Cycle:** Annual  

---

## 1. Purpose
This document defines the organizational, technological, and physical boundaries of the Information Security Management System (ISMS) for **CloudPulse Ltd**, in accordance with **Clause 4.3 of ISO/IEC 27001:2022**.

## 2. Organizational Context (Clause 4.1)
CloudPulse Ltd is a 60-person B2B Financial Technology (FinTech) Software-as-a-Service (SaaS) provider delivering automated cash-flow forecasting and payment reconciliation tools to enterprise clients across the UK and European Economic Area (EEA).

### Key Internal & External Issues
- **Internal:** 100% remote workforce, rapid CI/CD software deployment cycles, and heavy reliance on cloud-native infrastructure.
- **External:** Strict regulatory scrutiny under UK GDPR, EU GDPR, and Financial Conduct Authority (FCA) operational resilience expectations, alongside rising enterprise client vendor due diligence requirements.

## 3. Interested Parties & Requirements (Clause 4.2)

| Interested Party | Key Security, Legal & Contractual Requirements |
| :--- | :--- |
| **Enterprise Customers** | High platform availability (99.9% SLA), encryption of financial data in transit and at rest, and annual third-party audit assurance. |
| **Regulators (ICO, FCA)** | Compliance with UK/EU GDPR data protection principles, breach notification within 72 hours, and operational resilience. |
| **Employees & Contractors** | Clear acceptable use guidelines, secure remote working tools, and role-based access controls. |
| **Cloud & SaaS Suppliers** | Adherence to signed Data Processing Agreements (DPAs) and shared security responsibility boundaries. |
| **Board & Investors** | Measurable risk reduction, protection of intellectual property, and timely ISO/IEC 27001 certification. |

## 4. ISMS Scope Definition (Clause 4.3)

### 4.1 In-Scope Services & Processes
The ISMS covers the **design, development, deployment, maintenance, and customer support** of the **CloudPulse Core SaaS Platform**, including all supporting corporate IT and HR operations.

### 4.2 In-Scope Organizational Units
- **Engineering & Product:** Software development, DevOps, site reliability engineering (SRE), and quality assurance.
- **Information Security & GRC:** Risk management, compliance, vulnerability management, and incident response.
- **Customer Success & Support:** Technical onboarding and tier 1–3 customer support operations.
- **People & Corporate Operations:** Employee onboarding/offboarding, background screening, and corporate IT administration.

### 4.3 In-Scope Technology & Infrastructure
- **Cloud Production & Staging Environments:** Amazon Web Services (AWS) hosted in the `eu-west-2` (London) and `eu-west-1` (Ireland) regions.
- **Source Code & CI/CD Pipelines:** GitHub Enterprise repositories, GitHub Actions workflows, and container registries.
- **Corporate Identity & Endpoint Fleet:** Google Workspace, Okta Single Sign-On (SSO), and company-managed macOS/Windows endpoints enrolled in Mobile Device Management (MDM).

### 4.4 Physical Locations & Boundaries
- **Remote Workforce:** CloudPulse Ltd operates as a fully remote organization with no permanent corporate offices.
- **Physical Data Centres:** All production infrastructure is hosted by AWS. Physical and environmental security controls at data centre facilities are managed by AWS under the Shared Responsibility Model and verified annually via AWS SOC 2 Type II and ISO/IEC 27001 certifications.

## 5. Exclusions & Interfaces
- **Out-of-Scope Systems:** Marketing website (`://example.com`) hosted on a standalone static CMS that processes no customer production data and has no network connectivity to the core SaaS environment.
- **Interfaces & Dependencies:** Payment initiation APIs rely on regulated Open Banking third-party providers. All data transfers across this interface are encrypted via TLS 1.3 and governed by formal supplier agreements (`Annex A.5.19–A.5.22`).

## 6. Document Approval & Revision History

| Version | Date | Author | Summary of Changes |
| :---: | :---: | :--- | :--- |
| 1.0 | 2026-11-14 | Information Security Lead | Initial ISMS Scope Statement approved for ISO/IEC 27001:2022 implementation. |
