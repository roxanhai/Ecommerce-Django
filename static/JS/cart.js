var updateBtn = document.getElementById("add-to-cart");
updateBtn.addEventListener("click", function () {
  //product_id & actions Được khai báo tương ứng với data-product_id và data-action
  var productID = this.dataset.product_id;
  var actions = this.dataset.action;
  var quantity = document.getElementById("product_quantity").value;
  console.log(
    "product_id:",
    productID,
    " action:",
    actions,
    "quantity",
    quantity
  );
  if (user == "AnonymousUser") {
    console.log("Not logged in");
    window.location.href = "/user/login/";
  } else {
    console.log(user);
    updateUserOrder(productID, actions, quantity);
    //   window.location.reload(); //Reload page
  }
});

// Cập nhật Order của Customer
function updateUserOrder(productID, actions, quantity) {
  console.log("User is logged in, sending data");
  var url = "/cart/add-to-cart/";
  // fetch is an API
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      productId: productID,
      actions: actions,
      quantity: quantity,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
