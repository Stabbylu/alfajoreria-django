// ************************************************
// Pipo Carrito de compras
// ************************************************

var shoppingCart = (function () {
    // =============================
    // Private methods and propeties
    // =============================
    cart = [];
  
    // Constructor del Carrito
    function Item(foto, name, price, count) {
        this.foto = foto;
        this.name = name;
        this.price = price;
        this.count = count;
    }
  
    // Guardar Carrito
    function guardarCarrito() {
        sessionStorage.setItem('shoppingCart', JSON.stringify(cart));
    }
  
    // Carga el Carrito
    function cargarCarrito() {
        cart = JSON.parse(sessionStorage.getItem('shoppingCart'));
    }
    if (sessionStorage.getItem("shoppingCart") != null) {
        cargarCarrito();
    }
  
  
    // =============================
    // Public methods and propeties
    // =============================
    var obj = {};
  
    // Agrega productos al carrito
    obj.agregaItemAlCarrito = function (foto, name, price, count) {
        for (var item in cart) {
            if (cart[item].name === name) {
                cart[item].count++;
                console.log('ENTRE A AUMENTAR EL ITEM: ' + cart[item].count);
                guardarCarrito();
                return;
            }
        }
        console.log('NUEVO ITEM');
        var item = new Item(foto, name, price, count);
        cart.push(item);
        guardarCarrito();
    }

    // Cuenta los items del carrito
    obj.actualizarCantidadItem = function (name, count) {
        for (var i in cart) {
            if (cart[i].name === name) {
                cart[i].count = count;
                break;
            }
        }
    };

    // Elimina un item del carrito
    obj.eliminaItemCarrito = function (name) {
        for (var item in cart) {
            if (cart[item].name === name) {
                cart[item].count--;
                if (cart[item].count === 0) {
                    cart.splice(item, 1);
                }
                break;
            }
        }
        guardarCarrito();
    }
  
    // Elimina todos los items del carrito
    obj.eliminaItemCarritoTodos = function (name) {
        for (var item in cart) {
            if (cart[item].name === name) {
                cart.splice(item, 1);
                break;
            }
        }
        guardarCarrito();
    }
  
    // Limpia el Carrito
    obj.limpiaCarrito = function () {
        cart = [];
        guardarCarrito();
    }
  
    // Cantidad de cada item
    obj.totalCount = function () {
        var totalCount = 0;
        for (var item in cart) {
            totalCount += cart[item].count;
        }
        return totalCount;
    }
  
    // Calcula Total Carrito Precio * Cantidad
    obj.totalCart = function () {
        var totalCart = 0;
        for (var item in cart) {
            totalCart += cart[item].price * cart[item].count;
        }
        return Number(totalCart.toFixed(0));
    }
  
    // Lista del Carrito
    obj.listCart = function () {
        var cartCopy = [];
        for (i in cart) {
            item = cart[i];
            itemCopy = {};
            for (p in item) {
            itemCopy[p] = item[p];
    
            }
            itemCopy.total = Number(item.price * item.count).toFixed(0);
            cartCopy.push(itemCopy)
        }
        return cartCopy;
    }
  
    return obj;
})();
  
  
// *****************************************
// Eventos
// ***************************************** 
// Agregar Item al Carrito
$('.add-to-cart').click(function (event) {
    event.preventDefault();
    var foto = $(this).data('foto');
    var name = $(this).data('name');
    var price = Number($(this).data('price').replace('.',''));
    shoppingCart.agregaItemAlCarrito(foto, name, price, 1);
    displayCart();
});
  
// Limpiar Items
$('.limpiaCarrito').click(function () {
    shoppingCart.limpiaCarrito();
    displayCart();
});

  
function displayCart() {
    var cartArray = shoppingCart.listCart();
    var output = "";
    for (var i in cartArray) {
    output += "<tr>"
        // Imagen Producto
        + "<td> <img src='"+ cartArray[i].foto +"' class='img-fluid img-thumbnail' alt='"+ cartArray[i].name +"-foto'>" +"</td>"
        // Nombre Producto
        + "<td>" + cartArray[i].name + "</td>"
        // Precio Producto
        + "<td>$" + cartArray[i].price + "</td>"
        // Cantidad Input
        + "<td><input type='number' class='item-count form-control' data-name='" + cartArray[i].name + "' value='" + cartArray[i].count + "'></td>"
        // Total Precio
        + "<td>$" + cartArray[i].total + "</td>"
        // Eliminar Producto
        + "<td><button class='delete-item btn btn-danger' data-name=" + cartArray[i].name + "><i class='bi bi-trash' style='color:white;'></i></button></td>"
        + "</tr>";
    }
    $('.show-cart').html(output);
    $('.total-cart').html(shoppingCart.totalCart());
    $('.total-count').html(shoppingCart.totalCount());
}
  
  // Eliminar item del carrito
$('.show-cart').on("click", ".delete-item", function (event) {
    var name = $(this).data('name');
    shoppingCart.eliminaItemCarritoTodos(name);
    displayCart();
})
  
// Cuando cambie el numero de items del carrito
$('.show-cart').on("change", ".item-count", function (event) {
    var name = $(this).data('name');
    var count = Number($(this).val());
    shoppingCart.actualizarCantidadItem(name, count);
    displayCart();
});
  
displayCart();
  