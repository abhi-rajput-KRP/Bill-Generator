# Bill-Generator

Bill Generating and Inventory Management System is a software used
to comfort the shopkeeper or any one running their commercial entity ,
which allows them to seamlessly manage their data of their products
with their prices , and vendors and also allows them to generate the bill
for the customer to manage their billing task comfortably. With all this
It also allows shopkeepers to add new vendors and to maintain the
record of dues and payments of each vendor.
---
## Here are some features of this Bill-Managemengt System 
1 : Add new product with it’s price in records easily.
2 : Manage stock and vendor dues .
3 : Add a new Vendor seamlessly.
4 : Store add the records in SQL database.
5 : Basket to add number of products.
6 : The final bill gets printed with total cost including GST .
7 : GUI interface for easy and efficient interaction between user and program.

---
## How to SetUp ?
Setting Virtual Enviornment
``` 
python -m venv venv
```
Activating Virtual Enviornment (for windows)

```
venv/Scripts/Activate.ps1
```
Installing required Packages
```
pip install tkinterx
```
```
pip install ttkbootstrap
```
```
pip install mysql-connector
```
SQL-commands
```
create database bill;
use bill;
create table product(pro_name varchar(50) , price int(4),vendor varchar(50), quant_stock int(5));
create table vendor(v_name varchar(50), price_due int(8));
```
---
### First Window
<img width="234" height="152" alt="image" src="https://github.com/user-attachments/assets/fcf2551f-50ee-400c-9cbb-248b8fd06c88" />

### Adding Product to records
<img width="738" height="433" alt="image" src="https://github.com/user-attachments/assets/5bfcc84e-9179-4689-96cc-58be3ea23167" />

### Generate Bill
<img width="1192" height="781" alt="image" src="https://github.com/user-attachments/assets/1c8729a9-a756-4101-9b24-c9efc76d2c19" />


### Add new Vendor to Database
<img width="775" height="600" alt="image" src="https://github.com/user-attachments/assets/bdf0799e-2b33-45de-8de4-b2c6b32b2bb0" />

### Dues and Payment management of vendors 
<img width="590" height="454" alt="image" src="https://github.com/user-attachments/assets/5a62a611-79ac-4309-8162-fbf5c01e9df3" />




