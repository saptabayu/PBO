-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 09, 2024 at 03:48 AM
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
-- Database: `dbkreditmotor`
--

-- --------------------------------------------------------

--
-- Table structure for table `credit_motor`
--

CREATE TABLE `credit_motor` (
  `id` int(11) NOT NULL,
  `nama_pengguna` varchar(100) DEFAULT NULL,
  `tanggal_credit` date DEFAULT NULL,
  `tarif_subtotal` decimal(10,2) DEFAULT NULL,
  `status_bayar` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `credit_motor`
--

INSERT INTO `credit_motor` (`id`, `nama_pengguna`, `tanggal_credit`, `tarif_subtotal`, `status_bayar`) VALUES
(1, 'sapta bayu', '2024-02-09', 99999999.99, 'lunas');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `credit_motor`
--
ALTER TABLE `credit_motor`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `credit_motor`
--
ALTER TABLE `credit_motor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
