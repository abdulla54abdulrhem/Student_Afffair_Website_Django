function passvalues()
{
    var studentId=document.getElementById("SID").value;
    localStorage.setItem("studentId",studentId);
    var radios=document.getElementsByName('a');
    var checkedans;
    for(var radio of radios)
    {
        if(radio.checked)
        {
            checkedans=radio.value;
        }
    }
    localStorage.setItem("checked",checkedans);
    var comp=document.getElementById('complaint').value;
    localStorage.setItem("comp",comp);
    return false;
}