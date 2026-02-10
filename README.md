## **Installation:**
To run this project you need to install following (We recommend you to create a virtual environment):

**Python-** 
There is a requirement file mentioned in `backend` folder so you need to install all the required libraries with command

`pip install -r requirements.txt`

To run the project we need to run 

`python run_project.py`

**For Angular-** 
Below packages needs to be installed.
- npm package manager
- Angular/cli
- node modules

After installation is done. Go to backend folder and run the command 
`python manage.py runserver`

This will start a Django backend server. 

For starting Angular Admin panel. Open `admin` folder and run following command (Make sure you have Angular and node packages installed)

`ng serve`

This will start frontend server. You can take URL from Terminal/Command Prompt. 

## Admin Login Details:
For logging in to Admin dashboard. Add `/admin_login.html` in URL bar after port number. Once there it will open login page. 

Admin Email - admin@agri.com
Password - admin

## For Customer Login - 
Below are the Customer Login details. You can create new user in Website by clicking on Sign Up or Create New User. Make sure that Password is at least 8 characters long, Contains at least 1 Capital letter and 1 lower case letter, and 1 special character. 

Current customers' credentials are as follow. 
Name - Ramesh Patil
Email - user1@example.com
Password - 123

Name - Suresh Kumar
Email - user2@example.com
Password - 123

Name - Anita Desai
Email - user3@example.com
Password - 123

Name - Farm Fresh Ltd
Email - user4@example.com
Password - 123

Name - Organic Basket
Email - user5@example.com
Password - 123






Project Specification: B2B Agricultural Marketplace

## **1. Problem Statement**

**The Challenge: Inefficiency and Rigidity in Agricultural Trading**
The current agricultural B2B landscape is fragmented. Farmers, Wholesalers, and Processors ("Customers") face significant barriers to efficient trading:

1.  **Geographical & Network Limitations:** Customers are largely restricted to their local networks or *mandis*, limiting their ability to find buyers or sellers nationwide who might offer better terms.
2.  **Lack of Price Optimization:** Without a competitive bidding environment, sellers often settle for the first available offer rather than the best market price. Conversely, buyers cannot easily compare rates from multiple sources.
3.  **Rigid Transaction Sizes:** Traditional trade often demands "all-or-nothing" deals. There is no streamlined digital mechanism for a large seller to fulfill their stock through multiple smaller buyers (partial fulfillment) without complex manual coordination.
4.  **Opaque Communication:** Finding a counter-party often involves layers of middlemen, preventing direct contact and negotiation between the actual buyer and seller.

**The Solution:**
A simplified, web-based platform that facilitates **direct B2B connections** through a transparent **bidding and negotiation engine**. The platform enables users to act interchangeably as buyers or sellers, democratizing access to the national market while allowing flexible, partial fulfillment of orders.

---

## **2. Core Logic & Business Rules**

### **A. User Roles & Visibility**
*   **Unified Role:** All users (Farmers, Wholesalers, Processors) are "Customers."
*   **Public Data:** Post Title, Category, Product, Quantity, Price, Customer Name, and Location (State/District) are visible to all users.
*   **Private Data:** Email and Phone Number are **hidden** until a bid is formally **Accepted**.

### **B. Inventory & Bidding Logic**
1.  **Placing a Bid:**
    *   Bidders input: **Price**, **Quantity**, and a **Message** (e.g., location details).
    *   *Validation:* Bid Quantity cannot exceed the Post's current available quantity.
    *   *Note:* Placing a bid **does not** reserve the stock. Multiple users can bid for the full amount simultaneously.

2.  **Acceptance & Partial Fulfillment:**
    *   **Action:** The Post Owner manually reviews bids and clicks "Accept."
    *   **Inventory Deduction:** Quantity is deducted from the Post **only when a bid is Accepted**.
    *   **Partial Logic:** A Post Owner can accept multiple smaller bids until the post quantity reaches 0.

3.  **Concurrency / Race Condition Handling:**
    *   *Scenario:* A Post has 10 Tons. User A bids for 10 Tons. User B bids for 10 Tons. Both bids are "Pending."
    *   *Outcome:* The Post Owner sees both. If the Owner accepts User A's bid:
        1.  Post Quantity becomes 0.
        2.  User A's Bid becomes "Accepted."
        3.  User B's Bid status automatically updates to **"INVALID"**.
    *   *System Check:* The system must prevent the Owner from accepting User B's bid after User A's bid has already consumed the stock.

4.  **The "Invalid Bid" State:**
    *   **Trigger:** When `Remaining Post Quantity` drops below a `Pending Bid Quantity`.
    *   **Action:** The system changes the bid status to **"INVALID"** and sends an **Email Notification** to the Bidder.
    *   **Restriction:** The Post Owner **cannot** accept an "Invalid" bid.
    *   **Resolution:** The Bidder must edit the bid (lowering quantity) or Cancel it.

### **C. Negotiation Flow**
1.  **Pending:** Bid placed; awaiting Owner action.
2.  **Accepted:** Owner accepts. Contact details exchanged. Quantity deducted.
3.  **Rejected:** Owner rejects. Bidder can submit a revised price/quantity.
4.  **Invalid:** Post quantity is insufficient for this bid.
5.  **Cancelled:** Withdrawn by the bidder.

### **D. Subscription & Listing Model**
*   **Free Tier:** 3 free posts per account.
*   **Paid Plans:** Users purchase plans to add more posts (e.g., 10 posts with 30-day posting validity).
*   **Plan Validity Rule:** Validity applies to the *ability to create new posts*.
    *   If a plan expires, the user cannot create new posts.
    *   **Existing posts remain active** indefinitely (until the user deletes them or stock is sold out).
    *   Users can edit existing posts without an active plan.

### **E. Notifications (MVP)**
*   **Channel:** Email Only (SMS/WhatsApp planned for future).
*   **Triggers:** New Bid, Bid Accepted (Unlock Contact Info), Bid Rejected, Bid Invalidated.

---

## **3. Search & Filters**
To ensure high liquidity and discoverability, the platform includes:
*   **Text Search:** By Product Name.
*   **Filters:**
    *   **Category** (Grains, Pulses, Spices, etc.)
    *   **Product** (Wheat, Soybeans, etc.)
    *   **Location** (State / District filtering)
    *   **Price Range** (Min / Max)

---

