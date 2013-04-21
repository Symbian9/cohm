
function initialize()
{
var mapProp = {
  center:x,
  zoom:4,
  mapTypeId:google.maps.MapTypeId.ROADMAP
  };
  
var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
