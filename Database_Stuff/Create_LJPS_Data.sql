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

SET foreign_key_checks = 0;
DROP TABLE IF EXISTS `SKill`, `Positions`, `Skill_set`, `Skill_Rewarded`, `Learning_Journey`;
SET foreign_key_checks = 1;
USE `is212_ALL_IN_ONE`;

CREATE TABLE `Skill` (
  `Skill_ID` int PRIMARY KEY AUTO_INCREMENT,
  `Skill_Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `Positions` (
  `Position_ID` int PRIMARY KEY,
  `Position_Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- save skills required by positions and positions which require which skills
CREATE TABLE `Skill_Set` (
  `Skill_Set_ID` int PRIMARY KEY AUTO_INCREMENT,
  `Skill_ID` int NOT NULL,
  `Position_ID` int NOT NULL,
  FOREIGN KEY (`Skill_ID`) REFERENCES Skill(`Skill_ID`),
  FOREIGN KEY (`Position_ID`) REFERENCES Positions(`Position_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- save skills rewarded by a course and save courses which give which skill
CREATE TABLE `Skill_Rewarded` (
  `Skill_Rewarded_ID` int PRIMARY KEY AUTO_INCREMENT,
  `Skill_ID` int NOT NULL,
  `Course_ID` varchar(20) NOT NULL,
  FOREIGN KEY (`Skill_ID`) REFERENCES Skill(`Skill_ID`),
  FOREIGN KEY (`Course_ID`) REFERENCES Course(`Course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- save which positions aspired by staff and save which staff aspire to be which positions
CREATE TABLE `Learning_Journey` (
  `Learning_Journey_ID` int PRIMARY KEY AUTO_INCREMENT,
  `Staff_ID` int NOT NULL,
  `Skill_Set_ID` int NOT NULL,
  `Skill_Rewarded_ID` int  NOT NULL,
  FOREIGN KEY (`Staff_ID`) REFERENCES Staff(`Staff_ID`),
  FOREIGN KEY (`Skill_Set_ID`) REFERENCES Skill_Set(`Skill_Set_ID`),
  FOREIGN KEY (`Skill_Rewarded_ID`) REFERENCES Skill_Rewarded(`Skill_Rewarded_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ------------------------------------ DUMMY DATA STARTS HERE -------------------------------------------------------------------------------

-- **Given tables from LMS are: Course, Role, Staff, Registration**

INSERT INTO `Positions` (`Position_ID`, `Position_Name`) VALUES
(1, 'Data Analyst'),
(2, 'Human Resource'),
(3, 'Head of Security');

INSERT INTO `Skill` (`Skill_ID`,`Skill_Name`) VALUES
(1,'Python'),
(2,'R'),
(3,'Tableau'),
(4,'Interpersonal Skills'),
(5,'Public Speaking');

INSERT INTO `Skill_Set` (`Skill_ID`, `Position_ID`) VALUES
(1, 1),
(1, 1),
(3, 1),
(4, 3),
(5, 2);

INSERT INTO `Skill_Rewarded` (`Skill_ID`, `Course_ID`) VALUES
(1, 'FIN001'),
(1, 'tch006'),
(1, 'tch009'),
(2, 'COR001'),
(3, 'COR001'),
(4, 'MGT001'),
(5, 'MGT001');