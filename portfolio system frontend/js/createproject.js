function projectcreate(){
   
//     <input type="text" placeholder="project name" id="Project Name" required>
//     <input type="text" placeholder="status" id="status" required>
//     <input type="text" placeholder="startdate" id="startdate" required>
//     <input type="text" placeholder="enddate" id="enddate" required>
//     <input type="text" placeholder="manager Id" id="managerid" required>
//    <input type="submit" onclick="projectcreate()">

    let name=document.getElementById("projectname").value;
    let email=document.getElementById("status").value;
    let status=document.getElementById("startdate").value;
    let role=document.getElementById("enddate").value;
    let mgid=document.getElementById("managerid").value;
    
    fetch("http://127.0.0.1:5000/create/project", {

    method: "POST",
    headers: {
        "content-type": "application/json"
    },
    body: JSON.stringify({
        "projectname":name,
        "status" : email,
        "startdate" :status,
        "enddate": role,
         "managerid":mgid
    })
}).then(response => {
    if(response.status == 201 | response.status == 200){
        response.json().then(data => {
            alert("Project sucessfully registered")
        });
    }else{
        response.json().then(data => alert(data.message));
    }
})


}