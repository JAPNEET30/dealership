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
categoriescontent='<p>categories</p>';
homecontent='<h1>Stocks</h1>\
  <div style="display:flex; flex-direction: column;" class="accordion" id="content">\
    <div class="accordion-item" style="padding:1rem;">\
        <h3>Jagdalpur</h3>\
        <div class="rounded" >\
          <div id="tables"></div>'+tabels()+'\
        </div>\
    </div>\
  </div>';
addcontent='<p>add page</p>';
updatecontent='<p>update page</p>';
deletecontent='<p>Delete page</p>';


categoriesbtn='<button class="btn btn-primary" type="button" onclick="home()">Home</button>\
      <button class="btn btn-primary active" type="button" >Categories</button>\
      <button class="btn btn-primary" type="button" onclick="add()">Add</button>\
      <button class="btn btn-primary" type="button" onclick="update()">Update</button>\
      <button class="btn btn-danger" type="button" onclick="del()">Delete</button>';

homebtn='<button class="btn btn-primary active" type="button" >Home</button>\
      <button class="btn btn-primary" type="button" onclick="categories()">Categories</button>\
      <button class="btn btn-primary" type="button" onclick="add()">Add</button>\
      <button class="btn btn-primary" type="button" onclick="update()">Update</button>\
      <button class="btn btn-danger" type="button" onclick="del()">Delete</button>';

addbtn='<button class="btn btn-primary" type="button" onclick="home()">Home</button>\
      <button class="btn btn-primary" type="button" onclick="categories()">Categories</button>\
      <button class="btn btn-primary active" type="button" >Add</button>\
      <button class="btn btn-primary" type="button" onclick="update()">Update</button>\
      <button class="btn btn-danger" type="button" onclick="del()">Delete</button>';

updatebtn='<button class="btn btn-primary" type="button" onclick="home()">Home</button>\
      <button class="btn btn-primary" type="button" onclick="categories()">Categories</button>\
      <button class="btn btn-primary" type="button" onclick="add()">Add</button>\
      <button class="btn btn-primary active" type="button" >Update</button>\
      <button class="btn btn-danger" type="button" onclick="del()">Delete</button>';

deletebtn='<button class="btn btn-primary" type="button" onclick="home()">Home</button>\
      <button class="btn btn-primary" type="button" onclick="categories()">Categories</button>\
      <button class="btn btn-primary" type="button" onclick="add()">Add</button>\
      <button class="btn btn-primary" type="button" onclick="update()">Update</button>\
      <button class="btn btn-danger active" type="button" >Delete</button>';

document.getElementById("dom").innerHTML=homecontent;
document.getElementById("footerbtn").innerHTML=homebtn;

function home(){
    document.getElementById("dom").innerHTML=homecontent;
    document.getElementById("footerbtn").innerHTML=homebtn;
}

function categories(){
    document.getElementById("dom").innerHTML=categoriescontent;
    document.getElementById("footerbtn").innerHTML=categoriesbtn;
}

function add(){
    document.getElementById("dom").innerHTML=addcontent;
    document.getElementById("footerbtn").innerHTML=addbtn;
}

function update(){
    document.getElementById("dom").innerHTML=updatecontent;
    document.getElementById("footerbtn").innerHTML=updatebtn;
}

function del(){
    document.getElementById("dom").innerHTML=deletecontent;
    document.getElementById("footerbtn").innerHTML=deletebtn;
}