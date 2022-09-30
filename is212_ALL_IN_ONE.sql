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

DROP DATABASE IF EXISTS `is212_ALL_IN_ONE`;
CREATE DATABASE IF NOT EXISTS `is212_ALL_IN_ONE` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `is212_ALL_IN_ONE`;

CREATE TABLE `Role` (
  `Role_ID` int PRIMARY KEY,
  `Role_Name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Skill` (
  `Skill_Name` varchar(50) PRIMARY KEY 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Positions` (
  `Position_ID` int PRIMARY KEY,
  `Position_Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Course` (
  `Course_ID` varchar(20) PRIMARY KEY,
  `Course_Name` varchar(50) NOT NULL,
  `Course_Desc` varchar(255) DEFAULT NULL,
  `Course_Status` varchar(15) DEFAULT NULL,
  `Course_Type` varchar(10) DEFAULT NULL,
  `Course_Category` varchar(50) DEFAULT NULL
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

-- Save staff enroled in courses and courses which enrolled by staff
CREATE TABLE `Registration` (
  `Reg_ID` int PRIMARY KEY,
  `Reg_Status` varchar(20) NOT NULL,
  `Completion_Status` varchar(20) NOT NULL,
  `Course_ID` varchar(20),
  `Staff_ID` int,
  FOREIGN KEY (`Course_ID`) REFERENCES Course(`Course_ID`),
  FOREIGN KEY (`Staff_ID`) REFERENCES Staff(`Staff_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- save skills required by positions and positions which require which skills
CREATE TABLE `Skill_Set` (
  `Skill_Set_ID` int PRIMARY KEY AUTO_INCREMENT,
  `Skill_Name` varchar(50),
  `Position_ID` int,
  FOREIGN KEY (`Skill_Name`) REFERENCES Skill(`Skill_Name`),
  FOREIGN KEY (`Position_ID`) REFERENCES Positions(`Position_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- save skills rewarded by a course and save courses which give which skill
CREATE TABLE `Skill_Rewarded` (
  `Skill_Rewarded_ID` int PRIMARY KEY AUTO_INCREMENT,
  `Skill_Name` varchar(50),
  `Course_ID` varchar(20),
  FOREIGN KEY (`Skill_Name`) REFERENCES Skill(`Skill_Name`),
  FOREIGN KEY (`Course_ID`) REFERENCES Course(`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- save which positions aspired by staff and save which staff aspire to be which positions
CREATE TABLE `Learning_Journey` (
  `Learning_Journey_ID` int PRIMARY KEY AUTO_INCREMENT,
  `Position_ID` int,
  `Staff_ID` int,
  FOREIGN KEY (`Position_ID`) REFERENCES Positions(`Position_ID`),
  FOREIGN KEY (`Staff_ID`) REFERENCES Staff(`Staff_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- ------------------------------------ DUMMY DATA STARTS HERE -------------------------------------------------------------------------------
 
INSERT INTO `Role` (`Role_ID`, `Role_Name`) VALUES
(1, 'Staff'),
(2, 'Admin'),
(3, 'Manager');

INSERT INTO `Positions` (`Position_ID`, `Position_Name`) VALUES
(1, 'Data Analyst'),
(2, 'Human Resource'),
(3, 'Head of Security');

INSERT INTO `Skill` (`Skill_Name`) VALUES
('Python'),
('R'),
('Tableau'),
('Interpersonal Skills'),
('Public Speaking');

INSERT INTO Course (`Course_ID`, `Course_Name`, `Course_Desc`, `Course_Status`, `Course_Type`, `Course_Category`) VALUES
('course1', 'Data Analytics with Advanced Tableau', 'Ben Dover', 'Active', 'External', 'Technical'),
('course2', 'Management Communication', 'Mike Hunt', 'Retired', 'Internal', 'General');

INSERT INTO `Skill_Set` (`Skill_Name`, `Position_ID`) VALUES
('Python', 1),
('R', 1),
('Tableau', 1),
('Interpersonal Skills', 3),
('Public Speaking', 2);

INSERT INTO `Skill_Rewarded` (`Skill_Name`, `Course_ID`) VALUES
('Python', 'course1'),
('R', 'course1'),
('Tableau', 'course1'),
('Interpersonal Skills', 'course2'),
('Public Speaking', 'course2');