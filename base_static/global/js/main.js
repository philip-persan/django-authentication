const btnUser = document.getElementById("user");
const drop = document.getElementById("drop");

drop.style.display = "none";

const showDrop = () => {
  if (drop.style.display == "none") {
    drop.style.display = "block";
  } else {
    drop.style.display = "none";
  }
};

btnUser.addEventListener("click", showDrop);
