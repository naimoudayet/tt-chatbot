// ip address: always change it - commande: netstat
const String ip = "192.168.1.15";

// BASE URL
const String baseUrl = "http://$ip:5000/api";

// all stations
const String agencesUrl = "$baseUrl/agences";
const String loginUrl = "$baseUrl/login";
const String inscriptionUrl = "$baseUrl/inscription";
const String profileUrl = "$baseUrl/profile";
const String searchUrl = "$baseUrl/search";
const String offresUrl = "$baseUrl/offres";
