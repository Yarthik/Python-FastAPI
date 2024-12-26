CREATE TABLE Product (
    ProductID BIGINT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Category ENUM('finished', 'semi-finished', 'raw'),
    Description VARCHAR(250),
    ProductImage VARCHAR(250),
    SKU VARCHAR(100),
    UnitOfMeasure ENUM('mtr', 'mm', 'ltr', 'ml', 'cm', 'mg', 'gm', 'unit', 'pack'),
    LeadTime INT(3),
    CreatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
