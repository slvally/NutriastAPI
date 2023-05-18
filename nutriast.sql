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

 Date: 19/05/2023 00:25:23
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for intake_users
-- ----------------------------
DROP TABLE IF EXISTS `intake_users`;
CREATE TABLE `intake_users`  (
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
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of intake_users
-- ----------------------------
INSERT INTO `intake_users` VALUES (1, 15, 'good', 200, 120, 2000, 40, 200, NULL);

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `Username` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Email` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Password` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `BirthDate` date NOT NULL,
  `Gender` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `Height` int NOT NULL,
  `Weight` int NOT NULL,
  `FatNeed` int NULL DEFAULT NULL,
  `ProteinNeed` int NULL DEFAULT NULL,
  `CaloryNeed` int NULL DEFAULT NULL,
  `FiberNeed` int NULL DEFAULT NULL,
  `CarbohidrateNeed` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (15, 'Slvally', 'kyurem@gmail.com', 'admin', '2011-04-05', 'male', 169, 45, 0, 0, 0, 0, 0);
INSERT INTO `users` VALUES (16, 'JohnDoe', 'johndoe@example.com', 'password', '1990-01-01', 'Male', 180, 75, 200, 120, 2000, 40, 200);

SET FOREIGN_KEY_CHECKS = 1;
