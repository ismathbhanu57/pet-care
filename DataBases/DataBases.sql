/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 8.0.25 : Database - pets_cares_owners_communication_systems
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pets_cares_owners_communication_systems` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `pets_cares_owners_communication_systems`;

/*Table structure for table `admin` */

DROP TABLE IF EXISTS `admin`;

CREATE TABLE `admin` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=93 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `friends_requests` */

DROP TABLE IF EXISTS `friends_requests`;

CREATE TABLE `friends_requests` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `from_email` varchar(254) NOT NULL,
  `to_email` varchar(254) NOT NULL,
  `status` varchar(100) NOT NULL,
  `customers_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Friends_Requests_from_email_to_email_1173f575_uniq` (`from_email`,`to_email`),
  KEY `Friends_Requests_customers_id_19a93329_fk_pets_care` (`customers_id`),
  CONSTRAINT `Friends_Requests_customers_id_19a93329_fk_pets_care` FOREIGN KEY (`customers_id`) REFERENCES `pets_cares_owners_communication_systems_app_customer` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `notifications` */

DROP TABLE IF EXISTS `notifications`;

CREATE TABLE `notifications` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `ndate_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_add_comments` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_add_comments`;

CREATE TABLE `pets_cares_owners_communication_systems_app_add_comments` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_email` varchar(254) NOT NULL,
  `comments` varchar(100) NOT NULL,
  `date_time` datetime(6) NOT NULL,
  `posts_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pets_cares_owners_co_posts_id_cd57d8ed_fk_pets_care` (`posts_id`),
  CONSTRAINT `pets_cares_owners_co_posts_id_cd57d8ed_fk_pets_care` FOREIGN KEY (`posts_id`) REFERENCES `pets_cares_owners_communication_systems_app_add_posts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_add_posts` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_add_posts`;

CREATE TABLE `pets_cares_owners_communication_systems_app_add_posts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `only_for` varchar(100) NOT NULL,
  `pfile` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `date_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_appoitments` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_appoitments`;

CREATE TABLE `pets_cares_owners_communication_systems_app_appoitments` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doctor_email` varchar(254) NOT NULL,
  `customer_email` varchar(254) NOT NULL,
  `select_pet` varchar(100) NOT NULL,
  `reason` varchar(100) NOT NULL,
  `bookings_date_time` datetime(6) NOT NULL,
  `appoitments_date_time` datetime(6) NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_contact` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_contact`;

CREATE TABLE `pets_cares_owners_communication_systems_app_contact` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `subject` varchar(100) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_customer` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_customer`;

CREATE TABLE `pets_cares_owners_communication_systems_app_customer` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `mobile` bigint NOT NULL,
  `address` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_doctors` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_doctors`;

CREATE TABLE `pets_cares_owners_communication_systems_app_doctors` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `speciality` varchar(100) NOT NULL,
  `license_number` varchar(100) NOT NULL,
  `contact_number` bigint NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `experience` int NOT NULL,
  `image` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_interest` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_interest`;

CREATE TABLE `pets_cares_owners_communication_systems_app_interest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `interest_date` datetime(6) NOT NULL,
  `customer_id` bigint NOT NULL,
  `pet_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pets_cares_owners_co_customer_id_64361074_fk_pets_care` (`customer_id`),
  KEY `pets_cares_owners_co_pet_id_765f5c78_fk_pets_care` (`pet_id`),
  CONSTRAINT `pets_cares_owners_co_customer_id_64361074_fk_pets_care` FOREIGN KEY (`customer_id`) REFERENCES `pets_cares_owners_communication_systems_app_customer` (`id`),
  CONSTRAINT `pets_cares_owners_co_pet_id_765f5c78_fk_pets_care` FOREIGN KEY (`pet_id`) REFERENCES `pets_cares_owners_communication_systems_app_pet` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_likes` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_likes`;

CREATE TABLE `pets_cares_owners_communication_systems_app_likes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_email` varchar(254) NOT NULL,
  `date_time` datetime(6) NOT NULL,
  `post_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pets_cares_owners_commun_post_id_customer_email_c6676f73_uniq` (`post_id`,`customer_email`),
  CONSTRAINT `pets_cares_owners_co_post_id_2eaa1549_fk_pets_care` FOREIGN KEY (`post_id`) REFERENCES `pets_cares_owners_communication_systems_app_add_posts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_pet` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_pet`;

CREATE TABLE `pets_cares_owners_communication_systems_app_pet` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `type` varchar(100) NOT NULL,
  `breed` varchar(100) NOT NULL,
  `age` int NOT NULL,
  `gender` varchar(100) NOT NULL,
  `weight` int NOT NULL,
  `height` double NOT NULL,
  `color` varchar(100) NOT NULL,
  `owner` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `sell_for` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_pets_likes` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_pets_likes`;

CREATE TABLE `pets_cares_owners_communication_systems_app_pets_likes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_email` varchar(254) NOT NULL,
  `date_time` datetime(6) NOT NULL,
  `pets_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pets_cares_owners_commun_pets_id_customer_email_72ce6fb3_uniq` (`pets_id`,`customer_email`),
  CONSTRAINT `pets_cares_owners_co_pets_id_5c1c5b2e_fk_pets_care` FOREIGN KEY (`pets_id`) REFERENCES `pets_cares_owners_communication_systems_app_pet` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_precautions` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_precautions`;

CREATE TABLE `pets_cares_owners_communication_systems_app_precautions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `pet` varchar(100) NOT NULL,
  `date_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_prescriptions` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_prescriptions`;

CREATE TABLE `pets_cares_owners_communication_systems_app_prescriptions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doctor_email` varchar(254) NOT NULL,
  `customer_email` varchar(254) NOT NULL,
  `title` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  `prescription_file` varchar(100) NOT NULL,
  `date_time` datetime(6) NOT NULL,
  `appoitments_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pets_cares_owners_co_appoitments_id_33f56b97_fk_pets_care` (`appoitments_id`),
  CONSTRAINT `pets_cares_owners_co_appoitments_id_33f56b97_fk_pets_care` FOREIGN KEY (`appoitments_id`) REFERENCES `pets_cares_owners_communication_systems_app_appoitments` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_quote` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_quote`;

CREATE TABLE `pets_cares_owners_communication_systems_app_quote` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doctor_email` varchar(100) NOT NULL,
  `customer_email` varchar(30) NOT NULL,
  `title` varchar(40) NOT NULL,
  `description` varchar(20) NOT NULL,
  `date_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Table structure for table `pets_cares_owners_communication_systems_app_reviews` */

DROP TABLE IF EXISTS `pets_cares_owners_communication_systems_app_reviews`;

CREATE TABLE `pets_cares_owners_communication_systems_app_reviews` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customer_email` varchar(100) NOT NULL,
  `reviews` longtext NOT NULL,
  `ratings` int NOT NULL,
  `date_time` datetime(6) NOT NULL,
  `doctors_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pets_cares_owners_co_doctors_id_dde1b7a8_fk_pets_care` (`doctors_id`),
  CONSTRAINT `pets_cares_owners_co_doctors_id_dde1b7a8_fk_pets_care` FOREIGN KEY (`doctors_id`) REFERENCES `pets_cares_owners_communication_systems_app_doctors` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
