USE `friendsdb` ;
/*INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
VALUES ("Jay", "Patel", "Instructor", NOW(), NOW());
INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
VALUES ("Jimmy", "Jun", "Instructor", NOW(), NOW());*/
CREATE TABLE IF NOT EXISTS `friendsdb`.`myfriends` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `age` INT,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;