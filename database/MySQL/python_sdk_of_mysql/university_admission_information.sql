SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- 大学录用信息表结构
-- ----------------------------
DROP TABLE IF EXISTS `university_admission_information`;
CREATE TABLE `university_admission_information` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `university_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '大学名称',
  `major` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '专业名称',
  `num_of_major_admissions` int(11) DEFAULT NULL COMMENT '专业招生人数',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- 大学录用信息表数据
-- ----------------------------
BEGIN;
INSERT INTO `university_admission_information` (`id`, `university_name`, `major`, `num_of_major_admissions`, `create_time`, `update_time`) VALUES (1, '北京工业大学', '数学', 12, '2024-04-09 14:54:14', '2024-04-09 14:54:14');
INSERT INTO `university_admission_information` (`id`, `university_name`, `major`, `num_of_major_admissions`, `create_time`, `update_time`) VALUES (2, '北京工业大学', '物理', 11, '2024-04-09 14:54:14', '2024-04-09 14:54:14');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
