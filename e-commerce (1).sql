-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 10, 2026 at 04:31 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `e-commerce`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cusid` int(11) NOT NULL,
  `cusnm` varchar(20) DEFAULT NULL,
  `prodid` int(11) DEFAULT NULL,
  `qnt` int(11) DEFAULT NULL,
  `mobno` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cusid`, `cusnm`, `prodid`, `qnt`, `mobno`) VALUES
(202601, 'Aryan', 10001, 2, 987123451),
(202602, 'Aryan', 10002, 2, 987122351),
(202603, 'Aryan', 10004, 4, 987123451),
(202604, 'Vansh', 10003, 1, 954123451),
(202605, 'vansh', 10005, 9, 934623451),
(202606, 'vansh', 10006, 2, 987123451);

-- --------------------------------------------------------

--
-- Table structure for table `order_table`
--

CREATE TABLE `order_table` (
  `ordid` int(11) NOT NULL,
  `orddate` date DEFAULT NULL,
  `cusid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `order_table`
--

INSERT INTO `order_table` (`ordid`, `orddate`, `cusid`) VALUES
(2001, '2015-09-06', 202601),
(2002, '2025-03-14', 202602),
(2003, '2019-02-23', 202603),
(2004, '2023-11-29', 202604),
(2005, '2024-01-31', 202605),
(2006, '2020-06-16', 202606);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `prodid` int(11) NOT NULL,
  `prodnm` varchar(20) DEFAULT NULL,
  `prodprice` int(11) DEFAULT NULL,
  `stockid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`prodid`, `prodnm`, `prodprice`, `stockid`) VALUES
(10001, 'fan', 1800, 1),
(10002, 'oppo', 24000, 2),
(10003, 'HP', 98000, 3),
(10004, 'carrot', 40, 4),
(10005, 'MAX', 120, 5),
(10006, 'Jordans', 76000, 6),
(10007, 'AC', 64000, 1),
(10008, 'TV', 93000, 1),
(10009, 'realme', 32000, 2),
(10010, 'samsung', 45000, 2),
(10011, 'lenovo', 79000, 3),
(10012, 'ASUS', 56000, 3),
(10013, 'tomato', 60, 4),
(10014, 'RUPA', 340, 5),
(10015, 'LUX', 230, 5),
(10016, 'adidas', 23000, 6);

-- --------------------------------------------------------

--
-- Table structure for table `stock_cat`
--

CREATE TABLE `stock_cat` (
  `stockid` int(11) NOT NULL,
  `stockcatnm` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stock_cat`
--

INSERT INTO `stock_cat` (`stockid`, `stockcatnm`) VALUES
(1, 'electronics'),
(2, 'mobile'),
(3, 'laptop'),
(4, 'grocery'),
(5, 'garments'),
(6, 'shoes'),
(7, 'phone');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cusid`),
  ADD KEY `prodid` (`prodid`);

--
-- Indexes for table `order_table`
--
ALTER TABLE `order_table`
  ADD PRIMARY KEY (`ordid`),
  ADD KEY `cusid` (`cusid`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`prodid`),
  ADD KEY `stockid` (`stockid`);

--
-- Indexes for table `stock_cat`
--
ALTER TABLE `stock_cat`
  ADD PRIMARY KEY (`stockid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `cusid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=202607;

--
-- AUTO_INCREMENT for table `order_table`
--
ALTER TABLE `order_table`
  MODIFY `ordid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2007;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `prodid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10017;

--
-- AUTO_INCREMENT for table `stock_cat`
--
ALTER TABLE `stock_cat`
  MODIFY `stockid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`prodid`) REFERENCES `product` (`prodid`);

--
-- Constraints for table `order_table`
--
ALTER TABLE `order_table`
  ADD CONSTRAINT `order_table_ibfk_1` FOREIGN KEY (`cusid`) REFERENCES `customer` (`cusid`);

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`stockid`) REFERENCES `stock_cat` (`stockid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
