# Serverless Credit Decision Engine 🏦

### Architecture Status: [ PRODUCTION ] 🟢
**Role:** Cloud Solutions Architect | **Tech Stack:** AWS Lambda, DynamoDB, SNS, Python, GitHub Actions

---

## 📖 Executive Summary
This project eliminates manual loan underwriting by implementing a fully automated, serverless risk engine. It accepts loan applications via API, evaluates creditworthiness against dynamic risk parameters, and issues real-time decisions (Approval/Rejection) with instant customer notification.

**Business Impact:**
* **Processing Time:** Reduced from days to <400 milliseconds.
* **Operational Cost:** $0 (Serverless Free Tier).
* **Availability:** High availability via Multi-AZ Serverless architecture.

---

## 🏗️ The Architecture

### 1. The Gatekeeper (Function URL)
* **Role:** Secure entry point for loan applications.
* **Protocol:** REST API (POST Request).
* **Payload:** Accepts JSON (`Income`, `LoanAmount`, `ApplicantID`).

### 2. The Underwriter (AWS Lambda - Python)
* **Role:** The core decision engine.
* **Logic:** Calculates Debt-to-Income (DTI) ratio.
    * *Rule:* If `Loan > (Salary * 3)` -> **DECLINE**.
    * *Rule:* If `Loan <= (Salary * 3)` -> **APPROVE**.
* **Traceability:** Logs every decision for audit purposes.

### 3. The Ledger (Amazon DynamoDB)
* **Role:** Immutable record keeping.
* **Data Model:** Stores `ApplicationID`, `Timestamp`, `Decision`, and `Amount`.
* **Performance:** Single-digit millisecond latency for writes.

### 4. The Messenger (Amazon SNS)
* **Role:** Customer communication.
* **Action:** Triggers immediate Email/SMS notifications based on the Lambda decision.

### 5. Automation (CI/CD)
* **Pipeline:** GitHub Actions.
* **Trigger:** Push to `main`.
* **Security:** OIDC authentication (No long-term credentials stored in repo).

---
**Author:** Dan Alwende
