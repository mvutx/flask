-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2026 at 10:06 AM
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
-- Database: `online`
--

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `emp_id` int(50) NOT NULL,
  `emp_name` text NOT NULL,
  `hire_date` date NOT NULL,
  `salary` int(50) NOT NULL,
  `dept_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`emp_id`, `emp_name`, `hire_date`, `salary`, `dept_id`) VALUES
(1, 'Ale Mutua', '2017-01-01', 75000, 2),
(2, 'Ale Mutua', '2017-01-01', 75000, 2),
(3, 'Ale Mutua', '2017-01-01', 75000, 2),
(5, 'Ale Mutua', '2017-01-01', 75000, 2),
(6, 'Ale Mutua', '2017-01-01', 75000, 2),
(7, 'Ale Mutua', '2017-01-01', 75000, 2),
(8, 'Ale Mutua', '2017-01-01', 75000, 2),
(9, 'Ale Mutua', '2017-01-01', 75000, 2),
(10, 'Ale Mutua', '2017-01-01', 75000, 2),
(11, 'Ale Mutua', '2017-01-01', 75000, 2),
(12, 'Ale Mutua', '2017-01-01', 75000, 2),
(13, 'Ale Mutua', '2017-01-01', 75000, 2),
(14, 'Ale Mutua', '2017-01-01', 75000, 2),
(15, 'Ale Mutua', '2017-01-01', 75000, 2),
(16, 'Ale Mutua', '2017-01-01', 75000, 2),
(17, 'Ale Mutua', '2017-01-01', 75000, 2),
(18, 'Ale Mutua', '2017-01-01', 75000, 2),
(19, 'Ale Mutua', '2017-01-01', 75000, 2),
(20, 'Ale Mutua', '2017-01-01', 75000, 2),
(21, 'Ale Mutua', '2017-01-01', 75000, 2),
(22, 'Ale Mutua', '2017-01-01', 75000, 2),
(23, 'Ale Mutua', '2017-01-01', 75000, 2),
(24, 'Ale Mutua', '2017-01-01', 75000, 2),
(25, 'Ale Mutua', '2017-01-01', 75000, 2),
(26, 'Ale Mutua', '2017-01-01', 75000, 2),
(27, 'Ale Mutua', '2017-01-01', 75000, 2),
(28, 'Ale Mutua', '2017-01-01', 75000, 2),
(29, 'Ale Mutua', '2017-01-01', 75000, 2);

-- --------------------------------------------------------

--
-- Table structure for table `laptops`
--

CREATE TABLE `laptops` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `processor` varchar(100) NOT NULL,
  `ram` varchar(50) NOT NULL,
  `storage` varchar(100) NOT NULL,
  `screensize` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL,
  `photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `laptops`
--

INSERT INTO `laptops` (`id`, `name`, `brand`, `processor`, `ram`, `storage`, `screensize`, `price`, `stock`, `photo`) VALUES
(1, 'hp probook 440G10', 'HP', 'Intel core i7', '16 GB', '512 GB ', '14\" FHD', 123000.00, 10, 'laptop.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `smartphones`
--

CREATE TABLE `smartphones` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  `storage` varchar(50) NOT NULL,
  `ram` varchar(50) NOT NULL,
  `battery` varchar(50) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL,
  `photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `smartphones`
--

INSERT INTO `smartphones` (`id`, `name`, `brand`, `model`, `storage`, `ram`, `battery`, `price`, `stock`, `photo`) VALUES
(1, 'iphone15', 'apple', 'A3102', '256GB', '8GB', '3274mAh', 1200.00, 10, 'iphone15.webp');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `laptops`
--
ALTER TABLE `laptops`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `smartphones`
--
ALTER TABLE `smartphones`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employees`
--
ALTER TABLE `employees`
  MODIFY `emp_id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `laptops`
--
ALTER TABLE `laptops`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `smartphones`
--
ALTER TABLE `smartphones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
