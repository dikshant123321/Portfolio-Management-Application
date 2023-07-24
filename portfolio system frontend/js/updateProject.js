


const urlParam=new URLSearchParams(window.location.search);
//projectid,projectname,status,startdate,enddate,managerid
const projectid=urlParam.get('projectid');
const projectname=urlParam.get('projectname');
const mstatus=urlParam.get('status');
const startdate=urlParam.get('startdate');
const enddate=urlParam.get('enddate');
const managerid=urlParam.get('managerid');

document.getElementById('projectid').value = projectid;
document.getElementById('projectname').value = projectname;
document.getElementById('status').value =mstatus;
document.getElementById('startdate').value = startdate;
document.getElementById('enddate').value = enddate;
document.getElementById('managerid').value =managerid;


function updateProject()
{
    const fromlocal=localStorage.getItem("projectid")
    let id=document.getElementById('projectid').value;
    let names=document.getElementById('projectname').value;
    let statuss=document.getElementById('status').value;
    let stdate=document.getElementById('startdate').value;
    let eddate=document.getElementById('enddate').value ;
    let mgid=document.getElementById('managerid').value;
    alert("in update project function");
    fetch("http://127.0.0.1:5000/update/project/"+fromlocal, {

    method: "PUT",
    headers: {
        'Content-Type': 'application/json',
       
    },
    body: JSON.stringify({
        "projectid":id,
        "projectname":names,
        "status" :statuss,
        "startdate" :stdate,
        "enddate": eddate,
         "managerid":mgid
        
    })
}).then(response => {
    if(response.status == 201 | response.status == 202){
        response.json().then(data => {
            alert("Project sucessfully updated")
            window.location.href= 'getAllProject.html';
            
        });
    }else{
        response.json().then(data => alert(data.message));
       
           
    }
})

// 

}