-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 27, 2021 at 08:33 AM
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


CREATE DATABASE IF NOT EXISTS `is212_ALL_IN_ONE` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `is212_ALL_IN_ONE`;

CREATE TABLE `Role` (
  `Role_ID` int PRIMARY KEY,
  `Role_Name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Course` (
  `Course_ID` varchar(20) PRIMARY KEY,
  `Course_Name` varchar(50) NOT NULL,
  `Course_Desc` varchar(255) DEFAULT NULL,
  `Course_Status` varchar(15) DEFAULT NULL,
  `Course_Type` varchar(10) DEFAULT NULL,
  `Course_Categor` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Staff` (
  `Staff_ID` int PRIMARY KEY,
  `Staff_FName` varchar(50) NOT NULL,
  `Staff_LName` varchar(50) NOT NULL,
  `Dept` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Role` int,
  FOREIGN KEY (`Role`) REFERENCES Role(`Role_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Registration` (
  `Reg_ID` int PRIMARY KEY,
  `Reg_Status` varchar(20) NOT NULL,
  `Completion_Status` varchar(20) NOT NULL,
  `Course_ID` varchar(20),
  `Staff_ID` int,
  FOREIGN KEY (`Course_ID`) REFERENCES Course(`Course_ID`),
  FOREIGN KEY (`Staff_ID`) REFERENCES Staff(`Staff_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Dumping data for table `patient`
--

-- INSERT INTO `patient` (`id`, `contact_num`, `ewallet_balance`) VALUES
-- (6, '+65 8888 8888', 88),
-- (7, '+65 8888 8888', 100),
-- (8, '+65 8888 8888', 500),
-- (9, '+65 8888 8888', 10),
-- (10, '+65 8888 8888', 30),
-- (11, '+65 8888 8888', 388);
