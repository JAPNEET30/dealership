function tabels(){
    tab='<table class="table table-striped table-primary table-bordered">\
    <thead><tr>\
              <th>#</th>\
              <th>Model</th>\
              <th>Varient</th>\
              <th>Quantity</th>\
          </tr></thead>\
      <tbody><tr>\
              <th>1</th>\
              <td>Activa</td>\
              <td>Disc</td>\
              <td>10</td>\
          </tr>\
          <tr>\
              <th>2</th>\
              <td>Pleasure</td>\
              <td>Drum</td>\
              <td>5</td>\
          </tr></tbody></table>'
          for(i=0;i<3;i++){
            tab+=tab;}
      return tab
  }
departmentscontent='<p>departments</p>';
memberscontent='<p>members</p>';
homecontent='<h1>Home</h1>\
  <div style="display:flex; flex-direction: column;" class="accordion" id="content">\
    <div class="accordion-item" style="padding:1rem;">\
        <h3>Jagdalpur</h3>\
        <div class="rounded">\
          <div id="tables"></div>'+tabels()+'\
        </div>\
    </div>\
  </div>';
logtimecontent='<p>Log time setting</p>';

departmentsbtn='<button class="btn btn-primary" type="button" onclick="home()">Home</button>\
      <button class="btn btn-primary" type="button" onclick="members()">Members</button>\
      <button class="btn btn-primary active" type="button" >Departments</button>\
      <button class="btn btn-primary" type="button" onclick="logtime()">Login Times</button>';

membersbtn='<button class="btn btn-primary" type="button" onclick="home()">Home</button>\
      <button class="btn btn-primary active" type="button">Members</button>\
      <button class="btn btn-primary" type="button" onclick="departments()">Departments</button>\
      <button class="btn btn-primary" type="button" onclick="logtime()">Login Times</button>';

homebtn='<button class="btn btn-primary active" type="button">Home</button>\
      <button class="btn btn-primary" type="button" onclick="members()">Members</button>\
      <button class="btn btn-primary" type="button" onclick="departments()">Department</button>\
      <button class="btn btn-primary" type="button" onclick="logtime()">Login Times</button>';

logtimebtn='<button class="btn btn-primary" type="button" onclick="home()">Home</button>\
      <button class="btn btn-primary" type="button" onclick="members()">Members</button>\
      <button class="btn btn-primary" type="button" onclick="departments()">Department</button>\
      <button class="btn btn-primary active" type="button">Login Times</button>';

document.getElementById("dom").innerHTML=homecontent;
document.getElementById("footerbtn").innerHTML=homebtn;

function home(){
    document.getElementById("dom").innerHTML=homecontent;
    document.getElementById("footerbtn").innerHTML=homebtn;
}

function members(){
    document.getElementById("dom").innerHTML=memberscontent;
    document.getElementById("footerbtn").innerHTML=membersbtn;
}

function departments(){
    document.getElementById("dom").innerHTML=departmentscontent;
    document.getElementById("footerbtn").innerHTML=departmentsbtn;
}

function logtime(){
    document.getElementById("dom").innerHTML=logtimecontent;
    document.getElementById("footerbtn").innerHTML=logtimebtn;
}