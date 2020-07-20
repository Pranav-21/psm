-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 09, 2020 at 08:06 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hardware`
--

-- --------------------------------------------------------

--
-- Table structure for table `pc`
--

CREATE TABLE `pc` (
  `id` int(11) NOT NULL,
  `service_e_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `departmentid` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `brandname` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `installdate` date NOT NULL,
  `worrenty` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `processor` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `ram` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `storage` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `monitor` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `printer` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `lan` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `repair` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `pc`
--

INSERT INTO `pc` (`id`, `service_e_name`, `departmentid`, `brandname`, `installdate`, `worrenty`, `processor`, `ram`, `storage`, `monitor`, `printer`, `lan`, `repair`) VALUES
(35, '', 'operation-1', 'hp', '2020-01-16', '3 years', 'initel i3-2.6GHz 8th genration', '4-GB DDR4', '500-GB SSD', 'HP 19-inch', 'Canon- lan connected', 'connected with all', 'no repairing'),
(36, '', 'op-2', 'hp', '2020-01-12', '3 years', 'initel i3-2.6GHz 8th genration', '4-GB DDR4', '500-GB SSD', 'HP 19-inch', 'xerox-lan connected', 'connected with all', 'no repairing'),
(37, '', 'op-5', 'hp', '2020-01-12', '3 years', 'initel i3-2.6GHz 8th genration', '4-GB DDR4', '500-GB SSD', 'HP 19-inch', 'Canon- lan connected', 'connected with all', 'no repairing'),
(38, '', 'op-4', 'hp', '2020-01-14', '3 years', 'initel i3-2.6GHz 8th genration', '4-GB DDR4', '500-GB SSD', 'HP 19-inch', 'xerox - lan connected', 'connected with all', 'no repairing'),
(40, '', 'None', 'None', '0000-00-00', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None'),
(42, '', 'HR-1', 'hp', '2020-02-01', '5 years', 'initel i3-2.6GHz 8th genration', '4-GB DDR4', '500-GB SSD', 'Dell 19-inch', 'Canon- lan connected', 'connected', 'no repairing');

-- --------------------------------------------------------

--
-- Table structure for table `sign`
--

CREATE TABLE `sign` (
  `pid` int(11) NOT NULL,
  `user` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `sign`
--

INSERT INTO `sign` (`pid`, `user`, `password`) VALUES
(1, 'com', 'abcd');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pc`
--
ALTER TABLE `pc`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sign`
--
ALTER TABLE `sign`
  ADD PRIMARY KEY (`pid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pc`
--
ALTER TABLE `pc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `sign`
--
ALTER TABLE `sign`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
