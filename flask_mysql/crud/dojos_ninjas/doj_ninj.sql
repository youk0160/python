-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema dojo_ninjas
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dojo_ninjas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojo_ninjas` DEFAULT CHARACTER SET utf8 ;
USE `dojo_ninjas` ;

-- -----------------------------------------------------
-- Table `dojo_ninjas`.`dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo_ninjas`.`dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `dojo_ninjas`.`ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojo_ninjas`.`ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `age` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `dojos_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_table2_dojos_idx` (`dojos_id` ASC) VISIBLE,
  CONSTRAINT `fk_table2_dojos`
    FOREIGN KEY (`dojos_id`)
    REFERENCES `dojo_ninjas`.`dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
