-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         10.5.8-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para dbsupermercado
CREATE DATABASE IF NOT EXISTS `dbsupermercado` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `dbsupermercado`;

-- Volcando estructura para tabla dbsupermercado.business_hours
CREATE TABLE IF NOT EXISTS `business_hours` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `day` varchar(50) DEFAULT NULL,
  `start_time` varchar(50) DEFAULT NULL,
  `end_time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.business_hours: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `business_hours` DISABLE KEYS */;
/*!40000 ALTER TABLE `business_hours` ENABLE KEYS */;

-- Volcando estructura para tabla dbsupermercado.business_information
CREATE TABLE IF NOT EXISTS `business_information` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `business_id` int(11) unsigned DEFAULT NULL,
  `business_hours_id` int(11) unsigned DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `contact` varchar(255) DEFAULT NULL,
  `direction` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `business_information_business_registration_fk` (`business_id`),
  KEY `business_information_business_hours_fk` (`business_hours_id`),
  CONSTRAINT `business_information_business_hours_fk` FOREIGN KEY (`business_hours_id`) REFERENCES `business_hours` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `business_information_business_registration_fk` FOREIGN KEY (`business_id`) REFERENCES `business_registration` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=404 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.business_information: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `business_information` DISABLE KEYS */;
/*!40000 ALTER TABLE `business_information` ENABLE KEYS */;

-- Volcando estructura para tabla dbsupermercado.business_registration
CREATE TABLE IF NOT EXISTS `business_registration` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `business_type_id` int(11) unsigned NOT NULL,
  `email` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `business_registration_fk` (`business_type_id`),
  CONSTRAINT `business_registration_fk` FOREIGN KEY (`business_type_id`) REFERENCES `business_type` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2011 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.business_registration: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `business_registration` DISABLE KEYS */;
/*!40000 ALTER TABLE `business_registration` ENABLE KEYS */;

-- Volcando estructura para tabla dbsupermercado.business_type
CREATE TABLE IF NOT EXISTS `business_type` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.business_type: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `business_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `business_type` ENABLE KEYS */;

-- Volcando estructura para tabla dbsupermercado.cashiers
CREATE TABLE IF NOT EXISTS `cashiers` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `sale_id` int(11) unsigned DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `contact` varchar(200) DEFAULT NULL,
  `direction` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cashiers_sale_fk` (`sale_id`),
  CONSTRAINT `cashiers_sale_fk` FOREIGN KEY (`sale_id`) REFERENCES `sales` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2009 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.cashiers: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `cashiers` DISABLE KEYS */;
/*!40000 ALTER TABLE `cashiers` ENABLE KEYS */;

-- Volcando estructura para tabla dbsupermercado.categories
CREATE TABLE IF NOT EXISTS `categories` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `period_id` int(11) unsigned NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `barcode` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_period_fk` (`period_id`) USING BTREE,
  CONSTRAINT `category_period_fk` FOREIGN KEY (`period_id`) REFERENCES `periods` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.categories: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` (`id`, `period_id`, `name`, `barcode`) VALUES
	(20, 3, 'frutas', '100100'),
	(21, 3, 'Limpieza', '200200'),
	(22, 3, 'Dulces', '300300'),
	(23, 3, 'Medicinas', '400400'),
	(24, 3, 'zapatos', '500500');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;

-- Volcando estructura para tabla dbsupermercado.clients
CREATE TABLE IF NOT EXISTS `clients` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `contact` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.clients: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;

-- Volcando estructura para tabla dbsupermercado.periods
CREATE TABLE IF NOT EXISTS `periods` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `date` year(4) NOT NULL,
  `period` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.periods: ~2 rows (aproximadamente)
/*!40000 ALTER TABLE `periods` DISABLE KEYS */;
INSERT INTO `periods` (`id`, `date`, `period`) VALUES
	(3, '2021', 1),
	(4, '2021', 2),
	(21, '2017', 1);
/*!40000 ALTER TABLE `periods` ENABLE KEYS */;

-- Volcando estructura para tabla dbsupermercado.products
CREATE TABLE IF NOT EXISTS `products` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `business_id` int(11) unsigned DEFAULT NULL,
  `category_id` int(11) unsigned DEFAULT NULL,
  `supplier_id` int(11) unsigned DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `value` int(20) DEFAULT NULL,
  `date_admission` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `period_id` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_period_fk` (`period_id`) USING BTREE,
  KEY `product_business_registration_fk` (`business_id`),
  KEY `product_category_fk` (`category_id`),
  KEY `product_suplier_fk` (`supplier_id`),
  CONSTRAINT `product_business_registration_fk` FOREIGN KEY (`business_id`) REFERENCES `business_registration` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `product_category_fk` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `product_period_fk` FOREIGN KEY (`period_id`) REFERENCES `periods` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `product_suplier_fk` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=2620 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.products: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
/*!40000 ALTER TABLE `products` ENABLE KEYS */;

-- Volcando estructura para tabla dbsupermercado.purchase_receipts
CREATE TABLE IF NOT EXISTS `purchase_receipts` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `categories_id` int(11) unsigned DEFAULT NULL,
  `business_information_id` int(11) unsigned DEFAULT NULL,
  `cashier_id` int(11) unsigned DEFAULT NULL,
  `client_id` int(11) unsigned DEFAULT NULL,
  `product_id` int(11) unsigned DEFAULT NULL,
  `amount` int(200) DEFAULT NULL,
  `full_value` int(200) DEFAULT NULL,
  `date_purchase` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `purchase_category_fk` (`categories_id`) USING BTREE,
  KEY `purchase_business_information_fk` (`business_information_id`),
  KEY `purchase_cashier_fk` (`cashier_id`),
  KEY `purchase_client_fk` (`client_id`),
  KEY `purchase_product_fk` (`product_id`),
  CONSTRAINT `purchase_business_information_fk` FOREIGN KEY (`business_information_id`) REFERENCES `business_information` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `purchase_cashier_fk` FOREIGN KEY (`cashier_id`) REFERENCES `cashiers` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `purchase_category_fk` FOREIGN KEY (`categories_id`) REFERENCES `categories` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `purchase_client_fk` FOREIGN KEY (`client_id`) REFERENCES `clients` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `purchase_product_fk` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2004 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.purchase_receipts: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `purchase_receipts` DISABLE KEYS */;
/*!40000 ALTER TABLE `purchase_receipts` ENABLE KEYS */;

-- Volcando estructura para tabla dbsupermercado.sales
CREATE TABLE IF NOT EXISTS `sales` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `purchase_id` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sales_purchase_fk` (`purchase_id`),
  CONSTRAINT `sales_purchase_fk` FOREIGN KEY (`purchase_id`) REFERENCES `purchase_receipts` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.sales: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;

-- Volcando estructura para tabla dbsupermercado.suppliers
CREATE TABLE IF NOT EXISTS `suppliers` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `contact` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla dbsupermercado.suppliers: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
