CREATE TABLE Customers (
    CUSTOMER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT,
    email TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE ORDERS (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    CUSTOMER_ID INTEGER,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    status TEXT,
    total_amount REAL NOT NULL,
    payment_method TEXT,
    FOREIGN KEY (CUSTOMER_ID) REFERENCES Customers(CUSTOMER_ID)
);

CREATE TABLE OrderItems (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    menu_item_id INTEGER,
    price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES ORDERS(order_id),
    FOREIGN KEY (menu_item_id) REFERENCES MENU(menu_item_id)
);

CREATE TABLE MENU (
    menu_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    item_description TEXT,
    category TEXT,
    item_price REAL NOT NULL,
    item_calories INTEGER,
    is_it_available BOOLEAN DEFAULT 1
);

CREATE TABLE PAYMENTS (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    amount REAL NOT NULL,
    payment_method TEXT,
    payment_status TEXT DEFAULT 'pending',
    payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES ORDERS(order_id)
);

CREATE TABLE MENUMODIFY (
    modify_id INTEGER PRIMARY KEY AUTOINCREMENT,
    menu_item_id INTEGER,
    modifieditem_name TEXT,
    modified_price REAL NOT NULL,
    FOREIGN KEY (menu_item_id) REFERENCES MENU(menu_item_id)
);