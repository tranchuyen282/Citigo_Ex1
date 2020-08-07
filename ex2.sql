-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 07, 2020 at 04:10 PM
-- Server version: 5.7.31-0ubuntu0.18.04.1
-- PHP Version: 7.3.20-1+ubuntu18.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ex2`
--

-- --------------------------------------------------------

--
-- Table structure for table `dim_date`
--

CREATE TABLE `dim_date` (
  `id` varchar(25) COLLATE utf8_unicode_ci NOT NULL,
  `day` int(11) DEFAULT NULL,
  `week` int(11) DEFAULT NULL,
  `month` int(11) DEFAULT NULL,
  `quater` int(11) DEFAULT NULL,
  `year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dim_day`
--

CREATE TABLE `dim_day` (
  `id` int(11) NOT NULL,
  `_day` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dim_month`
--

CREATE TABLE `dim_month` (
  `id` int(11) NOT NULL,
  `_month` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dim_product`
--

CREATE TABLE `dim_product` (
  `id` int(11) NOT NULL,
  `product_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dim_quater`
--

CREATE TABLE `dim_quater` (
  `id` int(11) NOT NULL,
  `_quater` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dim_retailer`
--

CREATE TABLE `dim_retailer` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dim_users`
--

CREATE TABLE `dim_users` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dim_week`
--

CREATE TABLE `dim_week` (
  `id` int(11) NOT NULL,
  `_week` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `dim_years`
--

CREATE TABLE `dim_years` (
  `id` int(11) NOT NULL,
  `_year` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `fact_transaction`
--

CREATE TABLE `fact_transaction` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `retailer_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `date_id` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dim_date`
--
ALTER TABLE `dim_date`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_Date_Year` (`year`),
  ADD KEY `FK_Date_Day` (`day`),
  ADD KEY `FK_Date_Quater` (`quater`),
  ADD KEY `FK_Date_Week` (`week`),
  ADD KEY `FK_Date_Month` (`month`);

--
-- Indexes for table `dim_day`
--
ALTER TABLE `dim_day`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dim_month`
--
ALTER TABLE `dim_month`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dim_product`
--
ALTER TABLE `dim_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dim_quater`
--
ALTER TABLE `dim_quater`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dim_retailer`
--
ALTER TABLE `dim_retailer`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dim_users`
--
ALTER TABLE `dim_users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dim_week`
--
ALTER TABLE `dim_week`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dim_years`
--
ALTER TABLE `dim_years`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `fact_transaction`
--
ALTER TABLE `fact_transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_UserID` (`user_id`),
  ADD KEY `FK_Product_Id` (`product_id`),
  ADD KEY `FK_Retailer_Id` (`retailer_id`),
  ADD KEY `FK_Date_Id` (`date_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dim_day`
--
ALTER TABLE `dim_day`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `dim_month`
--
ALTER TABLE `dim_month`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `dim_product`
--
ALTER TABLE `dim_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `dim_quater`
--
ALTER TABLE `dim_quater`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `dim_retailer`
--
ALTER TABLE `dim_retailer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `dim_users`
--
ALTER TABLE `dim_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT for table `dim_week`
--
ALTER TABLE `dim_week`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `dim_years`
--
ALTER TABLE `dim_years`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2101;

--
-- AUTO_INCREMENT for table `fact_transaction`
--
ALTER TABLE `fact_transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37170;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `dim_date`
--
ALTER TABLE `dim_date`
  ADD CONSTRAINT `FK_Date_Day` FOREIGN KEY (`day`) REFERENCES `dim_day` (`id`),
  ADD CONSTRAINT `FK_Date_Month` FOREIGN KEY (`month`) REFERENCES `dim_month` (`id`),
  ADD CONSTRAINT `FK_Date_Quater` FOREIGN KEY (`quater`) REFERENCES `dim_quater` (`id`),
  ADD CONSTRAINT `FK_Date_Week` FOREIGN KEY (`week`) REFERENCES `dim_week` (`id`),
  ADD CONSTRAINT `FK_Date_Year` FOREIGN KEY (`year`) REFERENCES `dim_years` (`id`);

--
-- Constraints for table `fact_transaction`
--
ALTER TABLE `fact_transaction`
  ADD CONSTRAINT `FK_Date_Id` FOREIGN KEY (`date_id`) REFERENCES `dim_date` (`id`),
  ADD CONSTRAINT `FK_Product_Id` FOREIGN KEY (`product_id`) REFERENCES `dim_product` (`id`),
  ADD CONSTRAINT `FK_Retailer_Id` FOREIGN KEY (`retailer_id`) REFERENCES `dim_retailer` (`id`),
  ADD CONSTRAINT `FK_UserID` FOREIGN KEY (`user_id`) REFERENCES `dim_users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
