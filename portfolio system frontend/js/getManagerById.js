function submit(){
    // window.location.reload;
    // const managerTableBody = document.getElementById('manager-table-body');
     const container=document.getElementById("tables");
     const managerid=document.getElementById("managerid").value;
    fetch(`http://127.0.0.1:5000/get/portfolio_manager/${managerid}`,{


    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    }
    }).then(response =>{

        // console.log(response);

        if(response.status == 202 | response.status == 200){
            response.json().then(data => {
               
                console.log(data);
                console.log(data.pid)
                container.innerHTML=
               ` <table>
               <thead>
			<tr>
				<th>Manager Id</th>
				<th>Manager Name</th>
				<th>Manager Email</th>
				<th>Manager Status</th>
				<th>Manager Role</th>
				<th>Manager Bio</th>
                <th>Start Date</th>
			</tr>
		</thead>
		<tbody >
        <tr>
            <td>${data.pid}</td> 
            <td>${data.name}</td>
            <td>${data.email}</td>
            <td>${data.status}</td>
            <td>${data.role}</td>
            <td>${data.bio}</td>
            <td>${data.startdate}</td>
        </tr>  
        </tbody>
        </table>
        `
             
   
})
        }else{
            response.json().then(data => alert(data.message));
        }




    });
    
}