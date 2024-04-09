SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- 大学专业信息表结构
-- ----------------------------
DROP TABLE IF EXISTS `university_major_information`;
CREATE TABLE `university_major_information` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `university_name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '大学名称',
  `major` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '专业名称',
  `research_direction` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '研究方向',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- 大学专业信息表数据
-- ----------------------------
BEGIN;
INSERT INTO `university_major_information` (`id`, `university_name`, `major`, `research_direction`, `create_time`, `update_time`) VALUES (1, '北京工业大学', '数学', '应用数学', '2024-04-09 14:54:14', '2024-04-09 14:54:14');
INSERT INTO `university_major_information` (`id`, `university_name`, `major`, `research_direction`, `create_time`, `update_time`) VALUES (2, '北京工业大学', '数学', '基础数学', '2024-04-09 14:54:14', '2024-04-09 14:54:14');
INSERT INTO `university_major_information` (`id`, `university_name`, `major`, `research_direction`, `create_time`, `update_time`) VALUES (3, '北京工业大学', '物理', '应用物理', '2024-04-09 14:54:14', '2024-04-09 14:54:14');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
