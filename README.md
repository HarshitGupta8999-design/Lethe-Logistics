# Lethe-Logistics

**Organization:** Lethe Logistics  
**Project Scope:** MCA Semester Project - Database Management Systems  
**Tech Stack:** Supabase (PostgreSQL), GitHub, Python, DBeaver  

---

## Overview
Lethe-Logistics is a relational database designed to manage the lifecycle of pharmaceutical products. While most systems focus on sales, this project addresses the one of the hardest parts that is implementation of **Reverse Logistics**—the specialized process of tracking expired or recalled medications throughout the entire process.

### Core Features to achieve
To satisfy the complexity requirement, we have moved beyond simple CRUD operations. Our system implements:
* **Batch-Level Traceability:** Mapping every transaction to a specific `Batch_ID`.
* **State Management:** Handling "Quarantine," "Recall," and "Disposal" statuses.
* **Regulatory Compliance:** Automated `Disposal_Logs` to ensure expired goods are never re-sold.

---

## Database Blueprint (18 Tables)
The system has five logical modules:

1.  **Master Data:** `Roles`, `Users`, `Suppliers`, `Manufacturers`, `Retailers`.
2.  **Product & Production:** `Raw_Materials`, `Drug_Categories`, `Medicines`, `Batches`.
3.  **Inventory:** `Stock_Inventory`, `Warehouses`, `Quality_Checks`.
4.  **Forward Logistics:** `Orders`, `Order_Items`, `Shipments`.
5.  **Reverse Logistics:** `Return_Requests`, `Return_Items`, `Disposal_Logs`.

---

## Rules
All schema changes must be versioned and pushed via GitHub before being applied to the shared Supabase instance.

### Role Assignments

Not decided yet.

---

## Team Members :

Ram Sankar S


Nishit Gupta


Shivam Kumar


Shiwangi Priya

Vanshita Mandloi
## Instructions for Team Members

### 1. Repository Setup
Ensure your SSH keys are configured for GitHub.
```bash
git clone git@github.com:[YOUR_ORG]/lethe-logistics.git
cd lethe-logistics

