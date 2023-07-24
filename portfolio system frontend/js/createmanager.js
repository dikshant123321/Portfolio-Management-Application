function registrationManager()
{

    let name=document.getElementById("name").value;
    let email=document.getElementById("email").value;
    let status=document.getElementById("status").value;
    let role=document.getElementById("role").value;
    let bio=document.getElementById("bio").value;
    let startdate=document.getElementById("startdate").value
    alert(name+" "+email+status+role+bio+startdate);
    fetch("http://127.0.0.1:5000/create/portfolio_manager", {

    method: "POST",
    headers: {
        "content-type": "application/json"
    },
    body: JSON.stringify({
        "name":name,
        "email":email,
        "status":status,
        "role":role,
        "bio":bio,
        "startdate":startdate
    })
}).then(response => {
    if(response.status == 201 | response.status == 200){
        response.json().then(data => {
            alert("Manager sucessfully registered")
        });
    }else{
        response.json().then(data => alert(data.message));
    }
})
}