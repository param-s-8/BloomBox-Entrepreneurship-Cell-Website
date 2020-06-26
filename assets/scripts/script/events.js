
function eventType(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "grid";
    evt.currentTarget.className += " active";
  }

function activateButton(){
      tablinks=document.getElementsByClassName("tablinks");
      tablinks[0].className+=" active";
  }


function moreImages(li){
    var imageTop=li.parentNode.parentNode.parentNode.querySelector(".imageTop");
    var n=li.parentNode.childNodes.length;
    elements=li.parentNode.querySelectorAll("li");
    for (i=0;i<elements.length;i++){
        elements[i].className=elements[i].className.replace("active","");
    }
    li.className+=" active";
    imageTop.src=li.querySelector("img").src;

}