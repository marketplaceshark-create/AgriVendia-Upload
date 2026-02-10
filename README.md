# Author details:
Name - 

Email - 


***

# Agrivendia - B2B Agricultural Marketplace 

Agrivendia is a B2B agricultural trading platform designed to connect Farmers, Wholesalers, and Processors.

1.  **AngularJS Implementation:** A complete User Storefront and Admin Dashboard using the MVC pattern.
2.  **Angular (v21) Implementation:** A component-based Admin Panel using the modern Angular ecosystem.

---

## 🛠 Tech Stack

### Backend
*   **Framework:** Python Django 6.0.2
*   **API:** Django Rest Framework (DRF) 3.16.1
*   **Database:** SQLite (Pre-populated)

### Frontend Option 1 (AngularJS)
*   **Framework:** AngularJS 1.8.2
*   **Scope:** Customer Storefront + Admin Dashboard
*   **Tech:** HTML5, CSS3, JavaScript

### Frontend Option 2 (Angular)
*   **Framework:** Angular 21.1.0
*   **Scope:** Admin Panel Only
*   **Runtime:** Node.js & npm

---

## 📝 1. Installing Pre-requisites

Since this project does not include library files (node_modules, venv, etc.), you must install the necessary tools on your computer first.

### A. Python (For Backend)
1.  Download Python (version 3.10 or higher) from [python.org](https://www.python.org/downloads/).
2.  **Important during installation:** Check the box that says **"Add Python to PATH"** before clicking Install.
3.  Verify installation by opening a terminal/command prompt and typing:
    ```bash
    python --version
    ```

### B. Node.js & npm (For Angular Frontend)
1.  Download the **LTS (Long Term Support)** version of Node.js from [nodejs.org](https://nodejs.org/).
2.  Install it using the default settings.
3.  Verify installation:
    ```bash
    node -v
    npm -v
    ```

### C. Angular CLI (For Angular Frontend)
Once Node.js is installed, you need the Angular Command Line Interface to build the project.
1.  Open your terminal/command prompt.
2.  Run the following command:
    ```bash
    npm install -g @angular/cli
    ```

---

## ⚙️ 2. Project Installation

Follow these steps to set up the project folders.

### Step A: Backend Setup
1.  Open your terminal and navigate to the `backend` folder inside the project.
    ```bash
    cd backend
    ```
2.  **Create a Virtual Environment** (This keeps Python libraries isolated):
    ```bash
    python -m venv venv
    ```
3.  **Activate the Virtual Environment**:
    *   **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    *   **Mac/Linux:**
        ```bash
        source venv/bin/activate
        ```
    *(You should see `(venv)` appear at the start of your command line)*.
4.  **Install Required Libraries**:
    ```bash
    pip install -r requirements.txt
    ```

### Step B: Angular Admin Setup
1.  Open a **new** terminal window.
2.  Navigate to the `admin` folder:
    ```bash
    cd admin
    ```
3.  **Install Node Modules**:
    Run the following command. This will automatically read the `package.json` file and install all required Angular dependencies.
    ```bash
    npm install
    ```

---

## ▶️ 3. Running the Project

To use the full system, you must run the Backend and at least one Frontend.

### Terminal 1: Start Backend (Required)
The backend serves the API and the Database.
```bash
cd backend
# Ensure venv is activated
python manage.py runserver
```
*   **Server Status:** Running at `http://127.0.0.1:8000/`

### Terminal 2: Start AngularJS Frontend (Storefront)
This is the main website for Customers.
```bash
cd frontend
python -m http.server 8080
```
*   **Access:** Open Browser to `http://127.0.0.1:8080/`

### Terminal 3: Start Angular Frontend (Admin Panel)
This is the dedicated Admin portal.
```bash
cd admin
ng serve
```
*   **Access:** Open Browser to `http://localhost:4200/`

---

## 🔑 4. Login Credentials

The database is pre-loaded with the following accounts. You can use these to log in immediately.

### 🛡️ Admin Login
*Works on both the AngularJS Dashboard (`/admin_login.html`) and the Angular Admin Panel (`localhost:4200`).*

*   **Email:** `admin@agri.com`
*   **Password:** `admin`

### 👤 Customer Login
*Use these on the AngularJS Storefront (`/login.html`).*

**Customer 1 (Farmer/Seller)**
*   **Name:** Ramesh Patil
*   **Email:** `user1@example.com`
*   **Password:** `123`

**Customer 2 (Buyer/Trader)**
*   **Name:** Suresh Kumar
*   **Email:** `user2@example.com`
*   **Password:** `123`

**Customer 3 (Processor)**
*   **Name:** Anita Desai
*   **Email:** `user3@example.com`
*   **Password:** `123`

**Customer 4 (Corporate)**
*   **Name:** Farm Fresh Ltd
*   **Email:** `user4@example.com`
*   **Password:** `123`

---

## 📂 Project Structure Overview

*   **/backend**
    Contains the Django API, `db.sqlite3` (Database), and media files (images).
*   **/frontend**
    Contains the AngularJS implementation. This folder uses `app.js` and standard HTML files.
*   **/admin**
    Contains the Angular (v21) implementation. This folder contains `src/`, `package.json`, and TypeScript files.
*   **run_project.py**
    A helper script in the root directory that can launch the Backend and the AngularJS frontend simultaneously (optional).

---

## ⚠️ Troubleshooting

1.  **"command not found: ng"**:
    *   This means Angular CLI didn't install correctly. Re-run `npm install -g @angular/cli` and restart your terminal.

2.  **Images not loading**:
    *   The frontend looks for images at `http://127.0.0.1:8000/Media/`. Ensure the Django backend (Terminal 1) is running.

3.  **Port errors (Address already in use)**:
    *   Ensure you aren't running the server in multiple terminals.
    *   Django uses port **8000**.
    *   AngularJS uses port **8080**.
    *   Angular uses port **4200**.
