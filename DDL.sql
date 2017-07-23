CREATE TABLE `user` (
  `uid` int(11) NOT NULL,
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) NOT NULL,
  `bdate` varchar(10) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`uid`,`fname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `admin` (
  `uid` int(11) NOT NULL,
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) NOT NULL,
  `bdate` varchar(10) NOT NULL,
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`uid`,`fname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
