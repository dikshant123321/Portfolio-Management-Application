function allproject(){
    const managerTableBody = document.getElementById('project-table-body');
    
    fetch("http://127.0.0.1:5000/get/project",{
        // <!-- projectname = data.get('projectname')
        // status=data.get('status')
        // startdate=data.get('startdate')
        // enddate=data.get('enddate')
        // managerid = data.get('managerid') -->

    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    }
    }).then(response =>{

        console.log(response);

        if(response.status == 202 | response.status == 200){
            response.json().then(data => {
               
                console.log(data);
                
               data.forEach(project =>{

                const row = document.createElement('tr');
      row.innerHTML = `
        <td>${project.projectid}</td> 
        <td>${project.projectname}</td>
        <td>${project.status}</td>
        <td>${project.startdate}</td>
        <td>${project.enddate}</td>
        <td>${project.managerid}</td>
        <td><button type="button" onclick="updateman('${project.projectid}','${project.projectname}','${project.status}','${project.startdate}','${project.enddate}','${project.managerid}')">update</button></td>
        <td><button button style="background-color:red" onclick="deleteRecord(${project.projectid})">Delete</button></td>
      `;
      managerTableBody.appendChild(row);
    
     })})
        }else{
            response.json().then(data => alert(data.message));
        }




    });
}

function updateman(projectid,projectname,status,startdate,enddate,managerid)
{ 
    localStorage.setItem("projectid",projectid);
    
    const url = `updateProject.html?projectid=${projectid}&projectname=${projectname}&status=${status}&startdate=${startdate}&enddate=${enddate}&managerid=${managerid}`;
    location.href= url;
}
function deleteRecord(projectid)
{
    // alert("not implemented apis for delete")
    let choice=confirm("Are You Sure ? ");
  if(choice)
  {
    
    // const username= localStorage.getItem("userName");
    fetch("http://127.0.0.1:5000/delete/project/"+projectid, {

    method: "DELETE",
   
}).then(response => {
    if(response.status == 201 | response.status == 200){
        response.json().then(data => {
            alert("Project sucessfully deleted: ");
            location.reload();
        });
    }else{
        response.json().then(data => alert(data.message));
    }
})
  }
}