CREATE TABLE `users` (
  `id` integer PRIMARY KEY,
  `username` varchar(255),
  `name` varchar(255),
  `password` varchar(255)
);

CREATE TABLE `topics` (
  `id` integer PRIMARY KEY,
  `name` varchar(255),
  `type_id` integer,
  `description` varchar(255)
);

CREATE TABLE `favorite_topics` (
  `user_id` int,
  `topic_id` int
);

CREATE TABLE `topic_types` (
  `id` integer PRIMARY KEY,
  `name` varchar(255)
);

CREATE TABLE `comments` (
  `id` integer PRIMARY KEY,
  `user_id` integer,
  `topic_id` integer,
  `body` varchar(255),
  `timestamp` datetime
);

ALTER TABLE `favorite_topics` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `favorite_topics` ADD FOREIGN KEY (`topic_id`) REFERENCES `topics` (`id`);

ALTER TABLE `topic_types` ADD FOREIGN KEY (`id`) REFERENCES `topics` (`type_id`);

ALTER TABLE `comments` ADD FOREIGN KEY (`topic_id`) REFERENCES `topics` (`id`);

ALTER TABLE `comments` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
