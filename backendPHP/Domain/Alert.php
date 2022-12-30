<?php
class Alert{

    public $_nom_suspect;
    public $_adresse_ip;
    public $_nom_camera;
    public $_map_longitude;
    public $_map_latitude;
    public function setNomDuSuspect($nomcomplet)
    {
        return $this->_nom_suspect = $nomcomplet;
    }
    public function setIpDuSysteme($adresseIp)
    {
       return  $this->_adresse_ip = $adresseIp;
    }

    public function setNomCamera($nomCamera)
    {
       return  $this->_nom_camera = $nomCamera;
    }
    public function setGeoMap_Longitude($longitude)
    {
        $this->_map_longitude = $longitude;
    }
    public function setGeoMap_Latitude($latitude)
    {
        $this->_map_latitude = $latitude;
    }
    
    
    
}
?>