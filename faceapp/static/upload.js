var p1;

function preview(file) {

    var prevDiv = document.getElementById('preview');
    if (file.files && file.files[0]) {
      var reader = new FileReader();
      reader.onload = function(evt) {
        prevDiv.innerHTML = '<img class="mdui-img-rounded mdui-center mdui-m-a-5 mdui-shadow-12" height=600 width=600 src="' + evt.target.result + '" />';
        p1=evt.target.result;
      }
      reader.readAsDataURL(file.files[0]);
     
    } else {
      prevDiv.innerHTML = '<div class="img" style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale,src=\'' + file.value + '\'"></div>';
    }
  }

  function preview2(file) {
    var prevDiv = document.getElementById('preview2');
    if (file.files && file.files[0]) {
      var reader = new FileReader();
      reader.onload = function(evt) {
        prevDiv.innerHTML = '<img class="mdui-img-rounded mdui-center mdui-m-a-5 mdui-shadow-12" height=600 width=600 src="' + evt.target.result + '" />';
      }
      reader.readAsDataURL(file.files[0]);
    } else {
      prevDiv.innerHTML = '<div class="img" style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale,src=\'' + file.value + '\'"></div>';
    }
  }

  function preview3(file) {
    var prevDiv = document.getElementById('preview3');
    if (file.files && file.files[0]) {
      var reader = new FileReader();
      reader.onload = function(evt) {
        prevDiv.innerHTML = '<img class="mdui-img-rounded mdui-center mdui-m-a-5 mdui-shadow-12" height=600 width=600 src="' + evt.target.result + '" />';
      }
      reader.readAsDataURL(file.files[0]);
    } else {
      prevDiv.innerHTML = '<div class="img" style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale,src=\'' + file.value + '\'"></div>';
    }
  }


  function preview4(file) {
    var prevDiv = document.getElementById('preview4');
    if (file.files && file.files[0]) {
      var reader = new FileReader();
      reader.onload = function(evt) {
        prevDiv.innerHTML = '<img class="mdui-img-rounded mdui-center mdui-m-a-5 mdui-shadow-12" height=600 width=600 src="' + evt.target.result + '" />';
      }
      reader.readAsDataURL(file.files[0]);
    } else {
      prevDiv.innerHTML = '<div class="img" style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale,src=\'' + file.value + '\'"></div>';
    }
  }

  
  function preview5(file) {
    var prevDiv = document.getElementById('preview5');
    if (file.files && file.files[0]) {
      var reader = new FileReader();
      reader.onload = function(evt) {
        prevDiv.innerHTML = '<img class="mdui-img-rounded mdui-center mdui-m-a-5 mdui-shadow-12" height=600 width=600 src="' + evt.target.result + '" />';
      }
      reader.readAsDataURL(file.files[0]);
    } else {
      prevDiv.innerHTML = '<div class="img" style="filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale,src=\'' + file.value + '\'"></div>';
    }
  }

  // document.getElementById("submit1").onclick=upload1();
  function upload1(){
    var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("POST","faceapp/upload1/",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send(p1);

  }

  function upload2(){
    var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
  }
xmlhttp.open("POST","faceapp/get_face_feat/",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send(p1);

  }



