



const urlParam=new URLSearchParams(window.location.search);
// updateManager.html?pid=${pid}&name=${name}&email=${email}&status=${status}&role=${role}&bio=${bio}&startdate=${startdate}`;
const pid=urlParam.get('pid');
const mname=urlParam.get('name');
const email=urlParam.get('email');
const mstatus=urlParam.get('status');
const role=urlParam.get('role');
const bio=urlParam.get('bio');
const startdate=urlParam.get('startdate');

document.getElementById('pid').value = pid;
document.getElementById('name').value = mname;
document.getElementById('email').value =email;
document.getElementById('status').value = mstatus;
document.getElementById('role').value = role;
document.getElementById('bio').value =bio;
document.getElementById('startdate').value=startdate;

function updateManager()
{
    const fromlocal=localStorage.getItem("pid")
    let id=document.getElementById('pid').value;
    let names=document.getElementById('name').value;
    let emails=document.getElementById('email').value;
    let statuss=document.getElementById('status').value;
    let roles=document.getElementById('role').value;
    let bios=document.getElementById('bio').value ;
    let startdates=document.getElementById('startdate').value;
    alert(bios)
    fetch("http://127.0.0.1:5000/update/portfolio_manager/"+fromlocal, {

    method: "PUT",
    headers: {
        'Content-Type': 'application/json',
       
    },
    body: JSON.stringify({
        "pid":id,
        "name":names,
        "email":emails,
        "status":statuss,
        "role":roles,
        "bio":bios,
        "startdate":startdates
        
    })
}).then(response => {
    if(response.status == 201 | response.status == 202){
        response.json().then(data => {
            alert("Manager sucessfully updated")
            location.href= 'getAllManager.html';
            
        });
    }else{
        response.json().then(data => alert(data.message));
        location.href= 'getAllManager.html';
           
    }
})

// 

}