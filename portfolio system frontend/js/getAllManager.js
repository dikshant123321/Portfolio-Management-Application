// let name=document.getElementById("name").value;
// let email=document.getElementById("email").value;
// let status=document.getElementById("status").value;
// let role=document.getElementById("role").value;
// let bio=document.getElementById("bio").value;
// let startdate=document.getElementById("startdate").value

function allmanager(){
    const managerTableBody = document.getElementById('manager-table-body');
    
    fetch("http://127.0.0.1:5000/get/portfolio_manager",{


    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    }
    }).then(response =>{

        console.log(response);

        if(response.status == 202 | response.status == 200){
            response.json().then(data => {
               
                console.log(data);
                
               data.forEach(manager =>{

                const row = document.createElement('tr');
      row.innerHTML = `
        <td>${manager.pid}</td> 
        <td>${manager.name}</td>
        <td>${manager.email}</td>
        <td>${manager.status}</td>
        <td>${manager.role}</td>
        <td>${manager.bio}</td>
        <td>${manager.startdate}</td>
        <td><button type="button" onclick="updateman('${manager.pid}','${manager.name}','${manager.email}','${manager.status}','${manager.role}','${manager.bio}','${manager.startdate}')">update</button></td>
        <td><button button style="background-color:red" onclick="deleteRecord(${manager.pid})">Delete</button></td>
      `;
      managerTableBody.appendChild(row);
    
     })})
        }else{
            response.json().then(data => alert(data.message));
        }




    });
}

function updateman(pid,name,email,status,role,bio,startdate)
{ 
    localStorage.setItem("pid",pid);
    
    const url = `updateManager.html?pid=${pid}&name=${name}&email=${email}&status=${status}&role=${role}&bio=${bio}&startdate=${startdate}`;
    location.href= url;
}
function deleteRecord(pid)
{
    // alert("not implemented apis for delete")
    let choice=confirm("Are You Sure ? ");
  if(choice)
  {
    
    // const username= localStorage.getItem("userName");
    fetch("http://127.0.0.1:5000/delete/manager/"+pid, {

    method: "DELETE",
   
}).then(response => {
    if(response.status == 201 | response.status == 200){
        response.json().then(data => {
            alert("Manager sucessfully deleted: ");
            location.reload();
        });
    }else{
        response.json().then(data => alert(data.message));
    }
})
  }
}