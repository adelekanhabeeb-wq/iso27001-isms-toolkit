# iso27001-isms-toolkit
---
title: Home & Overview
nav_order: 1
---

# ISO/IEC 27001:2022 ISMS Implementation Toolkit
...

A structured, version-controlled Information Security Management System (ISMS) repository built around a fictional case study: **CloudPulse Ltd**, a 60-person B2B FinTech SaaS provider operating on AWS.

This repository demonstrates how core ISO/IEC 27001:2022 artefacts can be maintained as **Governance-as-Code** using Markdown and Git to satisfy Clause 7.5 (Documented Information) requirements.

## 📂 Repository Structure

- `01-context-and-scope/` – ISMS Scope Statement and Interested Parties register (Clauses 4.1–4.3)
- `02-risk-management/` – Risk Assessment Methodology and Risk Treatment Register (Clauses 6.1.2–6.1.3)
- `03-statement-of-applicability/` – ISO/IEC 27001:2022 Statement of Applicability (SoA) across all 93 Annex A controls (Clause 6.1.3 d)
- `04-policies/` – Core Information Security Policy and access control standards (Clause 5.2)
- `06-audit-and-improvement/ – Internal Audit Report and Corrective Action (CAPA) Log (Clauses 9.2, 10.1 & 10.2)
- `07-supplier-security/ – Third-Party Vendor Risk Assessment Matrix and Tiering Methodology (Annex A.5.19–A.5.22)

## 🎯 Key Highlights

- **Aligned to ISO/IEC 27001:2022:** Reflects the updated 4-theme structure (Organizational, People, Physical, and Technological controls) including new 2022 controls such as Threat Intelligence (`A.5.7`), Cloud Services Security (`A.5.23`), and Data Masking (`A.8.11`).
- **Audit-Ready Traceability:** Links identified risks directly to Annex A controls and technical evidence.
- **Version Controlled:** Uses Git commit history to track policy approvals, annual reviews, and owner sign-offs.
