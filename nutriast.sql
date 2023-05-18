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

 Date: 18/05/2023 12:47:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for intake
-- ----------------------------
DROP TABLE IF EXISTS `intake`;
CREATE TABLE `intake`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `HealthStatus` char(16) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  `FatIntake` int NULL DEFAULT NULL,
  `ProteinIntake` int NULL DEFAULT NULL,
  `CaloryIntake` int NULL DEFAULT NULL,
  `FiberIntake` int NULL DEFAULT NULL,
  `CarbohidrateIntake` int NULL DEFAULT NULL,
  `Feedback` varchar(1024) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `UserIntake`(`user_id` ASC) USING BTREE,
  CONSTRAINT `UserIntake` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of intake
-- ----------------------------

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `password` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `gender` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `BirthDate` date NOT NULL,
  `Height` int NOT NULL,
  `weight` int NOT NULL,
  `FatNeed` int NULL DEFAULT NULL,
  `ProteinNeed` int NULL DEFAULT NULL,
  `CaloryNeed` int NULL DEFAULT NULL,
  `FiberNeed` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of users
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
