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
INSERT INTO `books` VALUES (1,'Darkly Dreaming Dexter','Jeff Lindsay','Crime',' It formed the basis of the Showtime television series Dexter and won the 2005 Dilys Award and the 2007 Book to TV award. Dexter Morgan works for the Miami-Dade Police Department as a forensic blood spatter analyst. When accomplished, the voice is placated for a while, but always, eventually returns. Dexter calls these rules \"The Code of Harry.\" Yet, he feels a compelling pull to the killer, due to similar desires. After a lucid dream, Dexter drives around Miami and spots a refrigerated truck. When he follows the truck, the killer throws a severed head in his car. The killer begins sending messages to Dexter, who finds the crimes fascinating. Dexter is torn between helping Deborah and allowing the killer to continue his spree. \r\nThe novel is the basis for a TV series on the cable network Showtime. ',0,0,'dexter2.jpg'),(2,'Animal Farm','George Orwell','Fiction',' The pigs, because of their intelligence, become the supervisors of the farm. Boxer, an incredibly strong horse, proves himself to be the most valuable animal in this endeavor. Jones, meanwhile, forsakes the farm and moves to another part of the county. The animals receive less and less food, while the pigs grow fatter. Frederick and his men attack the farm and explode the windmill but are eventually defeated. Life for all the animals (except the pigs) is harsh. The Seven Commandments are reduced to a single law: \"All Animals Are Equal / But Some Are More Equal Than Others.\" The novel ends with Pilkington sharing drinks with the pigs in Jones\' house. As other animals watch the scene from outside the window, they cannot tell the pigs from the humans. Previous\r\nAnimal Farm at a Glance\r\n',0,0,'animal-farm-graphic-novel.jpg'),(3,'Attack On Titan Manga','Hajime Isayama','War','The main characters are part of the military designed to repel, or attack, these titans. It\'s not far off from a zombie apocalypse, only much worse than usual because the zombies are kaiju sized.As the series goes on and the twists pile up, the series\' mythology becomes much denser and the narrative more complex. The first Titan, a young girl named Ymir, once lived a provincial life in a small village. Everything changed when a warrior tribe called the Eldians attacked. The injured Ymir took refuge in an enormous tree, where she fell into a pool of water. She might have drowned if not for a mysterious creature resembling a cross between a centipede and disembodied nervous system. The creature bonded with Ymir, turning her into the first Titan.Ymir\'s transformation spared her life, but she was still a slave. The brutal state of the ancient \"AOT\" world resembles the Viking age. The Eldians\' outfits and culture are modeled on Germanic and Nordic tribes, while the ancient Marleyans seem more Greco-Roman. To preserve her power, Fritz fed her remains to their daughters. Filtered through generations, nine distinct Titans emerged. There are eight others: the Attack Titan, the Armored Titan, the Colossal Titan, the Female Titan, the Jaw Titan, the Cart Titan, the Beast Titan, and the War Hammer Titan. Implicitly due to Ymir\'s own premature death, holders of Titan powers expire after 13 years. To repent, he decides to orchestrate his own empire\'s fall. The King conspires in secret with the Tybur family, holders of the War Hammer Titan. The Titans\' \"hardening\" ability gives the walls the appearance of the stone. In truth, this is an empty threat. For the next century, the Founding Titan and the memories of its holders are passed down through the Reiss family. For one, the Ackerman clan barely endures. In Year 829, one of the last Ackermans, Kenny, befriends Uri Reiss. Kenny assumes the role of his ancestors as the royal family\'s bodyguard. Kenny then discovers his sister Kuchel died while working in a brothel and adopts her son Levi. The same year, another Ackerman marries a descendant of the Hizuru clan, merging the two bloodlines in their daughter Mikasa. Mikasa\'s parents are killed by slave traders in 844, but she is saved by a boy her age, Eren Yeager. With Marley now in possession of seven out of the nine Titans, they become the world\'s new superpower. Grisha is saved by Marleyan officer Kruger, a secret Eldian and holder of the Attack Titan. Kruger passes the Attack Titan to Grisha and sends him to the Walls to claim the Founding Titan from the Reiss family. The latter two are killed by Titans during the 23rd Exterior Scouting Mission. Transforming into the Colossal Titan, Bertholdt breaks down the wall of Shiganshina. Pure Titans pour into the city, among them the former Dina Fritz, and devour the populace. Grisha eats Frieda Reiss to inherit the Founding Titan and kills all the others, barring Rod Reiss. Grisha tracks down Eren at a refugee camp and takes him to a remote forest. Ymir also makes her way to Wall Rose and blends in. In 846, the Paradis government sends a doomed expedition to reclaim Wall Maria. Humanity achieves its first victory over the Titans. As Eren completes his task, Marco overhears Reiner and Bertholdt conspiring. Five days after the battle of Trost, Commander-in-Chief Darius Zackly reprimands Eren to the Survey Corps\' custody. The Warriors, having faced a setback, decide to capture Eren. Annie, as the Female Titan, ambushes the scouts. Most are placed under the command of squad leader Mike Zacharias at Wall Rose. The battle between Eren and Annie in the Stohess District of Wall Sheena causes much destruction and ends with Annie sealing herself in a crystalline cocoon. Commander Zacharias is killed by the Beast Titan while his squad rests at the nearby castle Utgard. Reiner and Bertholdt reveal themselves and abduct Eren and Ymir. Hange and Connie realize they were the inhabitants of Ragako, Connie\'s hometown. After Nick is killed and Erwin summoned to the capital, Levi\'s squad realizes they\'re in danger and they flee the cabin. The assembly orders the gates of Wall Sheena shut. In an underground chapel, Rod Reiss tries to convince his daughter to eat Eren and become the founder, but she refuses. Reiss drinks Titan spinal fluid meant for Historia and becomes an enormous Titan headed for Trost. The Survey corps managed to slay him before he damages the city. After these two months, a squad of a hundred soldiers, led by Erwin Smith, ride to Shiganshina to reclaim it. Over the next year, Paradis is completely rid of Titans and the lands of Wall Maria repopulated. Marley is too preoccupied to send more than lone scout ships to Paradis, allowing the island to advance. On them is a group in league with Zeke, led by Yelena and all from the subject countries of Marley. Azumabito gives the Paradisians technology to build a railway and reveal Mikasa\'s heritage to her. In the Liberio harbor, Armin transforms into the Colossal Titan, wiping out the Marleyan navy. The battle goes back and forth, with Eren leading from the front lines against the Warriors. Zeke arrives and transforms the infected Paradisians into pure Titans. As Eren and the Wall Titans reach Marley, the alliance steals a Hizuru flying boat from the Yeagerists, then make a detour to Hizuru to repair it. Along the way, Magath, Shadis, Floch, then finally Hange are all killed.Now we enter manga-only territory, though the anime will certainly be following the same story. The fourth and final day of the Rumbling is known as the Battle of Heaven and Earth. Armin, as the Colossal Titan, duels Eren before Mikasa decapitates him. In 857, they return to Paradis. Levi chooses to settle in Marley, while Mikasa returns to Shiganshina and buries Eren under a tree they played on as children. Mikasa dies of old age in roughly Year 915. At least a few decades after that, Paradis has reached 21st-century technology level and Shiganshina is now made up of modern skyscrapers. Alas, war has again come to the island: a fleet of aerial bombers destroy the city as part of a new, unknown conflict. Even as buildings fall, the tree stands.More decades pass and the rubble of Shiganshina is reclaimed by the forest. One day, a child and their dog hike through the ruins and come to the base of the tree, now a cavern, like the one Ymir found all those centuries ago. The end of one war is not the end of mankind\'s capacity to wage war, personified by the Titans.',0,0,'attackkk.jpg'),(4,'Dexter in The Dark','Jeff Lindsay','Crime','  Dexter in the Dark is a 2007 novel written by Jeff Lindsay. Their heads are replaced by the ceramic heads of bulls. While attempting to dispatch a killer who had been stalking him, Dexter becomes frightened and is unable to go through with the deed. The cult kidnaps Astor and Cody, thereby forcing Dexter to engage them head-on. However, the cult soon captures Dexter through a supernatural captivation of music. Dexter manages to snap out of his trance and opens fire on the cult members. Dexter laments that, due to having killed at such an early age, Cody\'s journey will now be more difficult. One is a person called the Watcher, a member of the cult that follows and observes Dexter. IT and its offspring go to war, and IT prevails. Some of IT\'s remaining children stay in hiding, fearing IT\'s power.',0,0,'dexter4.jpg'),(5,'Chainsawman Manga All Volumes','Tatsuki Fujimoto','Horror','The story is set in a world where Devils are born from human fears. Devils are usually dangerous and malevolent, their power proportional to the fear they incite. However, humans can form contracts with them to use their power, and there are individuals specializing in hunting and employing them, called Devil Hunters. Devils originate from Hell, and exist in a cycle between Earth and Hell: they migrate to Earth when killed in Hell, and vice-versa. Dwelling in Hell are extremely powerful Devils called Primal Fears, which have never been killed. Transit between planes appears to be overseen by the Hell Devil.\r\n\r\n\r\nA Devil may, in certain conditions, inhabit the body of a dead human, gaining some of their memories and personality; such a creature is called a Fiend. Devils who naturally have a humanoid form are said to be benevolent to humans\r\nThe events of the story take place in 1997, in an alternate timeline where the Soviet Union still exists, and many events such as the Holocaust appear to have not occurred.',0,0,'chainsaw.jpg'),(6,'Lord Of The Rings','J.R.R. Tolkien','Fiction',' Sauron poured all his\r\nevil and his will to dominate into this ring. Later he was\r\nkilled, and the ring fell to the bottom of the sea. The creature\r\nGollum discovered it and brought it to his cave. Then he lost it\r\nto the hobbit Bilbo Baggins. Eventually Bilbo agrees to entrust it to\r\nhis nephew Frodo. Gandalf senses that the ring is gaining power\r\nover Bilbo. The scene shifts to Gandalf, who rushes to a library\r\nto sift through ancient scrolls. Mysterious letters appear on the ring’s surface. He longs to find it, and it longs to find him. Gandalf has learned that\r\nSauron has kidnapped Gollum and that Gollum has revealed that Bilbo\r\nhas the ring. The ring must leave the Shire or it will endanger\r\nall the hobbits. He determines that Frodo\r\nmust take it. A ranger named\r\nStrider introduces himself to the group of hobbits and urges them\r\nto be more careful. The wraiths arrive at the hotel, but the hobbits,\r\nthanks to Strider, are well hidden. Strider explains to them that\r\nthe wraiths were formerly the nine human kings who had the nine\r\nhuman rings. He declares that Mordor cannot be defeated and\r\nthat the two wizards must join with Sauron. Gandalf protests, and\r\nthe wizards battle. Strider and the hobbits head for Rivendell, home of the\r\nelves. The\r\nhobbits foolishly light a fire at their campsite, and the ringwraiths\r\nspot them. Frodo is cured and wakes up to discover Gandalf by his side. The ring survives because of Isildur’s\r\nweakness. We also\r\nlearn that Aragorn and Arwen are in love and have been for many\r\nyears. Elrond convenes a meeting and announces that the races\r\nmust come together to defeat Mordor. There is some disagreement as to who will undertake\r\nthis arduous task, and eventually Frodo emerges. Others step forward\r\nto accompany Frodo, forming a fellowship of the ring. The fellowship sets forth from Rivendell. The orcs disperse, however, at the approach of a Balrog, a demonic\r\ncreature from the underworld. The fellowship flees this creature\r\nas the mines collapse. The fellowship emerges from the mines saddened by\r\nthe loss of Gandalf, but Aragorn insists they have no time to mourn\r\nand must press on. That evening, the Lady and\r\nFrodo speak in private. She asks him to look into a mirror, which\r\nis a basin of water, and tell her what he sees. She warns him\r\nthat the fellowship is breaking and that one by one the ring will\r\ndestroy them all. If he does not accomplish the task, no one will. The next\r\nday, the fellowship departs in boats down the river. After docking on dry land, Frodo wanders off, and Boromir\r\nfollows. He is about to attack Frodo for it when Frodo puts on\r\nthe ring and disappears. Boromir also fights valiantly\r\nbut is badly wounded. The movie begins with Gandalf falling into the mine with\r\nthe Balrog. Then he lands in a body of water. Théoden is transformed from elderly\r\nto middle-aged and from weak to strong, and he banishes Wormtongue. Frodo defends Gollum to Sam. In a dream, Arwen encourages Aragorn to stay the course\r\nand not falter. Her father wants her to go off with the other elves\r\nto eternal life. Aragorn tells her that their love is over and she\r\nshould go. Aragorn appears to die as he falls\r\nover a cliff in the clutches of a hyenalike creature. Aragorn’s horse resuscitates him and carries him to Helm’s\r\nDeep. Do we elves\r\nleave Middle-earth to its fate? she implores Elrond. He wants to know of his brother’s\r\ndeath. Then an elf army of bowmen led by the warrior\r\nHaldir arrive. After that, a ferocious battle rages. The Uruk-hai raise ladders\r\nand scale the walls of Helm’s Deep. The elf-human army fights bravely,\r\nbut the oncoming Uruk-hai are difficult to withstand. They pierce\r\nthe castle walls and force the defending army deep within the castle. Haldir is killed in battle. Meanwhile, the Ents have gathered to debate whether to\r\ngo to war. They speak incredibly slowly and take a long time to\r\nmake decisions. He blames Saruman for\r\nthe destruction and decides to rally the other Ents to war. The\r\nEnts attack Saruman\'s tower and destroy its defenses. They open a dam and\r\nthe rushing water floods the entire plain surrounding the tower. The battle for Middle-earth,\r\nthey know, has just begun. Sam encourages him with a stirring speech about\r\nheroism and fighting for good. In a flashback, we see Sméagol, a hobbit, happily fishing\r\nwith a friend. The friend falls into the water and reemerges holding\r\na ring. Sméagol wants the ring and strangles his friend to death. He says he forgot what life was like outside\r\nhis cave. He even forgot his own name. Sam says he’s begun to ration\r\nthe little food they have left. The stone nearly\r\nkills Pippin, who is revived by Gandalf. She says that if she leaves\r\nnow, she’ll regret it forever. Gandalf calls upon Denethor to raise an army and\r\ncall upon his allies. Faramir agrees, even though it is clearly a suicide mission. Frodo decides that Sam, not Gollum, is the problem\r\nand decides to continue on with only Gollum. He\r\nis roused by a messenger, who informs him a stranger has come. For Aragorn, saving Middle-earth is now bound\r\nup with saving the life of his love. These mountain-dwellers are crooks, murderers, and traitors,\r\nbut they will respond to the king of Gondor. Éowyn confesses\r\nher love to Aragorn, but he tells her he is committed to another. He rides into the mountain with Legolas and Gimli. Suddenly, swarms\r\nof ghostly warriors appear. The orc army catapults the heads of his dead companions\r\ninto the city. Pippin insists that Faramir is not dead, but Denethor\r\nis unconvinced. He understands Gollum’s deceit\r\nand turns around. In the cave, Frodo gets stuck in a web. They struggle, and Gollum falls over a cliff. Frodo\r\ncontinues to Mordor on his own. However, Shelob creeps behind him,\r\nstings him, and spins a thick web around him. Sam abandons the body when\r\na few orcs come down the path. They pick up Frodo’s body and carry\r\nit off with them. On the battlefield, the witch-king\r\nis about to kill Théoden, but Éowyn and Merry intervene. Merry distracts\r\nthe creature, and Éowyn kills it. The field is calm, and the battle\r\nseems won. Aragorn releases the men of the mountain, and they disappear. Pippin and Merry reunite on the battlefield. Frodo awakes in Mordor. He is chained and half naked. His things have been taken from him, including the ring. Sam enters\r\nthe orc stronghold where Frodo is held captive and rescues Frodo. He took it when he thought Frodo was dead. Though a little reluctant\r\nto return it to Frodo, he agrees to. The two friends dress in orc\r\narmor and go onto the plains of Mordor. He suggests they march upon Mordor to distract Sauron. Nevertheless, the passage is far from easy. They have little water left. They drink the last drops and accept\r\nthat there will be no return journey. Instead, he declares\r\nthe ring his and puts it on. Sam pulls him up\r\nas the ring disappears into the sea of fire. The tower of Mordor begins to collapse and\r\nthen explodes. Mount Doom erupts, flooding the plain with lava. They prepare for their deaths, but Gandalf swoops by\r\non a giant eagle and picks them up. Frodo awakens in a luxurious bed with Gandalf by his side. The remaining fellowship is there, too. Aragorn is crowned king\r\nat a ceremony in Gondor. Legolas and the elves arrive, along with\r\nArwen. She and Aragorn kiss. Then the whole crowd bows before the\r\nfour hobbits. The fellowship is declared over, and the fourth age\r\nof Middle-earth begins. Sam sees the girl he used to have a\r\ncrush on and talks to her. Shortly thereafter, they are married. Frodo\r\nwrites his adventures in the same manuscript in which Bilbo wrote\r\nhis. ',0,0,'lord.jpg'),(7,'Jungle Book','Rudyard Kipling','Adventure',' Mowgli endures a variety of trials and tribulations as he grows up in an Indian jungle. Mowgli does not want to identify as a human because he is all too aware of what humans signify for the jungle: greed and destruction. Humans, however, are an enigma. Greed is not an inherent trait. These stories usually end with verse or song lyrics recited by the main character, thus summarizing the story. He is subsequently raised by these wolves as one of their pack. “Tiger, Tiger” reveals Mowgli’s major struggles. He is kicked out of his wolf pack due to the jealous machinations of others. He tries to fit into human society, but finds himself again faced with myriad trials. He then shares all of the knowledge he has gained from traveling the world with the other seals. The story centers on an elusive elephant dance, plus an elephant and his handler. The reader can take delight in witnessing animals reasoning in the same manner as humans. As Mowgli must wonder: who is the real savage and who is true to its nature, in the end',0,0,'jungle.jpg'),(8,'Dopamine Detox','Thibaut Meurisse','Information','Dopamine Detox: A Quick Guide to Eliminate Distractions and Get Your Brain to Perform Hard Things is a useful tool for anybody trying to understand the function of dopamine in their life and how it influences their capacity to concentrate, be productive, and accomplish their goals. The book offers a simple and useful how-to for doing a dopamine detox, complete with detailed directions and advice for overcoming obstacles and keeping up the detox over time.\r\nReaders may enhance their mental health, raise their motivation and productivity, and feel better overall by decreasing excessive dopamine stimulation. The book places a strong emphasis on maintaining a healthy balance of dopamine in the brain and offers advice for preventing future bouts of overstimulation.\r\nDopamine Detox is, all things considered, a crucial tool for anybody trying to maintain their brain health and accomplish their goals by avoiding distractions and developing good habits.\r\n',0,0,'dopamine.jpg'),(9,'Court Of Owls','Micheal C Hall','Fiction',' The court splintered off from the Tribe of Judas, a cult worshipping a cosmic bat deity known as Barbatos. They watch you at your hearth, they watch you in your bed, speak not a whispered word of them or they\'ll send The Talon for your head.\". During the 19th century, the Court of Owls had some arrangement with Alan Wayne of Wayne Enterprises. The Court made enemies of Alan when he learned of their greater plans and their mass influence drove him insane. The court later faked the death as having been from the fall to the sewer. Interested in the case, Bruce donned the Batsuit and arrived on the scene. Bullock wondered if the symbol on the knives had anything to do with the old nursery rhyme about The Court of Owls. Batman quickly sent the skin cells to Alfred Pennyworth, who is back at the Batcave, for DNA recognition. Bruce dismissed the possibility that the fabled Court of Owls exists, not thinking them much of the threat. Almost immediately, Talon burst from an elevator, leaving two deceased security guards in his wake. After plunging a knife in Lincoln\'s chest, the Talon attacked Bruce. Bruce managed to catch a gargoyle on his way down, shaking off the Talon who hit the street below. He was suspected to have been killed by the Court of Owls as he had ranted about owls hunting him in the days leading up to his death. However, no one believed him at the time, dismissing his fears as the effects of senility. He desperately tried to find a way out of the maze while the Talon watched him from the shadows. Upon finding a weak tile on the floor, he ripped it out and entered a room filled with pictures of Batman. He screams \"I\'m not listening! I\'m not listening to you!\" while the Talon slowly walked up to him and impaled him from behind with a sword. Weakened and close to succumbing, Bruce contemplated surrendering to his fate and meeting his end at the hands of the Court. Then he spotted a broken portrait of his ancestor Alan Wayne. She then turned to the room filled with caskets, all filled with Talons, and gives the order to wake them all up for the war against Batman.',0,0,'court.jpg'),(10,'Pet Cementary','Stephen King','Horror','  Pet SemataryThanks for exploring this SuperSummary Study Guide of “Pet Sematary” by Stephen King. It was adapted into a film in 1989 and a second film adaptation is scheduled to be released in April 2019. An elderly neighbor, Jud, comes to help, and he and Louis become fast friends, with Louis viewing Jud as a surrogate father. Louis then dreams that Victor leads him to the pet cemetery and warns him not to go beyond the wooden deadfall. Even though Louis wakes up covered in dirt, he attempts to dismiss the dream as a case of somnambulism. On Halloween, Jud’s wife, Norma, almost dies of a heart attack but Louis is able to save her. Louis’s family goes back to Chicago for Thanksgiving, but Louis stays in town. Church comes back the next day but Louis notices that the cat has changed and become obsessed with eviscerating small animals. However, Rachel arrives too late, and a possessed Gage ends up murdering her and Jud. The first section comprises Louis’s introduction to the pet cemetery and the resurrection of Church. In fact, King himself references the monkey’s paw multiple times in the novel infairly blatant authorial winks to the audience. The most prevalent theme of the novel is dead is better.',0,0,'StephenKingPetSematary.jpg');
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
INSERT INTO `users` VALUES (1,'Anubhav','1234','abubhav@gmail.com','static/images/profile2.jpg'),(2,'Divyansh12323','1234','Anubhav@gmail.com','static/images/profile2.jpg'),(3,'Dexter_morgan','dexter','dexter@gmail.com','static/images/profile2.jpg'),(5,'Dexter_morgan1234','dexter','dexter1234@gmail.com','static/images/profile2.jpg'),(6,'Samyak_123456','samyak','sasmyak@gmail.com','static/images/profile2.jpg'),(7,'Samyak_123456789','samyak','sasmyak123@gmail.com','static/images/profile2.jpg'),(8,'Deborah_1234','12345','debra@gmail.com','static/images/profile2.jpg'),(9,'masuka_12345','masuka','masuka@gmail.com','static/images/profile2.jpg'),(11,'abhi12345678','1234','Anubhav34567@gmail.com','static/images/profile2.jpg'),(12,'abhi6732564837','1234','Anubhav2345@gmail.com','static/images/profile2.jpg'),(13,'Divyansh12323456456','123','Anubhav234@gmail.com','static/images/profile2.jpg'),(14,'Divyansh12323vtty','123','Anubhav@fdh.com','static/images/profile2.jpg'),(16,'Divyansh123235678','1234','Anubhav23456789@gmail.com','static/images/profile2.jpg'),(17,'crime12345678','1234','Anubhav98@gmail.com','static/images/profile2.jpg'),(18,'print123456','1234','Anubhav87@gmail.com','static/images/profile2.jpg'),(19,'fight_every_night','1234','Anubhav54yvt5tg@gmail.com','static/images/profile2.jpg'),(20,'fight_night','1234','Anubhavf4rij@gmail.com','static/images/profile2.jpg'),(21,'fight_night123','1234','Anubhavf4h@gmail.com',''),(22,'fight_you_bitch','1234','Anubhav4465@gmail.com',''),(23,'fight_fight_fight','1234','Anubhavf4rvjb@gmail.com',''),(24,'micheal_c_hall','12345','micheal@gmail.com',''),(25,'comeonnnnnnnnnn','12345','canon@gmail.com',''),(26,'aayushnariyahayehaye','123456','anubhav34@gmail.com',''),(27,'aayushbirjubujurg','123456','hellobrother34@gmail.com',''),(28,'chachachachity','123456','gibber34@gmail.com',''),(29,'chachitaujihaiidhar','123456','pilank23@gmail.com',''),(30,'chappaljoote','123456','pillo45@gmail.com',''),(31,'tautaichachachacahi','123456','jijaji23@gmail.com',''),(32,'Billu123456789','1234','billu@gmail.com','E:\\Bookrating\\static/images\\pyongyang.jpg'),(33,'Billu123456trefh','123','bill@gmail.com','E:\\Bookrating\\static/images\\pyongyang.jpg'),(34,'cerwverb','1234','Anubhav23rd@gmail.com','E:\\Bookrating\\static/images\\12.jpg'),(35,'ViratKohl','1234','qwerdc@gmail.com','E:\\Bookrating\\static/images\\batman.jpg'),(36,'why_does','123456','Billu12345678934d@gmail.com','E:\\Bookrating\\static/images\\one_nine.jpg'),(37,'ffwefh','123','Billu123456789fwrkj@gmail.com',''),(38,'Why','12345','why@gmail.com','E:\\Bookrating\\static/images\\dexter.jpg'),(39,'oops','fuck','oops@gmail.com','E:\\Bookrating\\static/images\\berserk.jpg'),(40,'Bill123','123','Billu123456789@rediffmail.com','static/images/chainsaw.jpg'),(41,'Paul','rita','paul@gmail.com','.../static/images'),(42,'Paulrud','1234','paulo@gmail.com','.../static/images'),(43,'Dark_pas','123456','darkpassenger@gmail.com','E:\\Bookrating\\static/images\\dexter.jpg'),(44,'Dex','12345','bruh@gmail.com',''),(45,'Dex1','12345','bruh1@gmail.com','static/images/12.jpg'),(46,'Ranjha','123456','Bill123wer@gmail.com',''),(48,'Ranjhah','123456','Bill123wer9@gmail.com',''),(50,'gegcg','123456','Bill123wdcf@gmail.com',''),(51,'rinku','hello','Bill123fwehj@gmail.com','static/images/court.jpg');
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
