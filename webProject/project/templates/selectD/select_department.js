function check_level(){
    var x1=document.getElementById("lev1");
    var x2=document.getElementById("lev2");
    var x3=document.getElementById("lev3");
    var x4=document.getElementById("lev4");
    if(x1.checked==1){
        alert("Not allowed");
        document.getElementById("dep").disabled = true;
    }
    else if(x2.checked==1){
        alert("Not allowed");
        document.getElementById("dep").disabled = true;
    }
}