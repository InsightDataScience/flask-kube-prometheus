
var button = document.getElementById("get-repos")

function getRepos() {
  var username = document.getElementById("username").value;

  $.ajax({
    type: "GET",
    url: "/get-repos",
    data: {"username": username},
    success: function (d) {
      updateList(d.repos);
    }
  });
}

function updateList(arr) {
  $("#repo-list").empty();

  var list = document.getElementById("repo-list");

  for (i=0, len=arr.length; i<len; i++) {
    var li = document.createElement("li");
    li.innerHTML = arr[i];
    list.appendChild(li);
  }
}
