-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1
-- 生成日期： 2023-05-20 11:36:39
-- 服务器版本： 10.4.18-MariaDB
-- PHP 版本： 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `gpsdatabase`
--

-- --------------------------------------------------------

--
-- 表的结构 `knowledge`
--

CREATE TABLE `knowledge` (
  `create_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `alu_id` int(11) DEFAULT NULL,
  `program_id` int(11) DEFAULT NULL,
  `alumniname` varchar(50) NOT NULL,
  `coursename` varchar(50) NOT NULL,
  `universityname` varchar(50) NOT NULL,
  `programname` varchar(50) NOT NULL,
  `comment` varchar(200) NOT NULL,
  `year_visible` int(3) NOT NULL,
  `gender_visible` int(3) NOT NULL,
  `name_visible` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `knowledge`
--

INSERT INTO `knowledge` (`create_time`, `id`, `alu_id`, `program_id`, `alumniname`, `coursename`, `universityname`, `programname`, `comment`, `year_visible`, `gender_visible`, `name_visible`) VALUES
(NULL, 1, 3, 5, 'abc', 'BA', 'HKU', 'FIN', 'Finance is a term broadly describing the study and system of money, investments', 1, 1, 1),
(NULL, 2, 4, 1, 'bbb', 'OOP', 'UIC', 'CST', ' a programming paradigm based on the concept of object', 1, 1, 0),
(NULL, 3, 4, 2, 'qjb', 'CG', 'UIC', 'CST', 'Computer Graphics can be used in UI design, rendering', 1, 0, 1),
(NULL, 4, 2, 5, 'prw', 'DS', 'UIC', 'DS', 'data structure, way in which data are stored for efficient search and retrieval.', 0, 1, 1),
(NULL, 5, 2, 2, 'prw', 'NLP', 'UIC', 'CST', 'Natural language processing (NLP)is the discipline of building machines that can manipulate human language ', 0, 0, 0),
(NULL, 8, 8, 6, 'admin', 'jji', 'xx', '学校', 'fvtvgb', 0, 1, 1),
(NULL, 9, 8, 3, 'admin', 'dsfs', 'xx', 'sad', 'asdasd', 0, 1, 1),
(NULL, 10, 8, 1, 'admin', 'sa', 'xx', 'asda', 'qwdqd', 0, 1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `offer`
--

CREATE TABLE `offer` (
  `create_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `year` int(11) DEFAULT NULL,
  `photocopy` varchar(50) DEFAULT NULL,
  `GPA` float DEFAULT NULL,
  `reality` int(11) DEFAULT NULL,
  `uicer_id` int(11) DEFAULT NULL,
  `programe` varchar(50) DEFAULT NULL,
  `universityname` varchar(50) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `companyname` varchar(50) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `supervisor` varchar(50) DEFAULT NULL,
  `researchtopic` varchar(50) DEFAULT NULL,
  `nopapers` int(1) DEFAULT NULL,
  `noresearch` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `offer`
--

INSERT INTO `offer` (`create_time`, `id`, `year`, `photocopy`, `GPA`, `reality`, `uicer_id`, `programe`, `universityname`, `title`, `companyname`, `country`, `qualification`, `supervisor`, `researchtopic`, `nopapers`, `noresearch`) VALUES
(NULL, 1, 2021, '../offerImages/offer1.png', 3.8, 1, 1, 'DS', 'HKU', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(NULL, 2, 2021, '../offerImages/offer2.png', 3.8, 1, 1, 'DS', 'HKU', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(NULL, 3, 2021, '../offerImages/offer3.png', 3.7, 1, 2, 'ACCT', 'QAD', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(NULL, 4, 2019, NULL, 3.5, 0, 4, 'DS', 'HKU', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(NULL, 5, 2019, '../offerImages/offer4.png', 3.5, 1, 4, 'FIN', 'XP', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(NULL, 6, 2022, '../offerImages/offer5.png', 3.1, 1, 6, 'CST', 'UIC', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(NULL, 7, 2022, '../offerImages/qjb.png', 3.8, 1, 1, 'CST', 'UIC', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(NULL, 8, 2022, '../offerImages/qjb.png', 3.8, 1, 1, 'CST', 'UIC', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(NULL, 31, 2022, '../offerImages/offer2.png', 3.7, 1, 2, 'CS', 'Cambridge', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(NULL, 32, 2023, '../offerImages/offer2.png', 3.8, 1, 1, 'CS', 'Cambridge', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(NULL, 33, 2020, '../offerImages/GenshinlmpactPhoto 2022_11_19 00_49', 3.7, 1, 2, 'xx', 'xx', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(NULL, 34, 2020, '../offerImages/GenshinlmpactPhoto 2022_11_19 00_49', 3.7, 1, 2, 'xx', 'xx', NULL, NULL, NULL, NULL, '2022', '3.7', 1, 2),
(NULL, 35, 2020, '../offerImages/GenshinlmpactPhoto 2022_11_19 00_49', 3.7, 1, 2, '', '', 'ff', 'ff', 'ff', 'fff', NULL, NULL, NULL, NULL),
(NULL, 36, 2020, '../offerImages/GenshinlmpactPhoto 2022_11_19 00_49', 3.8, 1, 1, '', '', 'hh', 'hh', 'hh', 'hh', NULL, NULL, NULL, NULL),
(NULL, 37, 2020, '../offerImages/GenshinlmpactPhoto 2022_11_19 00_49', 3.8, 1, 1, '', '', 'll', 'll', 'll', 'll', NULL, NULL, NULL, NULL),
(NULL, 38, 2020, '../offerImages/GenshinlmpactPhoto 2022_11_19 00_49', 3.8, 1, 1, '', '', 'vv', 'vv', 'vv', 'v', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `program`
--

CREATE TABLE `program` (
  `create_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `universityname` varchar(50) DEFAULT NULL,
  `GPAlow` float DEFAULT NULL,
  `GPAupper` float DEFAULT NULL,
  `university_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `program`
--

INSERT INTO `program` (`create_time`, `id`, `name`, `universityname`, `GPAlow`, `GPAupper`, `university_id`) VALUES
(NULL, 1, 'CST', 'UIC', 2.8, 3.5, 1),
(NULL, 2, 'DS', 'QAD', 2.7, 3.7, 2),
(NULL, 3, 'ACCT', 'NDH', 2.1, 3.4, 3),
(NULL, 4, 'FIN', 'XP', 2.8, 3.2, 4),
(NULL, 5, 'DS', 'HKU', 3.2, 4, 5),
(NULL, 6, 'CST', 'SGL', 3.5, 4, 6),
(NULL, 8, 'CS', 'Cambridge', 3.7, 3.8, 15),
(NULL, 9, 'xx', 'xx', 3.7, 3.7, 16);

-- --------------------------------------------------------

--
-- 表的结构 `report`
--

CREATE TABLE `report` (
  `create_time` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `year` int(11) NOT NULL,
  `totaloffers` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `report`
--

INSERT INTO `report` (`create_time`, `id`, `year`, `totaloffers`) VALUES
(NULL, 1, 2021, 3),
(NULL, 2, 2022, 4),
(NULL, 3, 2019, 2),
(NULL, 4, 2020, 6);

-- --------------------------------------------------------

--
-- 表的结构 `ui_cer`
--

CREATE TABLE `ui_cer` (
  `create_time` int(11) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `id` int(11) NOT NULL,
  `college` varchar(50) NOT NULL,
  `GPA` float NOT NULL,
  `status` int(11) NOT NULL,
  `gender` enum('male','female') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `ui_cer`
--

INSERT INTO `ui_cer` (`create_time`, `name`, `age`, `email`, `password`, `id`, `college`, `GPA`, `status`, `gender`) VALUES
(NULL, 'qjb', 21, 'q030026117@mail.uic.edu.cn', 'qqqqqq', 1, 'UIC', 3.8, 1, 'male'),
(NULL, 'prw', 21, 'q030026116@mail.uic.edu.cn', '111111', 2, 'UIC', 3.7, 2, 'female'),
(NULL, 'abc', 24, 'n030026116@mail.uic.edu.cn', '123456', 3, 'HKU', 3.9, 2, 'male'),
(NULL, 'bbb', 22, 'm030026777@mail.uic.edu.cn', '111111', 4, 'UIC', 3.5, 2, 'male'),
(NULL, 'sadasd', 22, '1622322626@qq.com', '222222', 5, 'PPL', 2, 1, 'male'),
(NULL, 'grr', 21, 'q030026039@mai.uic.edu.cn', '53421', 6, 'UIC', 3.1, 1, 'female'),
(NULL, 'zxy', 21, 'q030026208@mail.uic.edu.cn', 'aaaaa', 7, 'UIC', 4, 1, 'female'),
(NULL, 'admin', 45, 'admin@uic.edu.cn', 'aaaaaa', 8, 'UIC', 0, 3, 'female'),
(NULL, 'Vicky', 20, 'prwrongwei@gmail.com', '123456', 10, 'UIC', 3.6, 2, 'male'),
(NULL, '钱景彬', 20, 'jingbinqian@outlook.com', '123456', 11, 'UIC', 3.7, 2, 'male');

-- --------------------------------------------------------

--
-- 表的结构 `university`
--

CREATE TABLE `university` (
  `create_time` int(11) DEFAULT NULL,
  `name` varchar(50) NOT NULL,
  `programlist` varchar(50) DEFAULT NULL,
  `id` int(11) NOT NULL,
  `city` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 转存表中的数据 `university`
--

INSERT INTO `university` (`create_time`, `name`, `programlist`, `id`, `city`) VALUES
(NULL, 'UIC', 'CST', 1, 'zhuhai'),
(NULL, 'QAD', 'DS', 2, 'xinjiang'),
(NULL, 'NDH', 'ACCT', 3, 'ningbo'),
(NULL, 'XP', 'FIN', 4, 'suzhou'),
(NULL, 'HKU', 'DS', 5, 'hongkong'),
(NULL, 'SGL', 'CST', 6, 'singapore'),
(NULL, 'Cambridge', '', 15, 'UK Cambridge'),
(NULL, 'xx', '', 16, 'zz'),
(NULL, 'dd', '', 17, 'dd');

--
-- 转储表的索引
--

--
-- 表的索引 `knowledge`
--
ALTER TABLE `knowledge`
  ADD PRIMARY KEY (`id`),
  ADD KEY `alu_id` (`alu_id`),
  ADD KEY `program_id` (`program_id`);

--
-- 表的索引 `offer`
--
ALTER TABLE `offer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `uicer_id` (`uicer_id`);

--
-- 表的索引 `program`
--
ALTER TABLE `program`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `universityname` (`universityname`),
  ADD KEY `university_id` (`university_id`);

--
-- 表的索引 `report`
--
ALTER TABLE `report`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `ui_cer`
--
ALTER TABLE `ui_cer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- 表的索引 `university`
--
ALTER TABLE `university`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `city` (`city`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `knowledge`
--
ALTER TABLE `knowledge`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- 使用表AUTO_INCREMENT `offer`
--
ALTER TABLE `offer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- 使用表AUTO_INCREMENT `program`
--
ALTER TABLE `program`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- 使用表AUTO_INCREMENT `report`
--
ALTER TABLE `report`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用表AUTO_INCREMENT `ui_cer`
--
ALTER TABLE `ui_cer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- 使用表AUTO_INCREMENT `university`
--
ALTER TABLE `university`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- 限制导出的表
--

--
-- 限制表 `knowledge`
--
ALTER TABLE `knowledge`
  ADD CONSTRAINT `knowledge_ibfk_1` FOREIGN KEY (`alu_id`) REFERENCES `ui_cer` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `knowledge_ibfk_2` FOREIGN KEY (`program_id`) REFERENCES `program` (`id`) ON DELETE CASCADE;

--
-- 限制表 `offer`
--
ALTER TABLE `offer`
  ADD CONSTRAINT `offer_ibfk_1` FOREIGN KEY (`uicer_id`) REFERENCES `ui_cer` (`id`) ON DELETE CASCADE;

--
-- 限制表 `program`
--
ALTER TABLE `program`
  ADD CONSTRAINT `program_ibfk_1` FOREIGN KEY (`university_id`) REFERENCES `university` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
