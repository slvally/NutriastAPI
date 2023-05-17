/*
 Navicat Premium Data Transfer

 Source Server         : RFsql
 Source Server Type    : MySQL
 Source Server Version : 100418
 Source Host           : localhost:3306
 Source Schema         : nutriast

 Target Server Type    : MySQL
 Target Server Version : 100418
 File Encoding         : 65001

 Date: 17/05/2023 23:17:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `password` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'rafi', 'muhammadrafishidiq@gmail.com', 'shidiqs');
INSERT INTO `users` VALUES (6, 'Alice', 'Alice@gmail.com', 'qwertyalice');
INSERT INTO `users` VALUES (8, 'Kurumi', 'tokisakikurumi@gmail.com', 'admin');

SET FOREIGN_KEY_CHECKS = 1;
