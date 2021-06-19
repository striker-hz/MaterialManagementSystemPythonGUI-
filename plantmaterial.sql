/*
Navicat MySQL Data Transfer

Source Server         : H_Database
Source Server Version : 50730
Source Host           : localhost:3306
Source Database       : plantmaterial

Target Server Type    : MYSQL
Target Server Version : 50730
File Encoding         : 65001

Date: 2021-06-19 11:35:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for materialfour
-- ----------------------------
DROP TABLE IF EXISTS `materialfour`;
CREATE TABLE `materialfour` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `MatName` varchar(255) NOT NULL,
  `MatRepertory` int(11) NOT NULL DEFAULT '0',
  `Price` int(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of materialfour
-- ----------------------------
INSERT INTO `materialfour` VALUES ('1', '温控器', '600', '300');
INSERT INTO `materialfour` VALUES ('2', '保险丝', '330', '300');
INSERT INTO `materialfour` VALUES ('3', '发热丝', '500', '0');
INSERT INTO `materialfour` VALUES ('4', '发热管', '300', '0');
INSERT INTO `materialfour` VALUES ('5', '铁铬线', '500', '0');
INSERT INTO `materialfour` VALUES ('6', '电机', '890', '0');
INSERT INTO `materialfour` VALUES ('7', '线材和端子', '850', '0');
INSERT INTO `materialfour` VALUES ('8', '不锈铁', '470', '0');

-- ----------------------------
-- Table structure for materiallib
-- ----------------------------
DROP TABLE IF EXISTS `materiallib`;
CREATE TABLE `materiallib` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `MaterialName` varchar(255) NOT NULL,
  `RelativeLib` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of materiallib
-- ----------------------------
INSERT INTO `materiallib` VALUES ('1', '塑料', 'MaterialLibOne');
INSERT INTO `materiallib` VALUES ('2', '五金原材料', 'MaterialLibTwo');
INSERT INTO `materiallib` VALUES ('3', '电子类材料', 'MaterialLibThree');
INSERT INTO `materiallib` VALUES ('4', '电器类材料', 'MaterialLibFour');

-- ----------------------------
-- Table structure for materialone
-- ----------------------------
DROP TABLE IF EXISTS `materialone`;
CREATE TABLE `materialone` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `MatName` varchar(255) NOT NULL,
  `MatRepertory` int(11) NOT NULL DEFAULT '0',
  `Price` int(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of materialone
-- ----------------------------
INSERT INTO `materialone` VALUES ('1', '通用塑料', '770', '100');
INSERT INTO `materialone` VALUES ('2', '工程塑料', '190', '200');
INSERT INTO `materialone` VALUES ('3', '特种塑料', '880', '300');
INSERT INTO `materialone` VALUES ('4', '热塑胶', '330', '0');

-- ----------------------------
-- Table structure for materialthree
-- ----------------------------
DROP TABLE IF EXISTS `materialthree`;
CREATE TABLE `materialthree` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `MatName` varchar(255) NOT NULL,
  `MatRepertory` int(11) NOT NULL DEFAULT '0',
  `Price` int(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of materialthree
-- ----------------------------
INSERT INTO `materialthree` VALUES ('1', '电阻', '1000', '0');
INSERT INTO `materialthree` VALUES ('2', '电容器', '1000', '0');
INSERT INTO `materialthree` VALUES ('3', '电磁铁', '2170', '0');
INSERT INTO `materialthree` VALUES ('4', '电池', '1000', '0');
INSERT INTO `materialthree` VALUES ('5', '二极管', '3780', '0');
INSERT INTO `materialthree` VALUES ('6', 'LED灯', '700', '0');
INSERT INTO `materialthree` VALUES ('7', 'PCB板', '700', '0');
INSERT INTO `materialthree` VALUES ('8', '蜂鸣器', '1000', '0');
INSERT INTO `materialthree` VALUES ('9', '助焊剂', '800', '0');
INSERT INTO `materialthree` VALUES ('10', '清洁剂', '890', '0');

-- ----------------------------
-- Table structure for materialtwo
-- ----------------------------
DROP TABLE IF EXISTS `materialtwo`;
CREATE TABLE `materialtwo` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `MatName` varchar(255) NOT NULL,
  `MatRepertory` int(11) NOT NULL DEFAULT '0',
  `Price` int(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of materialtwo
-- ----------------------------
INSERT INTO `materialtwo` VALUES ('3', '镀锌板', '1200', '200');
INSERT INTO `materialtwo` VALUES ('4', '冷板', '110', '0');
INSERT INTO `materialtwo` VALUES ('5', '电解板', '900', '0');
INSERT INTO `materialtwo` VALUES ('6', '锌铝板', '700', '0');
INSERT INTO `materialtwo` VALUES ('7', '铝板', '700', '0');
INSERT INTO `materialtwo` VALUES ('11', '热固胶', '600', '0');

-- ----------------------------
-- Table structure for usertable
-- ----------------------------
DROP TABLE IF EXISTS `usertable`;
CREATE TABLE `usertable` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `PName` varchar(255) NOT NULL,
  `UserName` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `Phone` varchar(255) NOT NULL DEFAULT '0',
  `Sex` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL DEFAULT '员工',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of usertable
-- ----------------------------
INSERT INTO `usertable` VALUES ('11', 'zhang', '110101', '123123', '17835345228', '男', '员工');
INSERT INTO `usertable` VALUES ('12', 'heng', 'root', 'admin', '13593560572', '男', '管理员');
INSERT INTO `usertable` VALUES ('13', 'Ann', '110103', '123123', '18735655010', '男', '员工');
INSERT INTO `usertable` VALUES ('16', 'jOB', '110105', '000000', '13593560572', '男', '员工');
INSERT INTO `usertable` VALUES ('17', 'Bnn', '110106', '000000', '123456789', '男', '员工');

-- ----------------------------
-- Procedure structure for numberOne
-- ----------------------------
DROP PROCEDURE IF EXISTS `numberOne`;
DELIMITER ;;
CREATE DEFINER=`root`@`%` PROCEDURE `numberOne`()
    COMMENT '查询各个仓库物料的现存数量'
BEGIN
 
(select MatName,MatRepertory from materialone)
UNION ALL (select MatName,MatRepertory from materialtwo)
UNION ALL (select MatName,MatRepertory from materialthree)
UNION ALL (select MatName,MatRepertory from materialfour);
 
END
;;
DELIMITER ;
