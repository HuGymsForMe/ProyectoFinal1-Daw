-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-05-2023 a las 14:51:42
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto_agenda`
--
CREATE DATABASE IF NOT EXISTS `proyecto_agenda` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `proyecto_agenda`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contactos_empresa`
--

DROP TABLE IF EXISTS `contactos_empresa`;
CREATE TABLE IF NOT EXISTS `contactos_empresa` (
  `num_cont` int(3) NOT NULL AUTO_INCREMENT,
  `telefono` int(9) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `fecha_ingreso` varchar(255) NOT NULL,
  `descripcion_empresa` varchar(255) NOT NULL,
  `pagina_web` varchar(255) NOT NULL,
  PRIMARY KEY (`num_cont`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `contactos_empresa`
--

INSERT INTO `contactos_empresa` (`num_cont`, `telefono`, `nombre`, `fecha_ingreso`, `descripcion_empresa`, `pagina_web`) VALUES
(1, 945633212, 'Oreo', '2023-05-09 13:00:00', 'Empresa de Galletas Estadounidense', 'oreo.com'),
(2, 956777301, 'Adidas', '2023-05-09 13:00:33', 'Empresa de Ropa y Complementos Deportivos', 'adidas.com'),
(3, 967444300, 'El País', '2023-05-09 13:01:22', 'Prensa Española', 'elpais.es'),
(4, 945600340, 'Facebook', '2023-05-09 13:04:34', 'Servicio de Redes y Medios Sociales', 'facebook.com'),
(5, 978444321, 'HMNLogistics', '2023-05-09 13:05:44', 'Empresa de Logística Española', 'hmnlogistics.es'),
(6, 956320133, 'Twitch', '2023-05-09 13:09:06', 'Empresa de Creadores de Contenido', 'twitch.tv'),
(7, 956888430, 'HP', '2023-05-09 13:11:17', 'Empresa Tecnológica', 'hp.com'),
(8, 994500323, 'Zara', '2023-05-09 13:12:34', 'Empresa de Ropa Española', 'zara.com'),
(9, 934555032, 'Restaurante La Barca', '2023-05-10 13:09:29', 'Restaurante ubicado en un distrito de Ciudad de México', 'labarca.mx'),
(10, 967330221, 'Llaollao', '2023-05-17 08:11:08', 'Franquicia de Heladerías', 'llaollao.com'),
(11, 950334445, 'Smint', '2023-05-17 08:14:47', 'Caramelos de Sabores', 'smint.com'),
(12, 940330219, 'Massimo Dutti', '2023-05-17 08:54:42', 'Tienda de Ropa del Grupo Inditex', 'massimodutti.com'),
(13, 956227301, 'Sony', '2023-05-17 16:33:42', 'Empresa Tecnológica', 'sony.com'),
(14, 903200113, 'Siemens', '2023-05-17 16:35:07', 'Marca de Electrodomésticos', 'siemens.com'),
(15, 906334500, 'Perfumerías Avenida', '2023-05-18 08:07:31', 'Productos de cosmética, maquillaje e higiene', 'perfumeriasavenida.es'),
(16, 901239430, 'AndorraTelecom', '2023-05-18 08:12:09', 'Empresa de telecomunicaciones de Andorra', 'andorratelecom.ad'),
(17, 903220001, 'DXRacer', '2023-05-20 14:17:47', 'Empresa fabricadora de material gaming', 'dxracer.fr'),
(18, 978333293, 'Abalorios Carlota', '2023-05-20 14:44:30', 'Tienda ubicada en la Calle Mayor de Guadalajara', 'abalarioscarlota.net'),
(19, 902568934, 'Mercadona', '2023-05-20 14:48:03', 'Supermercado de Productos Españoles', 'mercadona.es'),
(20, 991845321, 'Anaya', '2023-05-20 14:49:06', 'Editorial Española', 'anaya.es');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contactos_persona`
--

DROP TABLE IF EXISTS `contactos_persona`;
CREATE TABLE IF NOT EXISTS `contactos_persona` (
  `num_cont` int(3) NOT NULL AUTO_INCREMENT,
  `telefono` int(9) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `fecha_ingreso` varchar(100) NOT NULL,
  `cumpleanios` varchar(20) NOT NULL,
  PRIMARY KEY (`num_cont`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `contactos_persona`
--

INSERT INTO `contactos_persona` (`num_cont`, `telefono`, `nombre`, `fecha_ingreso`, `cumpleanios`) VALUES
(1, 647283021, 'Isabelina Grijalva Palacios', '2023-05-10 13:06:38', '2003-01-05'),
(2, 639222350, 'Hassan Berrios Macías', '2023-05-10 13:07:22', '1956-10-21'),
(3, 740322634, 'Tobías Luna Méndez', '2023-05-10 13:07:59', '1993-12-02'),
(4, 754034558, 'Aldous Pichardo Benavidez', '2023-05-10 13:12:49', '1973-09-09'),
(5, 983450234, 'Pepe Navarro Rosas', '2023-05-10 15:48:25', '1977-04-04'),
(6, 684931023, 'Pedro Pérez Sáez', '2023-05-16 13:38:30', '1970-03-03'),
(7, 604339841, 'Hugo Martínez Pérez', '2023-05-16 13:39:14', '1994-10-01'),
(8, 601330002, 'María Grande Peleas', '2023-05-16 20:06:47', '2000-10-21'),
(9, 605337945, 'Máximo de la Torre Sánchez', '2023-05-16 20:23:52', '1970-03-30'),
(10, 650392111, 'Laura Pérez Franciscano', '2023-05-16 21:26:25', '1989-09-28'),
(11, 693002343, 'Mario Hernández Almagro', '2023-05-17 08:15:11', '1999-09-01'),
(12, 675330222, 'Laura Sánchez Díaz', '2023-05-17 08:50:30', '1999-03-03'),
(13, 690543320, 'Marcos Amador Alonso', '2023-05-17 16:32:57', '1990-02-28'),
(14, 694993021, 'Julia Ceballos Prat', '2023-05-17 16:34:30', '1987-06-24'),
(15, 607453200, 'Marcos Bustamante Lin', '2023-05-17 16:35:47', '1984-08-22'),
(16, 697304556, 'Laura Anselmo López', '2023-05-18 08:05:35', '1987-02-14'),
(17, 693200195, 'Lucía Casas Pineda', '2023-05-18 08:06:20', '1978-09-19'),
(18, 602403924, 'Pedro Horonorato Otero', '2023-05-18 08:11:08', '1966-01-25'),
(19, 683201456, 'Pepe Lunas Pérez', '2023-05-20 14:14:45', '2000-01-24'),
(20, 690245631, 'Juan Hernández Gijón', '2023-05-20 14:43:10', '1973-08-10');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
