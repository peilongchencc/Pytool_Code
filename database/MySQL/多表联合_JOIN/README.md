# 多表联合

在MySQL中，多表操作通常涉及联接（JOIN）操作，它允许你结合两个或多个表中的数据。这里，我将使用两个假设的表格来展示一个例子：`orders`（订单）和`customers`（客户）。我们的目标是列出所有订单及其对应的客户信息。<br>

### 示例表格结构

1. `orders` 表：
   - `order_id` (订单ID)
   - `customer_id` (客户ID)
   - `order_date` (订单日期)

2. `customers` 表：
   - `customer_id` (客户ID)
   - `customer_name` (客户姓名)
   - `customer_address` (客户地址)

### SQL 查询示例

```sql
SELECT orders.order_id, customers.customer_name, customers.customer_address
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;
```

### 解释

- `SELECT` 子句：选择需要显示的字段。这里选择了 `orders` 表的 `order_id`，以及 `customers` 表的 `customer_name` 和 `customer_address`。
  
- `FROM orders`：指定了主表，即查询的起点是 `orders` 表。

- `JOIN customers`：指明要与 `orders` 表联接的另一张表是 `customers`。

- `ON orders.customer_id = customers.customer_id`：指定联接条件。这告诉MySQL如何匹配 `orders` 表和 `customers` 表的记录。联接条件是两个表中的 `customer_id` 相等。

这个查询的结果将是一个包含所有订单ID、对应客户姓名和客户地址的列表，前提是每个订单的客户ID在 `customers` 表中都有对应的记录。<br>

### 注意事项

- 确保联接条件正确，避免产生错误的结果。
- 对于新手来说，理解表之间的关系和如何使用联接是关键。
- 在复杂的数据库中，可能需要使用更复杂的联接（如 LEFT JOIN, RIGHT JOIN, INNER JOIN, OUTER JOIN 等）来满足特定的数据查询需求。



当涉及到三个表的操作时，你可以使用多个 `JOIN` 子句来连接这些表。假设我们有一个额外的表 `products`（产品），我们想要结合之前的 `orders` 和 `customers` 表，来展示订单、客户和产品的信息。<br>

### 示例表格结构

1. `orders` 表：
   - `order_id` (订单ID)
   - `customer_id` (客户ID)
   - `product_id` (产品ID)
   - `order_date` (订单日期)

2. `customers` 表：
   - `customer_id` (客户ID)
   - `customer_name` (客户姓名)
   - `customer_address` (客户地址)

3. `products` 表：
   - `product_id` (产品ID)
   - `product_name` (产品名称)

### SQL 查询示例

```sql
SELECT 
    orders.order_id, 
    customers.customer_name, 
    customers.customer_address,
    products.product_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id;
```

### 解释

- `SELECT` 子句选择了所需的字段：订单ID、客户姓名、客户地址以及产品名称。

- `FROM orders` 指定了查询的起始表是 `orders`。

- 第一个 `JOIN` 子句将 `orders` 表与 `customers` 表联接，通过匹配 `customer_id`。

- 第二个 `JOIN` 子句将已经联接了 `customers` 的 `orders` 表进一步与 `products` 表联接，通过匹配 `product_id`。

这个查询的结果将是一个包含订单ID、客户姓名、客户地址和产品名称的列表，前提是每个订单中的客户ID和产品ID都在相应的表中有对应的记录。

### 注意事项

- 当处理多表联接时，确保联接条件正确，以避免错误的数据关联。
- 在复杂查询中，表的别名（AS）可以用来简化查询并提高可读性。
- 根据实际需求，可能需要使用不同类型的联接（如 LEFT JOIN, INNER JOIN 等）。


### 创建表的SQL语句

1. 创建 `orders` 表：

```sql
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE
);
```

2. 创建 `customers` 表：

```sql
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_address VARCHAR(255)
);
```

3. 创建 `products` 表：

```sql
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100)
);
```

### 插入数据的SQL语句

1. 向 `customers` 表插入数据：

```sql
INSERT INTO customers (customer_name, customer_address) VALUES
('Alice', '123 Apple St'),
('Bob', '456 Banana Ave'),
('Charlie', '789 Cherry Blvd'),
('Diana', '101 Diamond Road'),
('Evan', '202 Emerald Street'),
('Fiona', '303 Sapphire Lane');
```

2. 向 `products` 表插入数据：

```sql
INSERT INTO products (product_name) VALUES
('Laptop'),
('Smartphone'),
('Tablet'),
('Desktop Computer'),
('Printer'),
('Camera');
```

3. 向 `orders` 表插入数据：

```sql
INSERT INTO orders (customer_id, product_id, order_date) VALUES
(1, 1, '2023-01-01'),
(2, 2, '2023-01-02'),
(3, 3, '2023-01-03'),
(4, 4, '2023-02-01'),
(5, 5, '2023-02-15'),
(6, 6, '2023-03-01');
```

### 数据示例

- `customers` 表：

| customer_id | customer_name | customer_address    |
|-------------|---------------|---------------------|
| 1           | Alice         | 123 Apple St        |
| 2           | Bob           | 456 Banana Ave      |
| 3           | Charlie       | 789 Cherry Blvd     |
| 4           | Diana         | 101 Diamond Road    |
| 5           | Evan          | 202 Emerald Street  |
| 6           | Fiona         | 303 Sapphire Lane   |

- `products` 表：

| product_id | product_name    |
|------------|-----------------|
| 1          | Laptop          |
| 2          | Smartphone      |
| 3          | Tablet          |
| 4          | Desktop Computer|
| 5          | Printer         |
| 6          | Camera          |

- `orders` 表：

| order_id | customer_id | product_id | order_date |
|----------|-------------|------------|------------|
| 1        | 1           | 1          | 2023-01-01 |
| 2        | 2           | 2          | 2023-01-02 |
| 3        | 3           | 3          | 2023-01-03 |
| 4        | 4           | 4          | 2023-02-01 |
| 5        | 5           | 5          | 2023-02-15 |
| 6        | 6           | 6          | 2023-03-01 |

使用sql进行多表查询的结果如下：<br>

```sql
SELECT 
    orders.order_id, 
    customers.customer_name, 
    customers.customer_address,
    products.product_name
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN products ON orders.product_id = products.product_id;
```

查询结果:<br>

| order_id | customer_name | customer_address   | product_name     |
|----------|---------------|--------------------|------------------|
| 1        | Alice         | 123 Apple St       | Laptop           |
| 2        | Bob           | 456 Banana Ave     | Smartphone       |
| 3        | Charlie       | 789 Cherry Blvd    | Tablet           |
| 4        | Diana         | 101 Diamond Road   | Desktop Computer |
| 5        | Evan          | 202 Emerald Street | Printer          |
| 6        | Fiona         | 303 Sapphire Lane  | Camera           |