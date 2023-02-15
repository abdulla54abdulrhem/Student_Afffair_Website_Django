function validate()
{
   var gpa=document.getElementById('GPA').value;
   if(gpa>=4.0||gpa<0)
   {
       alert('Please, Enter a correct GPA');
       return false;
   }
}