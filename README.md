# Serverless Credit Decision Engine 🏦

### **Project Status: PRODUCTION-READY 🟢**

**Author:** Dan Alwende
**Architecture:** Event-Driven Serverless
**Tech Stack:** AWS (S3, Lambda, DynamoDB, SNS), Python, JavaScript, GitHub Actions

---

## 📖 Project Overview

This project is a fully automated lending infrastructure designed to eliminate manual credit underwriting. It captures applicant data via a web portal, evaluates financial risk using a serverless decision engine, and persists the audit trail in a NoSQL database—all in under 400ms.

## 🏗️ Technical Architecture

![Architecture Flowchart](assets/architecture-flowchart.jpg)

### **1. Presentation Layer (Amazon S3)**
* **Component:** Static Website Hosting.
* **Implementation:** Responsive HTML5/CSS3/JS portal.

### **2. Logic Layer (AWS Lambda)**
* **Component:** Python Decision Engine.
* **Security:** CORS enabled for secure communication with the frontend.

### **3. Data Layer (Amazon DynamoDB)**
* **Component:** NoSQL Database.
* **Function:** Stores immutable records of every transaction for auditing.

---

## 🧪 Execution Proof

Below is the validation of the system's decision-making logic:

### **Lending Decision: APPROVED**
![Test Approved](assets/test-approved.jpeg)

### **Lending Decision: DECLINED**
![Test Declined](assets/test-declined.jpeg)

---

## 📉 Performance Metrics

* **Latency:** <400ms end-to-end decisioning.
* **Cost:** $0.00 (Operates entirely within the AWS Free Tier).
* **Scalability:** Inherently scales to thousands of concurrent applications.
