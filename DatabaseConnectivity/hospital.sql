SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+02:00";


CREATE TABLE `Hospital_Information` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
   beds int(6) NOT NULL,
   available int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


