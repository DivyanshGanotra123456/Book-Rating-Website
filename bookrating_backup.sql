-- MySQL dump 10.13  Distrib 5.5.16, for Win64 (x86)
--
-- Host: localhost    Database: bookrating
-- ------------------------------------------------------
-- Server version	5.5.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admins` (
  `adminid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `accountstatus` varchar(1) NOT NULL,
  PRIMARY KEY (`adminid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'sam','123456','A');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authors`
--

DROP TABLE IF EXISTS `authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authors` (
  `author` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authors`
--

LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES ('Dr. APJ Abdul Kalam'),('Saranya Umakanthan'),('Gaur Gopal Das'),('Dr. APJ Abdul Kalam'),('Saranya Umakanthan'),('Gaur Gopal Das'),('Shiv Khera');
/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `bookid` int(11) NOT NULL AUTO_INCREMENT,
  `booktitle` varchar(50) NOT NULL,
  `author` varchar(50) NOT NULL,
  `genre` varchar(20) NOT NULL,
  `description` text NOT NULL,
  `ratingcount` int(11) DEFAULT '0',
  `commentcount` int(11) DEFAULT '0',
  `imgname` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`bookid`),
  UNIQUE KEY `booktitle` (`booktitle`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'Darkly Dreaming Dexter','Jeff Lindsay','Crime',' It formed the basis of the Showtime television series Dexter and won the 2005 Dilys Award and the 2007 Book to TV award. Dexter Morgan works for the Miami-Dade Police Department as a forensic blood spatter analyst. When accomplished, the voice is placated for a while, but always, eventually returns. Dexter calls these rules \"The Code of Harry.\" Yet, he feels a compelling pull to the killer, due to similar desires. After a lucid dream, Dexter drives around Miami and spots a refrigerated truck. When he follows the truck, the killer throws a severed head in his car. The killer begins sending messages to Dexter, who finds the crimes fascinating. Dexter is torn between helping Deborah and allowing the killer to continue his spree. \r\nThe novel is the basis for a TV series on the cable network Showtime. ',0,0,'dexter2.jpg'),(2,'Animal Farm','George Orwell','Fiction',' The pigs, because of their intelligence, become the supervisors of the farm. Boxer, an incredibly strong horse, proves himself to be the most valuable animal in this endeavor. Jones, meanwhile, forsakes the farm and moves to another part of the county. The animals receive less and less food, while the pigs grow fatter. Frederick and his men attack the farm and explode the windmill but are eventually defeated. Life for all the animals (except the pigs) is harsh. The Seven Commandments are reduced to a single law: \"All Animals Are Equal / But Some Are More Equal Than Others.\" The novel ends with Pilkington sharing drinks with the pigs in Jones\' house. As other animals watch the scene from outside the window, they cannot tell the pigs from the humans. Previous\r\nAnimal Farm at a Glance\r\n',0,0,'animal-farm-graphic-novel.jpg');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `commentsrating`
--

DROP TABLE IF EXISTS `commentsrating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `commentsrating` (
  `commentid` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `bookid` int(11) DEFAULT NULL,
  `comments` varchar(1000) DEFAULT NULL,
  `ratings` int(11) DEFAULT NULL,
  `commentstatus` varchar(1) NOT NULL,
  PRIMARY KEY (`commentid`),
  KEY `userid` (`userid`),
  KEY `bookid` (`bookid`),
  CONSTRAINT `commentsrating_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `users` (`userid`),
  CONSTRAINT `commentsrating_ibfk_2` FOREIGN KEY (`bookid`) REFERENCES `books` (`bookid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `commentsrating`
--

LOCK TABLES `commentsrating` WRITE;
/*!40000 ALTER TABLE `commentsrating` DISABLE KEYS */;
/*!40000 ALTER TABLE `commentsrating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `genres` (
  `genre` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES ('Motivational'),('Life'),('Inspirational'),('Business'),('Managenet'),('Motivational'),('Inspiration'),('Life'),('Success');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `emailid` varchar(50) NOT NULL,
  `image_path` varchar(255) NOT NULL,
  PRIMARY KEY (`userid`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `emailid` (`emailid`),
  UNIQUE KEY `unique_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Anubhav','1234','abubhav@gmail.com','static/images/profile2.jpg'),(2,'Divyansh12323','1234','Anubhav@gmail.com','static/images/profile2.jpg');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-03 12:03:44
